# AST node creation
# kwargs (keyword arguments) are the attributes of the node
def create_node(node_type, **kwargs):
    node = {"node_type": node_type}
    for key, value in kwargs.items(): # add each key-value pair to the node
        node[key] = value 
    return node # return the node