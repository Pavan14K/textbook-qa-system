import re

def identify_structure(text):
    chapters = re.split(r'\nChapter \d+\n', text)
    structure = {}
    
    for i, chapter in enumerate(chapters):
        if i == 0:
            continue
        sections = re.split(r'\nSection \d+\n', chapter)
        chapter_title = sections.pop(0).strip()
        structure[chapter_title] = {}
        
        for section in sections:
            subsections - re.split(r'\nSubsection \d+\.\d+\.\d+\n', section)
            section_title = subsections.pop(0).strip()
            structure[chapter_title][section_title] = subsections
            
    return structure

def validate_structure(structure):
    for chapter_title, sections in structure.items():
        if not chapter_title:
            return False, "Invalid chapter title"
        
        
        for section_title, subsections in sections.items():
            if not section_title:
                return False, "Invalid section title"
        
        for subsection in subsections:
            if not subsection.strip():
                return False, "Invalid subsection title"
            
    return True, "Structure is valid"

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    
    with open(input_path, 'r') as f:
        text = f.read()
        
    
    structure = identify_structure(text)
    is_valid, message = validate_structure(structure)
    print(message)
    
    
    if is_valid:
        import pickle
        with open(output_path, 'wb') as f:
            pickle.dump(structure, f)
            