from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None or self.value == "":
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
