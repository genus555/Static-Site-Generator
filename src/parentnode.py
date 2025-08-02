from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag")
        elif not self.children:
            raise ValueError("No Children")
        rtn_str = f"<{self.tag}>"
        for child in self.children:
            rtn_str = f"{rtn_str}{child.to_html()}"
        rtn_str = f"{rtn_str}</{self.tag}>"
        return rtn_str