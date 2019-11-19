exports.GenerateAST = function GenerateAST(statements) {
	const rootNode = new RootNode();
	nodes = statements.map(s => GenerateNode(s));
	rootNode.addStatements(nodes);
	return rootNode;
}

GenerateNode = function GenerateNode(statement) {
	if (!statement.type) {
		return {};
	}

	let newNode = {};
	switch(statement.type) {
		case "function":
			const body = statement.body;
				// TODO: GenerateNode for statement.body
			newNode = new FunctionNode(statement.fcn_name);
			const params = statement.params.map(p => GenerateNode(p)).filter(p => !!p && !!p.type);
			const paramsNode = new ParamsNode(params);
			newNode.params = paramsNode;
			paramsNode.parent = newNode;
			newNode.body = body;
			// body.parent = newNode;
			break;
		case "integer":
			newNode = new ValueNode(statement.value);
			break;
		case "identifier":
			newNode = new IdentifierNode(statement.name);
			break;
		case "arithmetic_expr":
			const operator = statement.params[1];
			newNode = new ArithmeticExprNode(operator);
			GenerateExprChildren(newNode, statement.params);
			break;
		case "boolean_expr":
			const op = statement.params[1];
			newNode = new BooleanExprNode(op);
			GenerateExprChildren(newNode, statement.params);
			break;
		case "variable_dec":
			newNode = new VariableDecNode();
			statement.declarations.forEach(d => {
				const decNode = GenerateNode(d);
				newNode.declarations.push(decNode);
				decNode.parent = newNode;
			});
			break;
		case "assignment":
			newNode = new AssignmentNode(statement.name);
			const exprNode = GenerateNode(statement.expr);
			newNode.expr = exprNode;
			exprNode.parent = newNode;
			break;
		case "if":
			newNode = new IfNode();
			newNode.evaluation = GenerateNode(statement.evaluation);
			newNode.statements = statement.statements.map(s => {
				statementNode = GenerateNode(s);
				statementNode.parent = newNode;
				return statementNode;
			});
			newNode.elseStatements = statement.else_statements.map(s => {
				statementNode = GenerateNode(s);
				statementNode.parent = newNode;
				return statementNode;
			});
			break;
		default: 
			console.log(`${statement.type} is an invalid statement type`);
	}
	return newNode;
}

GenerateExprChildren = function GenerateExprChildren(node, params) {
	let leftParams = params[0];
	if (!leftParams.type && leftParams.length > 1) {
		leftParams = leftParams[1];
	}
	const leftSide = GenerateNode(leftParams);
	node.leftSide = leftSide;
	leftSide.parent = node;
	let rightParams = params[2];
	if (!rightParams.type && rightParams.length > 1) {
		rightParams = rightParams[1];
	}
	const rightSide = GenerateNode(rightParams);
	node.rightSide = rightSide;
	rightSide.parent = node;
}

RootNode = function RootNode() {
	this.type = "root";
	this.statements = [];

	// TODO: possibly remove this and track in execution
	this.addStatements = function(statementArr) {
		statementArr.forEach(node => {
			switch(node.type) {
				case "variable_dec":
					node.declarations.forEach(assignmentNode => {
						this.statements.push(assignmentNode);
					})
					break;
				case "assignment":
					this.statements.push(node);
					break;
				case "function":
					this.statements.push(node);
					break;
				case "if":
					this.statements.push(node);
					break;
				default:
					console.log(`${node.type} is an invalid node type --treeNodes`);
			}
		});
	}
}

IfNode = function IfNode() {
	this.type = "if";
	this.parent = null;
	this.evaluation = null;
	this.statements = [];
	this.elseStatements = [];
}

FunctionNode = function FunctionNode(name) {
	this.type = "function";
	this.name = name;
	this.parent = null;
	this.params = null;
	this.body = null;
}

ArithmeticExprNode = function ArithmeticExprNode(operator) {
	this.type = "arithmetic_expr";
	this.parent = null;
	this.operator = operator;
	this.leftSide = null;
	this.rightSide = null;
}

BooleanExprNode = function BooleanExprNode(operator) {
	this.type = "boolean_expr";
	this.parent = null;
	this.operator = operator;
	this.leftSide = null;
	this.rightSide = null;
}

VariableDecNode = function VariableDecNode() {
	this.type = "variable_dec";
	this.parent = null;
	this.declarations = [];
}

AssignmentNode = function AssignmentNode(name) {
	this.type = "assignment";
	this.parent = null;
	this.name = name;
	this.expr = null;
}

ParamsNode = function ParamsNode(paramsArr) {
	this.type = "params";
	this.parent = null;
	this.params = paramsArr;
}

IdentifierNode = function IdentifierNode(name) {
	this.type = "identifier";
	this.parent = null;
	this.name = name;
}

ValueNode = function ValueNode(value) {
	this.type = "value";
	this.parent = null;
	this.value = value;
}