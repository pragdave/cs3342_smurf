//
//  binding.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 12/6/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "binding.hpp"


binding::binding(){
    //printBindings();
}

void binding::insertValue(string var, int val){
    binds.insert(pair<string, int>(var, val));
    binds[var] = val;
}

int binding::getBindingValue(string var){
    int result = binds.find(var)->second;
    if(result != 0){
        return result;
    }
    return result;
}

