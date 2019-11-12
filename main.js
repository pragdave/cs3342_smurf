treeNodes = require("./treeNodes");
fs = require("file-system");
peg = require("pegjs");

function printFunction(valArr) { console.log(valArr[0]); }

function generateNode(statement) {
	if (statement.type === "function") {
		const body = statement.fcn_name === "print" ? printFunction : statement.body;
			// TODO: generateNode for statement.body
		const newNode = new treeNodes.FunctionNode(statement.fcn_name);
		const params = statement.params.map(p => generateNode(p)).filter(p => !!p);
		const paramsNode = new treeNodes.ParamsNode(params);
		newNode.setParams(paramsNode);
		newNode.setBody(body);
		return newNode;
	} else if (statement.type === "integer") {
		const newNode = new treeNodes.ValueNode(statement.value);
		return newNode;
	}
}

function generateASTNodes(ast) {
	return ast.map(statement => generateNode(statement));
}

function executeNode(astNode) {
	if (astNode.type === "function") {
		astNode.executeBody();
	}
}

function executeAST(ast) {
	ast.forEach(node => executeNode(node));
}

const codeExample = `print(1)\n` +
					`print(2)`;

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