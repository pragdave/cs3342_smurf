#include "cpp-peglib-master/peglib.h"
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <dirent.h> 
#include <stdexcept>
#include <locale.h>
#include "visitor.h"
#include "ast_node.h"
#include "interpreter.h"


using namespace peg;
using namespace std;

auto grammar = R"(
        program <-  _? function / _? assign / if_statement /expr+
        if_statement  <-  'if' _ compare block ('else' _ block)?  
        function <-  'let' _ character assign_op _ 'fn' _ '()' _ block _ / 'let' _ character assign_op _ 'fn(' _ character ')' _ block _  / character _ '()' _ / character '(' _ number ')' _ 
        assign  <-  'let' _ character assign_op _  expr / character assign_op _  expr
        expr    <-  term ( add_op _ term )* 
        term    <-  primary ( mul_op _ primary )*
        primary <-  number / character / '(' _ expr ')' _ 
        compare <-  expr com_op _ expr / expr
        block   <-  '{' _ expr+ '}' _ 
        add_op  <-  '+' / '-'
        mul_op  <-  '*' / '/'
        com_op  <-  '==' / '!=' / '>=' / '<=' / '>' / '<'
        assign_op <-  '='
        character <- <[a-z][a-z0-9]* > _ 
        number  <-  '-'? < [0-9]+ > _ 
        ~_         <- [ \t\r\n]*
    )";

class Visitor;


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


AstNode *Func_Node(const SemanticValues &sv, vector<vector<varinode*>>& List, int& layer){
    if(sv.size() == 4){                                                      // If it is the delcaration of a function with parameter
        AstNode *name = sv[0].get<ParseTreeNode>().get();
        AstNode *parameter = sv[2].get<ParseTreeNode>().get();
        AstNode *execution = sv[3].get<ParseTreeNode>().get();
        AstNode *ans = new FuncNode(name, parameter, execution, &List, &layer, 5); 
        return ans;
    }
    else if(sv.size() == 3){                                               // If it is the implementation of a function with parameter
        AstNode *name = sv[0].get<ParseTreeNode>().get();
        AstNode *execution = sv[2].get<ParseTreeNode>().get();
        AstNode *ans = new FuncNode(name, execution, &List, &layer, 3); 
        return ans;
    }
    else if(sv.size() == 2){                                               // If it is the delcaration of a function without parameter
        AstNode *name = sv[0].get<ParseTreeNode>().get();
        AstNode *parameter = sv[1].get<ParseTreeNode>().get();
        AstNode *ans = new FuncNode(name, parameter, &List, &layer, 4); 
        return ans;
    }
    else if(sv.size() == 1){                                               // If it is the implementation of a function without parameter
        AstNode *name = sv[0].get<ParseTreeNode>().get();
        AstNode *ans = new FuncNode(name, &List, &layer, 2); 
        return ans;
    }
    else{
        cout << "Error on Func_Node" << endl;
        exit(0);
    }
}


