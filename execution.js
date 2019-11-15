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
	const params = ExecuteParams(node.children.params);
	return node.children.body(params);
}

ExecuteValue = function ExecuteValue(node) {
	return node.getValue();
}

ExecuteIdentifier = function ExecuteIdentifier(node) {
	return node.getValue();
}

ExecuteArithmeticExpr = function ExecuteArithmeticExpr(node) {
	return node.executeExpr().getValue();
}

ExecuteParams = function ExecuteParams(node) {
	return node.children.map(param => {
		return exports.ExecuteStatement(param);
	})
}