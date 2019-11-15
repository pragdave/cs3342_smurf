treeNodes = require("./treeNodes");
execution = require("./execution");
fs = require("file-system");
peg = require("pegjs");

function printFunction(valArr) { console.log(valArr[0]); }

function generateNode(statement) {
	if (!statement.type) {
		return {};
	}

	let newNode = {};
	switch(statement.type) {
		case "function":
			const body = statement.fcn_name === "print" ? printFunction : statement.body;
				// TODO: generateNode for statement.body
			newNode = new treeNodes.FunctionNode(statement.fcn_name);
			const params = statement.params.map(p => generateNode(p)).filter(p => !!p && !!p.type);
			const paramsNode = new treeNodes.ParamsNode(params);
			newNode.params = paramsNode;
			paramsNode.parent = newNode;
			newNode.body = body;
			// body.parent = newNode;
			break;
		case "integer":
			newNode = new treeNodes.ValueNode(statement.value);
			break;
		case "identifier":
			newNode = new treeNodes.IdentifierNode(statement.name);
			break;
		case "arithmetic_expr":
			const operator = statement.params[1];
			newNode = new treeNodes.ArithmeticExprNode(operator);
			let leftParams = statement.params[0];
			if (!leftParams.type && leftParams.length > 1) {
				leftParams = leftParams[1];
			}
			const leftSide = generateNode(leftParams);
			newNode.leftSide = leftSide;
			leftSide.parent = newNode;
			let rightParams = statement.params[2];
			if (!rightParams.type && rightParams.length > 1) {
				rightParams = rightParams[1];
			}
			const rightSide = generateNode(rightParams);
			newNode.rightSide = rightSide;
			rightSide.parent = newNode;
			break;
		case "variable_dec":
			newNode = new treeNodes.VariableDecNode();
			statement.declarations.forEach(d => {
				const decNode = generateNode(d);
				newNode.declarations.push(decNode);
				decNode.parent = newNode;
			});
			break;
		case "assignment":
			newNode = new treeNodes.AssignmentNode(statement.name);
			const exprNode = generateNode(statement.expr);
			newNode.expr = exprNode;
			exprNode.parent = newNode;
			break;
		default: 
			console.log(`${statement.type} is an invalid statement type`);
	}
	return newNode;
}

function generateASTNodes(ast) {
	const rootNode = new treeNodes.RootNode();
	nodes = ast.map(statement => generateNode(statement));
	rootNode.addStatements(nodes);
	return rootNode;
}

function executeAST(rootNode) {
	rootNode.statements.forEach(s => execution.ExecuteStatement(s));
}

// const codeExample = "let a = 1\nprint(1)";
const codeExample =
`print(1)          \n` +
`print(3 - 1)      \n` +
`print(2+1)        \n` +
`print(2 * 5 - 3*2)\n` +
`print(4 - -1)     \n` +
`print(5--1)       \n` +
`print(21/3)       \n` +
`print((3-1)*(3+1))`;



fs.readFile("grammar.txt", "utf8", function (err, data) {
	if (err) {
		throw err;
		return;
	}

	const grammar = data;
	const parser = peg.generate(grammar);
	const ast = parser.parse(codeExample);
	fs.writeFile("ast.json", JSON.stringify(ast, null, "\t"), function(err) {
		if (err) { console.log(err); }
	})
	const rootNode = generateASTNodes(ast);
	executeAST(rootNode)
});

// run w/ node main.js