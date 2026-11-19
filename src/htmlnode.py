class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag        = tag
        self.value      = value
        self.children   = children
        self.props      = props

    def to_html(self):
        raise NotImplementedError(".to_html() not implemented")

    def props_to_html(self):
        if not self.props:
            return ""

        props_str = ""
        for k, v in self.props.items():
            props_str += f' {k}="{v}"'

        return props_str
        
    def __repr__(self):
        first  = "HTMLNode(\n"
        second = f"\ttag:      {self.tag}\n"
        third  = f"\tvalue:    {self.value}\n"
        fourth = f"\tchildren: {self.children}\n"
        fifth  = f"\t{self.props_to_html()})"
        return first + second + third + fourth + fifth


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
        self.tag    = tag
        self.value  = value
        self.props  = props

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")

        if not self.tag:
            return self.value

        if isinstance(self.value, dict):
            raise ValueError("Passed props to value parameter in LeafNode.to_html(tag, value, props)")

        props_string  = self.props_to_html() if self.props else ""
        tag_string    = f"<{self.tag}{props_string}>"
        value_string  = f"{self.value}"
        ending_string = f"</{self.tag}>"

        return tag_string + value_string + ending_string

    def __repr__(self):
        self_str  = "HTMLNode(\n"
        tag_str   = f"\ttag:      {self.tag}\n"
        value_str = f"\tvalue:    {self.value}\n"
        props_str = f"\t{self.props_to_html()})"
        return self_str + tag_str + value_str + props_str
        

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag parameter")

        if not self.children:
            raise ValueError("Missing chidren parameter")
        
        child_results = ""
        for child in self.children:
            child_results += child.to_html()
        
        props_str = self.props_to_html() if self.props else ""
        wrapper = f"<{self.tag}{props_str}>{child_results}</{self.tag}>"
                
        return wrapper
