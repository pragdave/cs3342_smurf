exports.ExecuteStatement = function ExecuteStatement(node) {
	return ExecuteNode(node);
}

variables = {};
functions = {};

ExecuteNode = function ExecuteNode(node) {
	let returnVal = null;
	switch(node.type) {
		case "function":
			returnVal = ExecuteFunction(node);
			break;
		case "value":
			returnVal = ExecuteValue(node);
			break;
		case "identifier":
			returnVal = ExecuteIdentifier(node);
			break;
		case "arithmetic_expr":
			returnVal = ExecuteArithmeticExpr(node);
			break;
		case "params":
			returnVal = ExecuteParams(node);
			break;
		case "assignment":
			returnVal = ExecuteAssignment(node);
			break;
		default:
			console.log(`${node.type} is an invalid node type --execution`);
	}
	return returnVal;
}

ExecuteFunction = function ExecuteFunction(node) {
	const params = ExecuteParams(node.params);
	return node.body(params);
}

ExecuteValue = function ExecuteValue(node) {
	return node.value;
}

ExecuteIdentifier = function ExecuteIdentifier(node) {
	return variables[node.name];
}

ExecuteArithmeticExpr = function ExecuteArithmeticExpr(node) {
	let value = 0;
	let leftSide = node.leftSide;
	let rightSide = node.rightSide;
	if (leftSide.type) {
		leftSide = ExecuteNode(leftSide);
	}
	if (rightSide.type) {
		rightSide = ExecuteNode(rightSide);
	}
	switch(node.operator) {
		case "+":
			value = leftSide + rightSide;
			break;
		case "-":
			value = leftSide - rightSide;
			break;
		case "*":
			value = leftSide * rightSide;
			break;
		case "/":
			value = Math.floor(leftSide / rightSide);
			break;
		default:
			console.log(`${this.operator} is an invalid operator --execution`);
	}
	return value;
}

ExecuteParams = function ExecuteParams(node) {
	return node.params.map(param => {
		return ExecuteNode(param);
	})
}

ExecuteAssignment = function ExecuteAssignment(node) {
	const value = ExecuteNode(node.expr);
	variables[node.name] = value;
	return value;
}