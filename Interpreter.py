from arpeggio import PTNodeVisitor
from Bindings import Bindings
import AstNodes as nodes

class Interpreter(PTNodeVisitor):    
    ##############
    #Math Portion#
    ##############
    
    def evaluate_number(self, node, bindings):
        #print("number:",node.sign,node.value)
        if node.sign == "-":
            return -1 * int(node.value)
        return int(node.value)
        
    def evaluate_var_ref(self, node, bindings):
        return bindings.getVal(node.ident)
            
    def evaluate_factor(self, node, bindings):
        return node.value.accept(self, bindings)
        
    def evaluate_mult_term(self, node, bindings):
        #print("in multTerm")
        multTerm = node.factor.accept(self, bindings)
        #print("bindings:",bindings)
        #print("multTerm:",multTerm)
        #print("multTermIsStr:", isinstance(multTerm, str))
        #print("multTermIsObject:", isinstance(multTerm, object))
        #print("multTermIsInt:", isinstance(multTerm, int))
        for i in range(1, len(node.multAndFactList), 2):
            if node.multAndFactList[i-1] == "*":
                multTerm *= node.multAndFactList[i].accept(self, bindings)
            else:
                multTerm /= node.multAndFactList[i].accept(self, bindings)
        return int(multTerm)
        
    def evaluate_arithmetic_expression(self, node, bindings):
        #print("arithmetic_expression")
        expr = node.multTerm.accept(self, bindings)
        #print("expr:",expr)
        for i in range(1, len(node.plusAndTermList), 2):
            if i and node.plusAndTermList[i-1] == "-":
                expr -= node.plusAndTermList[i].accept(self, bindings)
            else:
                expr += node.plusAndTermList[i].accept(self, bindings)
        #print("done arithmetic_expression")
        return int(expr)
    
    ####################
    #Built in Functions#
    ####################
    
    def evaluate_var_decl(self, node, bindings):
        #print("varDecl")
        bindings.setVal(node.name, node.expr.accept(self, bindings))
    
    def evaluate_var_let(self, node, bindings):
        for decl in node.list:
            if isinstance(decl, str):
                print("varLet")
                self.bindings.setVal(decl, 0)
            else:
                decl.accept(self, bindings)
    
    def evaluate_boolean_expression(self, node, bindings):
        left = node.left.accept(self, bindings)
        right = node.right.accept(self, bindings)
        
        if node.op == "==":
            return int(left == right)
        elif node.op == "!=":
            return int(left != right)
        elif node.op == ">=":
            return int(left >= right)
        elif node.op == ">":
            return int(left > right)
        elif node.op == "<=":
            return int(left <= right)
        else:
            return int(left < right)
    
    def evaluate_print_func(self, node, bindings):
        list = node.listOfList[0]
        printLine = ""
        for expr in list:
            print("expr:",expr)
            printLine += str(expr.accept(self, bindings))
            printLine += "|"
        printLine = printLine[:-1]
        print("Print:",printLine)
        return printLine
        
    def evaluate_code_block(self, node, bindings, fn_decl):
        lastLine = node.list[-1]
        
        if fn_decl == True:
            return lastLine
        
        if len(node.list) > 1:
            for line in node.list:
                line.accept(self, bindings)
                
        return lastLine.accept(self, bindings)
        
    def evaluate_if_statement(self, node, bindings):
        boolVal = node.boolExpr.accept(self, bindings)
        if boolVal == 1:
            return node.ifBlock.accept(self, bindings)
        return node.elseBlock.accept(self, bindings)
    
    def evaluate_fn_decl(self, node, bindings):
        if isinstance(node.name, str):
            print("function declaration:",node.name)
        else:
            print("function declaration:",node.name.ident)
        if isinstance(node.paramList, str):
            #Figure out how to set x as the paramList not 2
            #Need to set x to 2
            codeBlock = bindings.getVal(node.codeBlock.name)
            funcToRun = node.codeBlock.accept(self, bindings)
            print("node.name:",node.name.ident)
            print("node.codeBlock.accept:",funcToRun)
            print("node.codeBlock.name:",node.codeBlock.name.ident)
            print("bindings:",bindings)
            print("node.codeBlock.name:",funcToRun.name)
            funcToRunParamList = funcToRun.paramList[0].ident
            paramsToPass = node.codeBlock.paramList
            print("node.codeBlock.paramList:",funcToRunParamList)
            print("n:",paramsToPass[0].accept(self,bindings))
            print("codeBlock:",codeBlock)
            print("node.codeBlockBinding:",node.codeBlock)
            
            bindingToPass = codeBlock[2].binding
            #set n = 2)
            
            paramsToSet = codeBlock[0]
            print(paramsToSet)
            
            #params to pass: 2
            index = 0
            for param in paramsToPass:
                bindingToPass[paramsToSet[index]] = param.accept(self,bindings)
                index += 1
            
            print("bindingToPass:",bindingToPass)
            
            bindings.setFunc(node.name.ident, funcToRunParamList, funcToRun, Bindings(bindingToPass,bindings))
            
            
            print("NOT BROKEN")
            return codeBlock[1].accept(self, bindings)
        else:
            if isinstance(node.name, str):
                return node
            else:
                newBindings = Bindings(bindings, {})
                bindings.setFunc(node.name.ident, node.paramList, node.codeBlock, newBindings)
                print("bindings:",bindings)
                return node.codeBlock.accept(self, bindings, True)
        
    def evaluate_fn_let(self, node, bindings):
        for decl in node.list:
            decl.accept(self, bindings)
            
    def evaluate_fn_call(self, node, bindings):
        print("funcCall")
        bindingsTemp = bindings.copy()
        function = bindingsTemp.getVal(node.name)
        parameters = function[0]
        code = function[1]
        index = 0
        for param in parameters:
            val = node.paramList[index].accept(self,bindings)
            bindingsTemp.setVal(param, node.paramList[index].accept(self, bindings))
            index += 1
        print("Done evaluating func call")
        print(bindingsTemp.binding)
        if isinstance(code, nodes.Fn_Decl):
            return code.codeBlock.accept(self, bindingsTemp)
        return code.accept(self, bindingsTemp)
    
    ####################
    #Top Level Function#
    ####################
        
    def evaluate_code(self, node):
        globalBinding = Bindings(None, {})
        for expr in node.list:
            value = expr.accept(self, globalBinding)
        return value;
