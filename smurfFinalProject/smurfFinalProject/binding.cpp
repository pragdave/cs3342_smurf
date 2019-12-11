//
//  binding.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 12/6/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "binding.hpp"


binding::binding(){
//    printBindings();
}

void binding::insertValue(string var, int val){
    binds.insert(pair<string, int>(var, val));
    binds[var] = val;
    //cout<<"I have inserted something to the binds"<<endl;
}

int binding::getBindingValue(string var){
    //cout<<"Binds variable: "<<binds[var]<<endl;
    int result = binds.find(var)->second;
    if(result != 0){
        cout<<"result"<<endl;
        return result;
    }
    cout<<"Value: "<<result<<endl;
    return result;
}

//void binding::printBindings(){
//    cout<<"Do we even get here??"<<endl;
//}
