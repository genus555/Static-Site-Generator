class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            raise Exception("No Props")
        rtn_str = ""
        for prop in self.props:
            rtn_str = f"{rtn_str} {prop}=\"{self.props[prop]}\""
        return rtn_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def text_node_to_html_node(text_node):
        raise NotImplementedError
