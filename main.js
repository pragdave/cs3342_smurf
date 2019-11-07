fs = require("file-system");
peg = require("pegjs");

const codeExample = `let a = 99\n
  		let f = fn(x) { x + a }\n
  		print(f(1))     #=> 100\n
  		a = 100\n
  		print(f(1))     #=> 101\n`;

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
})

// run w/	node main.js