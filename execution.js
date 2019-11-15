exports.ExecuteStatement = function ExecuteStatement(node) {
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
		default:
			console.log(`${node.type} is an invalid node type`);
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
	return node.value;
}

ExecuteArithmeticExpr = function ExecuteArithmeticExpr(node) {
	let value = 0;
	let leftSide = node.leftSide;
	let rightSide = node.rightSide;
	if (leftSide.type === "arithmetic_expr") {
		leftSide = ExecuteArithmeticExpr(leftSide);
	}
	if (rightSide.type === "arithmetic_expr") {
		rightSide = ExecuteArithmeticExpr(rightSide);
	}
	switch(node.operator) {
		case "+":
			value = leftSide.value + rightSide.value;
			break;
		case "-":
			value = leftSide.value - rightSide.value;
			break;
		case "*":
			value = leftSide.value * rightSide.value;
			break;
		case "/":
			value = leftSide.value / rightSide.value;
			break;
		default:
			console.log(`${this.operator} is an invalid operator`);
	}
	return value; // TODO: possibly return node somewhere?
}

ExecuteParams = function ExecuteParams(node) {
	return node.params.map(param => {
		return exports.ExecuteStatement(param);
	})
}