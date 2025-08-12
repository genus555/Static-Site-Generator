from LeafNode import *
from parentnode import *
from textnode import *
from splitter import text_to_textnodes

from block import *   

def hashtags(block):
    hashtag = 0
    check = True
    while check:
        if block[hashtag] == '#':
            hashtag += 1
        else:
            check = False
    return hashtag
    
def blockType_to_markdownType(blockType, block):
    if blockType == BlockType.heading:
        hashtag = hashtags(block)
        return f"h{hashtag}"
    elif blockType == BlockType.quote:
        return "blockquote"
    elif blockType == BlockType.unordered_list:
        return "ul"
    elif blockType == BlockType.ordered_list:
        return "ol"
    elif blockType == BlockType.code:
        return "pre"
    else:
        return 'p' 

def create_child_nodes(block):
    children = []
    list_items = block.split("\n")

    for item in list_items:
        temp_item = item[2:]
        temp_item = temp_item.strip()
        textNodes = text_to_textnodes(temp_item)
        item_children = []
        for textnode in textNodes:
            item_child = text_node_to_html_node(textnode)
            item_children.append(item_child)
        node = ParentNode('li', item_children)
        children.append(node)
    return children

def create_code_node(text):
    new_text = text[4:-3]
    return LeafNode('code', new_text)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    allNodes = []

    for block in blocks:
        blockType = block_to_block_type(block)
        markdownType = blockType_to_markdownType(blockType, block)
        if markdownType == 'p':
            block = block.replace('\n', ' ')
        
        if markdownType == 'pre':
            node = create_code_node(block)
            parentNode = ParentNode(markdownType, [node])
            allNodes.append(parentNode)
        elif markdownType in ['ul', 'ol']:
            children = create_child_nodes(block)
            node = ParentNode(markdownType, children)
            allNodes.append(node)
        else:
            if markdownType.startswith('h'):
                hastag = hashtags(block)
                clean_block = block[hastag:].strip()
            elif markdownType == "blockquote":
                lines = block.split('\n')
                clean_lines = []
                for line in lines:
                    if line.startswith('> '):
                        clean_lines.append(line[2:])
                    elif line.startswith('>'):
                        clean_lines.append(line[1:])
                    else:
                        clean_lines.append(line)
                clean_block = '\n'.join(clean_lines)
            else:
                clean_block = block
            textNodes = text_to_textnodes(clean_block)
            htmlNodes = []

            for node in textNodes:
                leafNode = text_node_to_html_node(node)
                htmlNodes.append(leafNode)
        
            node = ParentNode(markdownType, htmlNodes)
            allNodes.append(node)
    
    final_node = ParentNode('div', allNodes)
    return final_node
