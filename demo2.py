import matplotlib.pyplot as plt
import networkx as nx
import time
from IPython.display import display, clear_output

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def new_node(key):
    return Node(key)

def right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def splay(root, key):
    if root is None:
        return new_node(key)
    if root.key == key:
        return root

    if root.key > key:
        if root.left is None:
            return root
        if root.left.key > key:  
            root.left.left = splay(root.left.left, key)
            root = right_rotate(root)
        elif root.left.key < key: 
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = left_rotate(root.left)
        return right_rotate(root)
    else:
        if root.right is None:
            return root
        if root.right.key > key: 
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root.right = right_rotate(root.right)
        elif root.right.key < key:  
            root.right.right = splay(root.right.right, key)
            root = left_rotate(root)
        return left_rotate(root)

def insert(root, key):
    if root is None:
        return new_node(key)
    root = splay(root, key)
    if root.key == key:
        return root
    node = new_node(key)
    if root.key > key:
        node.right = root
        node.left = root.left
        root.left = None
    else:
        node.left = root
        node.right = root.right
        root.right = None
    return node



'''

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Everything below is just animation

'''





def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        pos[node.key] = (x, -y)
        if node.left:
            graph.add_edge(node.key, node.left.key)
            add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y + 1, layer + 1)
        if node.right:
            graph.add_edge(node.key, node.right.key)
            add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y + 1, layer + 1)

def visualize_step(root, operation):
    clear_output(wait=True)
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)
    plt.figure(figsize=(8, 5))
    plt.title(f"{operation}")
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', edge_color='gray')
    plt.show()
    time.sleep(1)

def animate_splay_tree():
    test_cases = [
        ("Zig", [10, 20]),
        ("Zig", [20, 10]),
        
    ]
    
    for operation, keys in test_cases:
        root = None  
        for key in keys:
            root = insert(root, key) 
        root = splay(root, keys[-1]) 
        visualize_step(root, operation)  

animate_splay_tree()

