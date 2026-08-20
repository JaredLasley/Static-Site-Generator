class HTMLNode:
    def __init__(self,tag:str|None=None,value=None,children:list|None =None,props:dict|None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        rtn_str = f''
        for key in self.props:
            rtn_str = f'{rtn_str} {key}="{self.props[key]}"'
        return rtn_str

    def __repr__(self):
        return f"HTMLNode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"
    
    def __eq__(self,other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None) -> None:
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNode(tag = {self.tag}, value = {self.value}, props = {self.props})"


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        full_tag = ""
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("This node has no children")
        for child in self.children:
            full_tag =  f"{full_tag}{child.to_html()}"
        return f"<{self.tag}>{full_tag}</{self.tag}>"