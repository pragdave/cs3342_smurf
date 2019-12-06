//
//  binding.hpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 12/6/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#ifndef binding_hpp
#define binding_hpp
#include <map>
#include <string>
#include <stdio.h>

using namespace std;

class binding{
public:
    map<string, int> binds;
    binding();
    void insertValue(string, int);
    int getBindingValue(string);
};

#endif /* binding_hpp */
