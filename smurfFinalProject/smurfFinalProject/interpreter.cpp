//
//  interpreter.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/20/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "interpreter.hpp"
using namespace std;

int interpreter::evaluate_integer(node *nodex, int value){
    return value;
}

int interpreter::evaluate_binop(node *nodex, node *left, string operation, node *right){
    int lval = left->accept(this);
    int rval = right->accept(this);
    return evaluateOperator[operation](lval, rval);
}

int interpreter::evaluate_assignment(node *nodex, node *left, node *right){
    left->accept(this);                                              //sets the variableName
    int rval = right->accept(this);
    this->bindings->insertValue(variableName, rval);
    int value = this->bindings->getBindingValue(variableName);
    return value;
}

int interpreter::evaluate_variable(node *nodex, string var){
    variableName = var;
//    int value = this->bindings->getBindingValue(variableName);
    return 0;
}

int interpreter::evaluate_statement(node *nodex){
    int result = 0;
    result = nodex->accept(this);
    return result;
}

int interpreter::evaluate_code(vector<node*> nodex){
    int result=212121212;
    int result1 = 0;
    int result2 = 0;
    //cout<<"Just tell me you tried to evaluate the code"<<endl;
    cout<<"Number of children nodes: "<<nodex.size()<<endl;
    cout<<"Node: "<<nodex[0]->str()<<endl;
    cout<<"Node: "<<nodex[1]->str()<<endl;
//    for(int i=0; i<nodex.size(); i++){
//        result = nodex[i]->accept(this);
//        cout<<"Result: "<<result<<endl;
//    }
    result1 = nodex[0]->accept(this);
    result2 = nodex[1]->accept(this);
    
    return result1;
    
    //    node statement;
//    int result = 0;
////    cout<<"Do you try to evaluate code??"<<endl;
//    cout<<"Statement at nodex[0]:"<<nodex[0]->str()<<endl;
//    for(int i=0; i<nodex.size(); i++){
//        result = nodex[i]->accept(this);
//    }
////    cout<<"Result at nodex[0]: "<<result<<endl;
//
////    for(int i=0; i<nodex.size(); i++){
////        statement = *nodex[i];
////        result = statement.accept(this);
////        cout<<"Result: "<<result<<endl;
////    }
//    return result;
    
}

//int interpreter::evaluate_ifstatement(node *nodex, node *expr, node *children){
//
//}



