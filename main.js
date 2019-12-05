treeNodes = require("./treeNodes");
execution = require("./execution");
fs = require("file-system");
peg = require("pegjs");

fs.readFile("grammar.txt", "utf8", function (err, data) {
	if (err) {
		throw err;
		return;
	}

	const grammar = data;
	const parser = peg.generate(grammar);
	const fileName = process.argv[2];
	fs.readFile(fileName, "utf8", function (err2, data2) {
		if (err2) {
			throw err2;
			return;
		}
		console.log("hello")
		const code = data2;
		const ast = parser.parse(code);
		fs.writeFile("ast.json", JSON.stringify(ast, null, "\t"), function(err) {
			if (err) { console.log(err); }
		})
		const rootNode = treeNodes.GenerateAST(ast);
		rootNode.statements.forEach(s => execution.ExecuteStatement(s));
	})
});