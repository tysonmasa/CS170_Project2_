import random

class Node:
    def __init__(self, state, size, parent_node, depth):
        self.state = state # showing the feature combination, would be something like (3,4)
        self.size = size # number features in the combination
        self.parent = parent_node # showing its parent node
        self.depth = depth # showing the depth of this node

def create_node(state, parent_node, depth):
    return Node(state, parent_node, depth)

def eval_function():
    return random.randrange(1,100)

def foward_selection(features):
    current_node = Node(init, '', 0, None, 0)
    explored = []
    frontier = []
    best = current_node
    while (current_node.size != features):
        continue
    pass

def backward_elimination():
    pass

def main():
    print(eval_function)