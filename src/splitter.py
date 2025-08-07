from textnode import TextNode, TextType
from extractlink import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            old_message = node.text
            for image in images:
                left_over = old_message.split(f"![{image[0]}]({image[1]})", 1)
                new_nodes.append(TextNode(left_over[0], TextType.text))
                new_nodes.append(TextNode(image[0], TextType.image, image[1]))
                old_message = left_over[1]
            new_nodes.append(TextNode(old_message, TextType.text))
    
    for i in range(len(new_nodes)):
        if new_nodes[i].text == '':
            new_nodes.pop(i)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            old_message = node.text
            for link in links:
                left_over = old_message.split(f"[{link[0]}]({link[1]})", 1)
                new_nodes.append(TextNode(left_over[0], TextType.text))
                new_nodes.append(TextNode(link[0], TextType.link, link[1]))
                old_message = left_over[1]
            new_nodes.append(TextNode(old_message, TextType.text))
    
    for i in range(len(new_nodes)):
        if new_nodes[i].text == '':
            new_nodes.pop(i)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.text)]
    nodes = split_nodes_delimiter(nodes, "_", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
