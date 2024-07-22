import pickle
from anytree import Node, RenderTree

def traverse_tree(root):
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

if __name__ == "__main__":
    import sys
    index_path = sys.argv[1]
    
    with open(index_path, 'rb') as f:
        root = pickle.load(f)
    
    traverse_tree(root)
