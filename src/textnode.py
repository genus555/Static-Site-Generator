from enum import Enum

class TextType(Enum):
    text = "text(plain)"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"
    bold = "bold"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_node):
        same = True
        if self.text != other_node.text:
            same = False
        if self.text_type != other_node.text_type:
            same = False
        if self.url != other_node.url:
            same = False
        return same
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"