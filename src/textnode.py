from enum import Enum

class TextType(Enum):
    text = "text(plain)"
    italic = "_Italic text_"
    code = "`Code text`"
    links = "[anchor text](url)"
    images = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_node):
        return self == other_node
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"