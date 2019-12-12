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
        multTerm = node.factor.accept(self, bindings)
        for i in range(1, len(node.multAndFactList), 2):
            if node.multAndFactList[i-1] == "*":
                multTerm *= node.multAndFactList[i].accept(self, bindings)
            else:
                multTerm /= node.multAndFactList[i].accept(self, bindings)
        return int(multTerm)
        
    def evaluate_arithmetic_expression(self, node, bindings):
        #print("arithmetic_expression")
        expr = node.multTerm.accept(self, bindings)
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
    
    ###################
    #Cusotom Functions#
    ###################
    
    def evaluate_fn_decl(self, node, bindings):
        if isinstance(node.name, str):
            print("\nFUNC_DECL:",node.name)
        else:
            print("\nFUNC_DECL:",node.name.ident)
            
        if isinstance(node.paramList, str):
            codeBlock = bindings.getVal(node.codeBlock.name)
            funcToRun = node.codeBlock.accept(self, bindings)
            funcToRunParamList = funcToRun.paramList
            paramsToPass = node.codeBlock.paramList
            paramsToSet = codeBlock[0]
            bindingToPass = Bindings(codeBlock[-1].binding, {})
            
            print("node.name:",node.name.ident)
            print("node.codeBlock.accept:",funcToRun)
            print("node.codeBlock.name:",node.codeBlock.name.ident)
            print("bindings:",bindings)
            print("funcToRun.name:",funcToRun.name)
            print("funcToRunParamList:",funcToRunParamList)
            print("n:",paramsToPass[0].accept(self,bindings))
            print("codeBlock:",codeBlock)
            print("paramsToSet:",paramsToSet)
            print("bindingToPass:",bindingToPass.binding)
            
            index = 0
            for param in paramsToPass:
                bindingToPass.setVal(paramsToSet[index], param.accept(self,bindings))
                #bindingToPass[paramsToSet[index]] = param.accept(self,bindings)
                index += 1
            
            #print("bindingToPass:",bindingToPass.binding)
            
            bindings.setFunc(node.name.ident, funcToRunParamList, funcToRun, bindingToPass)
            return codeBlock[1].accept(self, bindings)
        else:
            if isinstance(node.name, str):
                print("NODE:",node)
                print("BINDINGS:",bindings)
                return node
            else:
                print("node:",node)
                print("node.name:",node.name.ident)
                newBindings = Bindings(bindings, {})
                bindings.setFunc(node.name.ident, node.paramList, node.codeBlock, newBindings)
                print("bindings:",bindings)
                print("newBindings:",newBindings)
                return node.codeBlock.accept(self, newBindings, True)
        
    def evaluate_fn_let(self, node, bindings):
        for decl in node.list:
            decl.accept(self, bindings)
            
    def evaluate_fn_call(self, node, bindings):
        print("\nFUNC_CALL")
        print(node.name.ident)
        print("bindings:",bindings)
        #function = bindings.getVal(node.name)
        function = bindings.getVal(node.name.ident)
        parameters = function[0]
        code = function[1]
        bindingsTemp = function[-1].copy()
        print("function call bindings:",bindingsTemp)
        
        index = 0
        for param in parameters:
            bindingsTemp.setVal(param, node.paramList[index].accept(self, bindings))
            index += 1
        
        print("bindingsTemp:",bindingsTemp)
        print("Done evaluating func call")
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
