#include <iostream>
#include "varinode.h"

using namespace std;


varinode::varinode(/* args */){
    name = "null";
    value = 0;
    vtype = "null";
}

varinode::varinode(string newname){
    if(newname == "true"){                 // Boolean node has name true or false
        value = 1;
        vtype = "boolean";
    }
    else if(newname == "false"){
        value = 0;
        vtype = "boolean";
    }
    else{
        name = newname;
        bool trigger = true;
        if(newname[0] == '-'){
            for(int i = 1; i < newname.size();i++){
                if (!isdigit(newname[i]))
                    trigger = false;
            }
        }
        else{
            for(int i = 0; i < newname.size();i++){
                if (!isdigit(newname[i]))
                    trigger = false;                 // All digit varinode should be a integer, else it is a character
            }
        }
        if(trigger == true){
            value = stoi(newname);
            vtype = "integer";
        }
        else{
            value = 0;
            vtype = "character";
        }
    }
}

varinode::varinode(const varinode& newnode){
    name = newnode.name;
    value = newnode.value;
    vtype = newnode.vtype;
}

varinode& varinode::operator = (varinode const &obj) { 
    value = obj.value;
    name = obj.name;
    vtype = obj.vtype;
    return *this; 
}


varinode& varinode::operator >> (varinode const &obj){
    if(vtype == "character"){
    value = obj.value;
    }
    else{
        std::cout << "Invalid Assignment" << std::endl;
        exit(0);
    }
    return *this; 
}


void varinode::SetValue(int newvalue){
     value = newvalue;
}

void varinode::SetName(std::string newname){
     name = newname;
}


string varinode::GetName(){
    return name;
}

int varinode::GetValue(){
    return value;
}

varinode::~varinode(){

}