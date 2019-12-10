#include "cpp-peglib-master/peglib.h"
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm> 
#include "visitor.h"
#include "ast_node.h"
#include "interpreter.h"

using namespace peg;
using namespace std;

auto grammar = R"(
        program <-  _? assign / if_statement /expr+
        if_statement  <-  'if' _ compare block ('else' _ block)?  
        assign  <-  'let ' character assign_op _  expr / character assign_op _  expr
        expr    <-  term ( add_op _ term )* 
        term    <-  primary ( mul_op _ primary )*
        primary <-  number / character / '(' _ expr ')' _ 
        compare <-  expr com_op _ expr / expr
        block   <-  '{' _ expr+ '}' _ 
        add_op  <-  '+' / '-'
        mul_op  <-  '*' / '/'
        com_op  <-  '==' / '!=' / '<' / '<=' / '>' / '>='
        assign_op <-  '='
        character <- <[a-z][a-z0-9]* > _ 
        number  <-  '-'? < [0-9]+ > _ 
        ~_         <- [ \t\r\n]*
    )";

class Visitor;


    //  number  <-  '-'? < [0-9]+ > _

////////////////////
//  ParseTreeNode

class ParseTreeNode{
    AstNode *content;

public:
    ParseTreeNode(){};
    ParseTreeNode(AstNode *content_node){
        content = content_node;
    }

    AstNode *get() const{
        return content;
    }

    string to_string(){
        return content->to_string();
    }
};

AstNode *bin_op(const SemanticValues &sv){
    AstNode *left = sv[0].get<ParseTreeNode>().get();
    for (auto i = 1u; i < sv.size(); i += 2){
        AstNode *right = sv[i + 1].get<ParseTreeNode>().get();
        string op = sv[i].get<ParseTreeNode>().get()->to_string();
        left = new BinopNode(left, op, right);
    }
    return left;
};


AstNode  *If_Node(const SemanticValues &sv){
    if(sv.size() == 2){
        AstNode *cond = sv[0].get<ParseTreeNode>().get();
        AstNode *ifs = sv[1].get<ParseTreeNode>().get();
        AstNode *ans = new IfNode(cond,ifs);
        return ans;
    }
    else if(sv.size() == 3){
        AstNode *cond = sv[0].get<ParseTreeNode>().get();
        AstNode *ifs = sv[1].get<ParseTreeNode>().get();
        AstNode *elses = sv[2].get<ParseTreeNode>().get();
        AstNode *ans = new IfNode(cond,ifs,elses);
        return ans;
    }
    else{
        cout << "Error on If Syntax" << endl;
        exit(0);
    }
}


void setup_ast_generation(parser &parser, vector<vector<varinode*>>& List, int& layer){
    parser["expr"] = [&](const SemanticValues &sv) {
        AstNode *n = bin_op(sv);
        return ParseTreeNode(n);
    };



    parser["if_statement"] = [&](const SemanticValues &sv) {
        AstNode *n = If_Node(sv);
        return ParseTreeNode(n);
    };

    parser["add_op"] = [&](const SemanticValues &sv) {
        return ParseTreeNode(new OpNode(sv.str()));
    };

    parser["mul_op"] = [&](const SemanticValues &sv) {
        return ParseTreeNode(new OpNode(sv.str()));
    };

    parser["com_op"] = [&](const SemanticValues &sv) {
        return ParseTreeNode(new OpNode(sv.str()));
    };

    parser["assign_op"] = [&](const SemanticValues &sv) {
        return ParseTreeNode(new OpNode(sv.str()));
    };

    parser["term"] = [&](const SemanticValues &sv) {
        AstNode *n = bin_op(sv);
        return ParseTreeNode(n);
    };

    parser["assign"] = [&](const SemanticValues &sv) {
        AstNode *n = bin_op(sv);
        return ParseTreeNode(n);
    };

    parser["compare"] = [&](const SemanticValues &sv) {
        AstNode *n = bin_op(sv);
        return ParseTreeNode(n);
    };

    parser["character"] = [&](const SemanticValues &sv) {
        string charnode(sv.str());
        charnode.erase(remove(charnode.begin(), charnode.end(), ' '), charnode.end()); 
        varinode* newnode = new varinode(charnode);
        bool trigger = false;
        for(int i = 0; i < List.at(layer).size(); i++){
            if(List.at(layer).at(i)->GetName() == charnode){
                 AstNode* ListNode = new VarinodeNode(List.at(layer).at(i));
                return ParseTreeNode(ListNode); 
            }
        }
        AstNode* ListNode = new VarinodeNode(newnode);
        List.at(layer).push_back(newnode); 
        return ParseTreeNode(ListNode); 
    };

    parser["number"] = [&](const SemanticValues &sv) {
        string integernode(sv.str());
        int temp = atoi(sv.c_str());
        varinode* varnode = new varinode(to_string(temp));
        return ParseTreeNode(new VarinodeNode(varnode));
    };
}

void filter(vector<string>& List, string& inputline, bool& trigger){
    List.clear();
    std::size_t found = inputline.find("print(");
    if (found!=std::string::npos){
        std::size_t found2 = inputline.find_last_of(")");
        if (found2!=std::string::npos){
            inputline = inputline.substr(found + 6, found2-found - 6);
            trigger = true;
        }
    }

    std::size_t found3 = inputline.find("#");
    if (found3!=std::string::npos){
        inputline = inputline.substr(0, found3 - 1);
    }
    int last = 0;
    for(int i = 0; i < inputline.size(); i++){
        if(inputline.at(i) == ','){
            string newpart = inputline.substr(last, i-last);
            List.push_back(newpart);
            last = i + 1;
        }
    }
    if(last == 0){
        List.push_back(inputline);
    }
    else{
        string newpart = inputline.substr(last, inputline.size()-last);
        List.push_back(newpart);
    }
}

int main(int argc, const char **argv){
    vector<vector<varinode*>> VariableList;
    vector<varinode*> FirstLayer;
    VariableList.push_back(FirstLayer);
    int layer = 0;

    if (argc > 1){
        cout << "Reading from command line..." << endl;
            //char* a = argv[1];
        return 1;
    }

    ifstream infile("expr.smu");
    while(!infile.eof()){
        string newline;
        vector<string> CommandList;
        bool printtrigger = false;
        getline(infile,newline);
        filter(CommandList, newline,printtrigger);
    
        parser parser(grammar);
        ParseTreeNode val = ParseTreeNode();
        setup_ast_generation(parser, VariableList, layer);
        for(int i = 0; i < CommandList.size(); i++){
            auto expr = CommandList.at(i).c_str();
            if (parser.parse(expr,val)){
                if(printtrigger == true){
                    cout << "expr: print(" << val.to_string() << ")";
                    cout << "\n======== Print out: " << val.get()->accept(new Interpreter())->GetValue() << " ========\n" << endl;
                }
                else{
                    cout << "expr: " << val.to_string() << endl;
                    val.get()->accept(new Interpreter());
                }
            }
        }
    }
    infile.close();
}