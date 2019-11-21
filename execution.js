exports.ExecuteStatement = function ExecuteStatement(node) {
	return ExecuteNode(node);
}

variables = {
	print: {
		execute: (paramsArr) => {
			let printString = "";
			paramsArr.forEach((p,i) => {
				if (i !== 0) {
					printString += "|";
				}
				printString += p;
			});
			console.log(printString);
		}
	}
};

functionVariables = {};

ExecuteNode = function ExecuteNode(node) {
	let returnVal = null;
	switch(node.type) {
		case "function_call":
			returnVal = ExecuteFunctionCall(node);
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
		case "boolean_expr":
			returnVal = ExecuteBooleanExpr(node);
			break;
		case "function_def":
			returnVal = ExecuteFunctionDef(node);
			break;
		default:
			console.log(`\n******\t${node.type} is an invalid node type --execution\t******\n`);
	}
	return returnVal;
}

ExecuteFunctionDef = function ExecuteFunctionDef(node) {
	const parentNode = node.parent;
	const functionName = parentNode.name;
	const functionNode = new ExecuteFunction(node.body);
	node.params.params.forEach(p => {
		functionNode.params[p.name] = null;
		functionNode.paramsOrder.push(p.name);
	})
	variables[functionName] = functionNode;
	return variables[functionName];
}

ExecuteFunction = function ExecuteFunction(body) {
	this.params = {};
	this.paramsOrder = [];
	this.body = body;

	this.execute = function(localParams) {
		localParams.forEach((p,i) => {
			const paramName = this.paramsOrder[i];
			variables[paramName] = p;
		})
		const executed = this.body.map(statement => ExecuteNode(statement));
		return executed[executed.length - 1]
	}
}

ExecuteFunctionCall = function ExecuteFunctionCall(node) {
	const params = ExecuteParams(node.params);
	const functionBody = node.name.type ? ExecuteNode(node.name) : variables[node.name];
	return functionBody.execute(params);
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

ExecuteBooleanExpr = function ExecuteBooleanExpr(node) {
	let evaluation = null;
	let leftSide = node.leftSide;
	let rightSide = node.rightSide;
	if (leftSide.type) {
		leftSide = ExecuteNode(leftSide);
	}
	if (rightSide.type) {
		rightSide = ExecuteNode(rightSide);
	}
	switch(node.operator) {
		case "==":
			value = leftSide === rightSide;
			break;
		case "!=":
			value = leftSide !== rightSide;
			break;
		case ">=":
			value = leftSide >= rightSide;
			break;
		case ">":
			value = leftSide > rightSide;
			break;
		case "<=":
			value = leftSide <= rightSide;
			break;
		case "<":
			value = leftSide < rightSide;
			break;
		default:
			console.log(`${this.operator} is an invalid operator --execution`);
	}
	return value;
}

ExecuteParams = function ExecuteParams(node) {
	arr = node.params.map(param => {
		return ExecuteNode(param);
	})
	return arr;
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