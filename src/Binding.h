#ifndef BINDING
#define BINDING
#include <string>
#include <map>
#include "func.h"
#include "astNode.h"
using namespace std;
class func;
class Binding{
public:
	vector<map<string, int>> list;
	map<string, func*> funclist;
	void add(string s, int i) {
		list[list.size()-1][s] = i;
	};
	int get(string s) { //go through the bindings from the top down
		for (int i = list.size()-1; i >= 0; i--) {
			map<string, int>::iterator it = list[i].find(s);
			if (it != list[i].end()) {
				return list[i][s];
			}
		}
		return 9999999;
	};
	void add(string s, func* f) {
		this->funclist[s] = f;
	};
	func* getFunc(string s) {
		map<string, func*>::iterator it = funclist.find(s);
		if (it != funclist.end()) {
			return funclist[s];
		}
		func* f = nullptr;
		return f;
	};
};
#endif BINDING