fs = require("file-system");
peg = require("pegjs");

fs.readFile("grammar.txt", "utf8", function (err, data) {
	if (err) {
		throw err;
		return;
	}
	
	const grammar = data;
	const parser = peg.generate(grammar);
})

// run w/	node main.js