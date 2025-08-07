from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
        else:
            old_message = node.text
            old_message = old_message.split(delimiter)
            if len(old_message)%2 == 0:
                raise Exception("No closing delimiter found. Invalid markdown syntax")
            for i in range (len(old_message)):
                if old_message[i] != '':
                    if i == 0 or (i%2) == 0:
                        new_nodes.append(TextNode(old_message[i], node.text_type))
                    else:
                        new_nodes.append(TextNode(old_message[i], text_type))
    return new_nodes
