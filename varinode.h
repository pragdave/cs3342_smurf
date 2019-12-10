#ifndef VARINODE_H
#define VARINODE_H


#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>


class varinode{
private:
    std::string name;
    int value;
public:
    std::string vtype;
    varinode();
    varinode(std::string);
    varinode(const varinode&);
    varinode& operator = (varinode const&); 
    varinode& operator >> (varinode const&); 
    varinode Assign(varinode const&, varinode const&);

    void SetValue(int);
    void SetName(std::string);
    std::string GetName();
    int GetValue();
    ~varinode();

friend varinode operator + (varinode const& a , varinode const& b){
    varinode c;
    int Tvalue = a.value+b.value; 
    c.SetValue(Tvalue);
    c.SetName(std::to_string(Tvalue));
    c.vtype = "integer";
    return c;
}

friend varinode operator - (varinode const& a , varinode const& b){
    varinode c;
    c.vtype = "integer";
    int newValue = a.value-b.value;
    c.SetValue(newValue);
    c.SetName(std::to_string(newValue));
    return c;
}

friend varinode operator * (varinode const& a , varinode const& b){
    varinode c;
    c.vtype = "integer";
    int newValue = a.value*b.value;
    c.SetValue(newValue);
    c.SetName(std::to_string(newValue));
    return c;
}

friend varinode operator / (varinode const& a , varinode const& b){
    varinode c;
    c.vtype = "integer";
    int newValue = a.value/b.value;
    c.SetValue(newValue);
    c.SetName(std::to_string(newValue));
    return c;
}


friend varinode operator == (varinode const& a , varinode const& b){
    if(a.value == b.value){
        varinode c("true");
        return c;
    }
    else{
        varinode c("false");
        return c;
    }
}


friend varinode operator != (varinode const& a , varinode const& b){
    if(a.value != b.value){
        varinode c("true");
        return c;
    }
    else{
        varinode c("false");
        return c;
    }
}


friend varinode operator > (varinode const& a , varinode const& b){
    if(a.value > b.value){
        varinode c("true");
        return c;
    }
    else{
        varinode c("false");
        return c;
    }
}


friend varinode operator >= (varinode const& a , varinode const& b){
    if(a.value >= b.value){
        varinode c("true");
        return c;
    }
    else{
        varinode c("false");
        return c;
    }
}


friend varinode operator < (varinode const& a , varinode const& b){
    if(a.value < b.value){
        varinode c("true");
        return c;
    }
    else{
        varinode c("false");
        return c;
    }
}


friend varinode operator <= (varinode const& a , varinode const& b){
    if(a.value <= b.value){
        varinode c("true");
        return c;
    }
    else{
        varinode c("false");
        return c;
    }
}


friend std::ostream& operator<<(std::ostream& os, const varinode& dt){
    os << dt.value << std::endl;;
    return os;
}

};


#endif

