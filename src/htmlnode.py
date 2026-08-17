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