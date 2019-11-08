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
	this.fndef = definition;
	this.parent = null;
	this.children = {};
	this.type = "function";

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

exports.ParamsNode = function ParamsNode(paramsArr) {
	this.children = paramsArr;
	this.parent = null;
	this.type = "params";

	this.setParent = function(node) { this.parent = node; }
	this.getParent = function() { return this.parent; }

	this.executeParams = function() {
		return this.children.map(param => {
			if (param.type === "value") {
				return param.getValue();
			}
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