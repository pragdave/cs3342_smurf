treeNodes = require("./treeNodes");
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
			newNode.setParams(paramsNode);
			newNode.setBody(body);
			break;
		case "integer":
			newNode = new treeNodes.ValueNode(statement.value);
			break;
		case "arithmetic_expr":
			const operator = statement.params[1];
			newNode = new treeNodes.ArithmeticExprNode(operator);
			let leftParams = statement.params[0];
			if (!leftParams.type && leftParams.length > 1) {
				leftParams = leftParams[1];
			}
			const leftSide = generateNode(leftParams);
			newNode.setLeftSide(leftSide);
			let rightParams = statement.params[2];
			if (!rightParams.type && rightParams.length > 1) {
				rightParams = rightParams[1];
			}
			const rightSide = generateNode(rightParams);
			newNode.setRightSide(rightSide);
			break;
		default: 
			console.log(`${statement.type} is an invalid statement type`);
	}
	return newNode;
}

function generateASTNodes(ast) {
	return ast.map(statement => generateNode(statement));
}

function executeNode(node) {
	switch(node.type) {
		case "function":
			node.executeBody();
			break;
		default:
			console.log(`${node.type} is an invalid node type`);
	}
}

function executeAST(ast) {
	ast.forEach(node => executeNode(node));
}

const codeExample = 

`print(1)          \n` +
`print(3 - 1)      \n` +
`print(2+1)        \n` +
`print(2 * 5 - 3*2)\n` +
`print(4 - -1)     \n` +
`print(5--1)       \n` +
`print(21/3)       \n` +
`print((3-1)*(3+1))`;


// const codeExample = `let a = 99\n
//   		let f = fn(x) { x + a }\n
//   		print(f(1))     #=> 100\n
//   		a = 100\n
//   		print(f(1))     #=> 101\n`;

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
	const astArr = generateASTNodes(ast);
	executeAST(astArr)
});

// run w/ node main.js