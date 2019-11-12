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
			const leftSide = generateNode(statement.params[0]);
			newNode.setLeftSide(leftSide);
			const rightSide = generateNode(statement.params[2]);
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
		case "arithmetic_expr":
			node.executeExpr();
			break;
		default:
			console.log(`${node.type} is an invalid node type`);
	}
}

function executeAST(ast) {
	ast.forEach(node => executeNode(node));
}

const codeExample = `print(1 - 2)`;

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
	fs.writeFile("ast.txt", JSON.stringify(ast, null, "\t"), function(err) {
		if (err) {console.log(err);}
	})
	const astArr = generateASTNodes(ast);
	executeAST(astArr)
});

// run w/ node main.js