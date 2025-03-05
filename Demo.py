import matplotlib.pyplot as plt
import networkx as nx
import time
from IPython.display import display, clear_output

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


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

def draw_tree(root):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)
    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', edge_color='gray')
    plt.show()

def animate_bst(operations):
    root = None
    for op, key in operations:
        if op == 'insert':
            root = insert(root, key)
        elif op == 'delete':
            root = deleteNode(root, key)
        clear_output(wait=True)
        draw_tree(root)
        time.sleep(1)

operations = [('insert', 50), ('insert', 30), ('insert', 70), ('insert', 20), ('insert', 40),
              ('insert', 60), ('insert', 80)]
animate_bst(operations)
