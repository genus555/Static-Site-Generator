from enum import Enum

def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    blocks = []

    for split in splits:
        if split != '':
            blocks.append(split.strip())

    return blocks

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def block_to_block_type(block):
    #headings check
    check = True
    heading = False
    i = 0
    if block[i] == '#':
        heading = True
    else:
        check = False
    while check:
        if block[i] == '#':
            i += 1
        else:
            if i > 5 or block[i] != ' ':
                heading = False
            check = False
    
    #list check
    List = False
    if "\n" in block:
        List = True
    
    if heading:
        return BlockType.heading
    elif block[-3:] == "```" and block[:3] == "```":
        return BlockType.code
    elif block[0] == ">":
        return BlockType.quote
    elif List:
        list_items = block.split("\n")
        items = []
        unordered = True
        ordered = True
        i = 1
        for item in list_items:
            start = item[:3]
            items.append(start)
        
        for item in items:
            if item[:2] != "- ":
                unordered = False
            if item == f"{i}. ":
                i += 1
            else:
                ordered = False
        
        if unordered:
            return BlockType.unordered_list
        elif ordered:
            return BlockType.ordered_list
        return BlockType.paragraph
    
    else:
        return BlockType.paragraph
    