AstNode  *If_Node(const SemanticValues &sv){
    if(sv.size() == 2){
        AstNode *cond = sv[0].get<ParseTreeNode>().get();           // If there is no else expression 
        AstNode *ifs = sv[1].get<ParseTreeNode>().get();
        AstNode *ans = new IfNode(cond,ifs);
        return ans;
    }
    else if(sv.size() == 3){                                        // If there is a else expression
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

    parser["function"] = [&](const SemanticValues &sv) {
        AstNode *n = Func_Node(sv, List, layer);
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
            if(List.at(layer).at(i)->GetName() == charnode){                    // If it is already delcared, we find it on the List
                 AstNode* ListNode = new VarinodeNode(List.at(layer).at(i));
                return ParseTreeNode(ListNode); 
            }
        }
        AstNode* ListNode = new VarinodeNode(newnode);                 // If it is firstly declared, create a new one
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


void getAllFiles( string path, vector<string>& files) {   //https://www.cnblogs.com/fnlingnzb-learner/p/6424563.html
  long  hFile  =  0; 
  struct _finddata_t fileinfo; 
  string p; 
  if((hFile = _findfirst(p.assign(path).append("\\*").c_str(),&fileinfo)) != -1) 
  { 
    do
    {  
      if((fileinfo.attrib & _A_SUBDIR)) 
      { 
        if(strcmp(fileinfo.name,".") != 0 && strcmp(fileinfo.name,"..") != 0) 
        {
         files.push_back(p.assign(path).append("\\").append(fileinfo.name) );
          getAllFiles( p.assign(path).append("\\").append(fileinfo.name), files ); 
        }
      } 
      else
      { 
        files.push_back(p.assign(path).append("\\").append(fileinfo.name) ); 
      } 
    }while(_findnext(hFile, &fileinfo) == 0); 
    _findclose(hFile); 
  } 
}




void CombineLine(vector<string>& List, string& inputline, vector<int>& TriggerList, int& ileft, int& iright){
    int left = 0;                                      // Combine inputs, which are in different lines like the if-statement, into a single line
    int right = 0;
    std::size_t found = inputline.find("#");           // Delete the Comment
    if (found != std::string::npos){
       inputline = inputline.substr(0, found);
    }

    if(inputline.size() == 0){
        return;
    }

    for(int i = 0; i < inputline.size(); i++){
        if(inputline.at(i) == '{')
            left++;
        if(inputline.at(i) == '}')
            right++;
    }

    if(ileft == iright ){
        std::size_t found1 = inputline.find("else");
        if (found1 != std::string::npos){
            std::size_t found2 = inputline.find("if");
            if (found2 != std::string::npos){
                List.push_back(inputline);
                TriggerList.push_back(0);
                ileft = 0;
                iright = 0;
            }
            else{
                List.at(List.size() - 1) = List.at(List.size() - 1) + inputline;
                iright = right + iright;
                ileft = left + ileft;
            }
        }
        else{
            List.push_back(inputline);
            TriggerList.push_back(0);
            ileft = left + ileft;
            iright = right + iright;
        }
    }
    else if(left + ileft == right + iright){
        List.at(List.size() - 1) = List.at(List.size() - 1) + inputline;
        ileft = 0;
        iright = 0;
    }
    else{
        List.at(List.size() - 1) = List.at(List.size() - 1) + inputline;
        iright = right + iright;
        ileft = left + ileft;
    }
}


void PrintWord(vector<string>& StringList, vector<int>& PrintTrigger){            // Identify Print command
    for(int i = 0; i < StringList.size(); i++){
        string newline = StringList.at(i);
        std::size_t found = newline.find("print(");
        while(found!=std::string::npos){
            PrintTrigger.at(i) = 1;
            newline = newline.substr(0, found) + newline.substr(found+6, newline.size() - found - 6);
            std::size_t found1 = newline.find_last_of(")");
            if(found1!=std::string::npos)
                newline = newline.substr(0, found1) + newline.substr(found1 + 1, newline.size() - found1 -1);
            found = newline.find("print(");
        }
        StringList.at(i) = newline;
    }
}

void SplitWord(vector<string>& StringList, vector<int>& PrintTrigger){          // Split commands that has ' into different lines 
    vector<string> newStringList;
    vector<int> newTriggerList;
    for(int i = 0; i < StringList.size(); i++){
        string newline = StringList.at(i);
        std::size_t found = newline.find(",");
        bool findsign = false;
        while(found!=std::string::npos){
            newStringList.push_back(newline.substr(0,found));
            newline = newline.substr(found + 1, newline.size() - found -1);
            findsign = true;
            if(PrintTrigger.at(i) == 1){
                newTriggerList.push_back(2);
            }
            else{
                newTriggerList.push_back(0);
            }
            found = newline.find(",");
        }

        if(newline.size() != 0){
            if(PrintTrigger.at(i) == 1 && findsign == true){
                newStringList.push_back(newline);
                newTriggerList.push_back(3);
            }
            else if(PrintTrigger.at(i) == 1){
                newStringList.push_back(newline);
                newTriggerList.push_back(1);
            }
            else{
                newStringList.push_back(newline);
                newTriggerList.push_back(0);
            }
        }
    }
    StringList = newStringList;
    PrintTrigger = newTriggerList;
}


int main(int argc, const char **argv){

    string filename("test_cases");
    vector<string> files;
    getAllFiles(filename, files);
    for(int a = 0; a < files.size(); a++){
        vector<vector<varinode*>> VariableList;
        vector<varinode*> FirstLayer;
        vector<string> CommandList;
        vector<int> PrintTrigger;
        int left = 0;
        int right = 0;
        VariableList.push_back(FirstLayer);
        int layer = 0;
        int funcNum = 0;
        
        cout<< files.at(a) << endl;
        ifstream infile(files.at(a));
        if(!infile){
            cout << "Unable to open file" << endl;
            exit(0);
        }
        while(!infile.eof()){
            string newline;
            getline(infile,newline);
            CombineLine(CommandList, newline, PrintTrigger, left, right);
        }
        infile.close();
        PrintWord(CommandList, PrintTrigger);
        SplitWord(CommandList, PrintTrigger);
        for(int i = 0; i < CommandList.size(); i++){
            parser parser(grammar); 
            setup_ast_generation(parser, VariableList, layer);
            ParseTreeNode val = ParseTreeNode();
            auto expr = CommandList.at(i).c_str();
            if (parser.parse(expr,val)){
                if(PrintTrigger.at(i) == 1){
                    cout << "expr: print(" << val.to_string() << ")" << endl;                  // Ways to output the result
                    cout << "======== Print out: " << val.get()->accept(new Interpreter())->GetValue() << " ========\n" << endl;
                }
                else if(PrintTrigger.at(i) == 2){
                    cout << "expr: print(" << val.to_string() << ") |";
                    cout << "Print out: " << val.get()->accept(new Interpreter())->GetValue() << " | ";
                }
                else if(PrintTrigger.at(i) == 3){
                    cout << "expr: print(" << val.to_string() << ") |";
                    cout << "Print out: " << val.get()->accept(new Interpreter())->GetValue() << "\n" << endl;
                }
                else{
                    cout << "expr: " << val.to_string() << endl;
                    val.get()->accept(new Interpreter());
                }
            }
            else{
                cout << "Error on testing..." << endl;
            }
        }
    }
}