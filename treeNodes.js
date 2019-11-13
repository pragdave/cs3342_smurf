// Reference = https://stackoverflow.com/questions/12036966/generic-tree-implementation-in-javascript
exports.TreeNode = function TreeNode(value) {
	this.value = value;
	this.parent = null;
	this.children = [];

	this.setParent = function(node) {
		this.parent = node;
	}
	this.getParent = function() {
		return this.parent;
	}

	this.addChild = function(node) {
		node.setParent(this);
		this.children[this.children.length] = node;
	}
	this.getChildren = function() {
		return this.children;
	}
	this.removeChildren = function() {
		this.children = [];
	}
}

exports.FunctionNode = function FunctionNode(definition) {
	this.type = "function";
	this.fndef = definition;
	this.parent = null;
	this.children = { params: null, body: null };

	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.setParams = function(node) {
		node.setParent(this);
		this.children.params = node;
	}
	this.getParams = function() {
		return this.children.params;
	}

	this.setBody = function(body) {
		// body.setParent(this);
		this.children.body = body;
	}
	this.getBody = function() {
		return this.children.body;
	}

	this.executeBody = function() {
		const result = this.children.params.executeParams();
		return this.children.body(result)
	}
}

exports.ArithmeticExprNode = function ArithmeticExprNode(operator) {
	this.type = "arithmetic_expr";
	this.parent = null;
	this.children = { leftSide: null, rightSide: null };
	this.operator = operator;

	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.setLeftSide = function(node) {
		node.setParent(this);
		this.children.leftSide = node;
	}
	this.setRightSide = function(node) {
		node.setParent(this);
		this.children.rightSide = node;
	}

	this.executeExpr = function() {
		let value = 0;
		let finalLeftSide = this.children.leftSide;
		let finalRightSide = this.children.rightSide;
		if (finalLeftSide.type === "arithmetic_expr") {
			finalLeftSide = this.children.leftSide.executeExpr();
		}
		if (finalRightSide.type === "arithmetic_expr") {
			finalRightSide = this.children.rightSide.executeExpr();
		}
		switch(this.operator) {
			case "+":
				value = finalLeftSide.getValue() + finalRightSide.getValue();
				break;
			case "-":
				value = finalLeftSide.getValue() - finalRightSide.getValue();
				break;
			case "*":
				value = finalLeftSide.getValue() * finalRightSide.getValue();
				break;
			case "/":
				value = finalLeftSide.getValue() / finalRightSide.getValue();
				break;
			default:
				console.log(`${this.operator} is an invalid operator`);
				value = 0;
		}
		const resultNode = new exports.ValueNode(value);
		return resultNode;
	}
	
}

exports.VariableDecNode = function VariableDecNode() {
	this.type = "variable_dec";
	this.parent = null;
	this.declarations = null;

	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.setDeclarations = function(decArr) {
		decArr.forEach(node => node.setParent(this));
		this.declarations = decArr;
	}
}

exports.AssignmentNode = function AssignmentNode(name) {
	this.type = "variable";
	this.parent = null;
	this.children = { name: name, expr: null };

	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.setExpr = function(node) {
		node.setParent(this);
		this.children.expr = node;
	}
}

exports.ParamsNode = function ParamsNode(paramsArr) {
	this.type = "params";
	this.parent = null;
	this.children = paramsArr;
	
	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.executeParams = function() {
		return this.children.map(param => {
			let returnVal = null;
			switch(param.type) {
				case "value":
					returnVal = param.getValue();
					break;
				case "arithmetic_expr":
					const returnNode = param.executeExpr();
					returnVal = returnNode.getValue();
					break;
				default:
					console.log(`${param.type} is an invalid param type`)
			}
			return returnVal;
		})
	}
}

exports.ValueNode = function ValueNode(value) {
	this.value = value;
	this.parent = null;
	this.type = "value";

	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.getValue = function() { return this.value; }
}