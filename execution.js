exports.ExecuteStatement = function ExecuteStatement(node) {
	return ExecuteNode(node);
}

variables = {};
functions = {
	print: (paramsArr) => {
			let printString = "";
			paramsArr.forEach((p,i) => {
			
			if (i !== 0) {
				printString += "|";
			}
			printString += p;
		});
		console.log(printString);
	}
};

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
		case "if":
			returnVal = ExecuteIf(node);
			break;
		default:
			console.log(`${node.type} is an invalid node type --execution`);
	}
	return returnVal;
}

DefineFunction = function DefineFunction(node) {
	functions[node.name] = {params: node.params, body: node.body};
}

ExecuteFunction = function ExecuteFunction(node) {
	const params = ExecuteParams(node.params);
	const functionBody = functions[node.name];
	return functionBody(params);
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

ExecuteIf = function ExecuteIf(node) {
	const evaluation = ExecuteNode(node.evaluation);
	if (evaluation) {
		return node.statements.map(statement => ExecuteNode(statement));
	} else {
		return node.elseStatements.map(statement => ExecuteNode(statement));
	}
}