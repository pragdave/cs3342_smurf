//
//  binding.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 12/6/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "binding.hpp"


binding::binding(){}

void binding::insertValue(string var, int val){
    binds.insert({var, val});
}

int binding::getBindingValue(string var){
    return binds.at(var);
}

