//
//  intNode.cpp
//  smurfFinalProject
//
//  Created by Alden Shiverick on 11/19/19.
//  Copyright © 2019 Alden Shiverick. All rights reserved.
//

#include "intNode.hpp"

intNode::intNode() {
    val = value;
}

void intNode::createInt (int x) {
    value = x;
}

intNode::~intNode() {
    value = NULL;
}
