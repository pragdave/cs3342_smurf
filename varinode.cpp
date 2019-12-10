#include <iostream>
#include "varinode.h"

using namespace std;


varinode::varinode(/* args */){
    name = "null";
    value = 0;
    vtype = "null";
}

varinode::varinode(string newname){
    if(newname == "true"){
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
                    trigger = false;
            }
        }
        if(trigger == true){
       // cout << newname << " is a number" << endl;
            value = stoi(newname);
            vtype = "integer";
        }
        else{
            value = 0;
            vtype = "character";
       // cout << newname << " is a character" << endl;
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
    std::cout << vtype << " and " << obj.vtype << std::endl;
    if(vtype == "character"){
    //c.SetName(a.name);
    value = obj.value;
    //c.vtype = "character";
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