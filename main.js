treeNodes = require("./treeNodes");
fs = require("file-system");
peg = require("pegjs");

function printFunction(valArr) { console.log(valArr[0]); }

function generateASTNodes(statement) {
	// iterate through generated ast and create AST nodes
	// ast.forEach(statement => {
	if (statement.type === "function") {
		const body = statement.fcn_name === "print" ? printFunction : statement.body;
			// TODO: generateASTNodes for statement.body
		const newNode = new treeNodes.FunctionNode(statement.fcn_name);
		const params = statement.params.map(p => generateASTNodes(p)).filter(p => !!p);
		const paramsNode = new treeNodes.ParamsNode(params);
		newNode.setParams(paramsNode);
		newNode.setBody(body);
		return newNode;
	} else if (statement.type === "integer") {
		const newNode = new treeNodes.ValueNode(statement.value);
		return newNode;
	}
	// })
}

function executeAST(astNode) {
	if (astNode.type === "function") {
		astNode.executeBody();
	}
}

const codeExample = "print(1)";
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
	fs.writeFile("ast.txt", JSON.stringify(ast), function(err) {
		if (err) {console.log(err);}
	})
	const newAST = generateASTNodes(ast[0]);
	executeAST(newAST);
});

// run w/	node main.js