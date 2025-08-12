from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All Leaf nodes must have a value")
        if self.tag == None:
            return self.value
        
        if self.tag == 'img':
            return f"<{self.tag}{super().props_to_html()} />"
        elif self.props != None:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
def text_node_to_html_node(text_node):
    tag = None
    props = None
    value = None
    if text_node.text_type == TextType.text:
        tag = None
    elif text_node.text_type == TextType.bold:
        tag = 'b'
    elif text_node.text_type == TextType.italic:
        tag = 'i'
    elif text_node.text_type == TextType.code:
        tag = 'code'
    elif text_node.text_type == TextType.link:
        tag = 'a'
        props = {"href":text_node.url}
    elif text_node.text_type == TextType.image:
        tag = 'img'
        props = {"src":text_node.url, "alt":text_node.text}
    
    if text_node.text_type != TextType.image:
        value = text_node.text
    else:
        value = ''

    #print(f"DEBUG: Creating LeafNode - tag: {tag}, value: '{value}', props: {props}")
    return LeafNode(tag, value, props)
