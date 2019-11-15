exports.RootNode = function RootNode() {
	this.type = "root";
	this.variables = {};
	this.functions = {};
	this.statements = [];

	// TODO: possibly remove this and track in execution
	this.addStatements = function(statementArr) {
		statementArr.forEach(node => {
			switch(node.type) {
				case "function":
					this.functions[node.name] = node;
					this.statements.push(node);
					break;
				case "variable_dec":
					node.declarations.forEach(assignmentNode => {
						this.variables[node.name] = node;
						this.statements.push(assignmentNode);
					})
					break;
				default:
					console.log(`${node.type} is an invalid node type`);
			}
		});
	}
}

exports.FunctionNode = function FunctionNode(name) {
	this.type = "function";
	this.name = name;
	this.parent = null;
	this.params = null;
	this.body = null;
}

exports.ArithmeticExprNode = function ArithmeticExprNode(operator) {
	this.type = "arithmetic_expr";
	this.parent = null;
	this.operator = operator;
	this.leftSide = null;
	this.rightSide = null;
}

exports.VariableDecNode = function VariableDecNode() {
	this.type = "variable_dec";
	this.parent = null;
	this.declarations = [];
}

exports.AssignmentNode = function AssignmentNode(name) {
	this.type = "assignment";
	this.parent = null;
	this.name = name;
	this.expr = null;
}

exports.ParamsNode = function ParamsNode(paramsArr) {
	this.type = "params";
	this.parent = null;
	this.params = paramsArr;
}

exports.IdentifierNode = function IdentifierNode(name) {
	this.type = "identifier";
	this.parent = null;
	this.name = name;
}

exports.ValueNode = function ValueNode(value) {
	this.type = "value";
	this.parent = null;
	this.value = value;
}