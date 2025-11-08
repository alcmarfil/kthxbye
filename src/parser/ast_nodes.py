# AST node creation
# kwargs are the attributes of the node
def create_node(node_type, **kwargs):
    node = {"node_type": node_type}
    for key, value in kwargs.items():
        node[key] = value
    return node