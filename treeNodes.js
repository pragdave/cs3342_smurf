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

exports.FunctionNode = function FunctionNode(definition, params, body) {
	this.fndef = definition;
	this.parent = null;
	this.children = {params, body}

	this.setParent = function(node) {
		this.parent = node;
	}
	this.getParent = function() {
		return this.parent;
	}

	this.getParams = function() {
		return this.children.params;
	}
	this.getBody = function() {
		return this.children.body;
	}

	this.executeBody = function() {
		return this.children.body(this.children.params)
	}
}