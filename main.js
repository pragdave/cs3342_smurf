treeNodes = require("./treeNodes");
execution = require("./execution");
fs = require("file-system");
peg = require("pegjs");

// const codeExample = 
// "print(1)            #=> 1\n" +
// "print(3 - 1)        #=> 2\n" +
// "print(2+1)          #=> 3\n" +
// "print(2 * 5 - 3*2)  #=> 4\n" +
// "print(4 - -1)       #=> 5\n" +
// "print(5--1)         #=> 6\n" +
// "print(21/3)         #=> 7\n" +
// "print((3-1)*(3+1))  #=> 8\n";

// const codeExample =
// `let a = 3\n
// let b = 4\n\n
// print(b-a)          #=> 1\n
// print(a-1)          #=> 2\n
// print(2+b/a)        #=> 3\n
// print(b)            #=> 4\n\n
// a = a + b\n
// b = b-a\n\n
// print(a)            #=> 7\n
// print(b)            #=> -3\n\n
// let c = a\n
// a = b\n
// b = c\n\n
// print(a)            #=> -3\n
// print(b)            #=> 7\n`;

// const codeExample = 
// `let a = 1\n
// print(a)          #=> 1\n
// let b = a+2\n
// print(b)          #=> 3\n
// let c = a+b\n
// print(c)          #=> 4\n\n
// # multiple declarations in a single let\n\n
// let e = 99, f = 100, g = e+f\n
// print(e,f,g)   #=> 99|100|199\n\n
// # on multiple lines\n\n
// let h = 99,\n
//     i = 200,\n
//     j = h+i\n
// print(h,i,j)   #=> 99|200|299\n`;

// const codeExample = 
// `if 1 {\n
//   print(99)\n
// }\n
// else {\n
//   print(100)\n
// }                                        #=> 99\n
// # 'if' as an expression\n
// print(if 1 { 99 } else { 100 })          #=> 99\n
// print(if 0 { 99 } else { 100 })          #=> 100\n\n
// # try relops\n\n
// print(if 9 < 10 { 1  } else { -1 })      #=> 1\n
// print(if 10 < 9 { -1 } else {  1 })      #=> 1\n
// print(if 9 < 9  { -1 } else {  1 })      #=> 1\n
// print(if  9 <= 10 {  1 } else { -1 })    #=> 1\n
// print(if 10 <=  9 { -1 } else {  1 })    #=> 1\n
// print(if  9 <=  9 {  1 } else { -1 })    #=> 1\n\n
// print(if  9 >= 10 { -1 } else {  1 })    #=> 1\n
// print(if 10 >=  9 {  1 } else { -1 })    #=> 1\n
// print(if  9 >=  9 {  1 } else { -1 })    #=> 1\n\n
// print(if  9 > 10 { -1 } else {  1 })     #=> 1\n
// print(if 10 >  9 {  1 } else { -1 })     #=> 1\n
// print(if  9 >  9 { -1 } else {  1 })     #=> 1\n\n
// print(if  9 ==  9 {  1 } else { -1 })    #=> 1\n
// print(if  9 == 10 { -1 } else {  1 })    #=> 1\n
// print(if  9 !=  9 { -1 } else {  1 })    #=> 1\n
// print(if  9 != 10 {  1 } else { -1 })    #=> 1\n
// `;

const codeExample = 
`# no parameters\n\n
let f = fn () { 99 }\n
print(f())             #=> 99\n\n
`;

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
	const rootNode = treeNodes.GenerateAST(ast);
	rootNode.statements.forEach(s => execution.ExecuteStatement(s));
});

// run w/ node main.js