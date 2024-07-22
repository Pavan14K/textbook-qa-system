import pickle
from anytree import Node, RenderTree

def create_nodes(structure):
    root = Node("Textbook Title")
    
    for chapter_title, sections in structure.items():
        chapter_node = Node(chapter_title, parent=root)
        
        for section_title, subsections in sections.items():
            section_node = Node(section_title, parent=chapter_node)
            
            for i, subsection in enumerate(subsections):
                Node(f"Subsection {i+1}", parent=section_node, content=subsection)
    
    return root

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    with open(input_path, 'rb') as f:
        structure = pickle.load(f)
        
    root = create_nodes(structure)
    
    with open(output_path, 'wb') as f:
        pickle.dump(root, f)
    
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")
