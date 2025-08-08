"""def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip("\n")
        if blocks[i] == '':
            blocks.pop(i)
    
    return blocks
"""
def markdown_to_blocks(markdown):
    splits = markdown.split("\n\n")
    blocks = []

    for split in splits:
        if split != '':
            blocks.append(split.strip())

    return blocks