from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT   = "plain"
    BOLD    = "bold"
    ITALIC  = "italic"
    CODE    = "code"
    LINK    = "link"
    IMG     = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text       = text
        self.text_type  = text_type
        self.url        = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b",value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i",value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code",value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        case TextType.IMG:
            return LeafNode(tag="img",value="",props={"src":text_node.url,"alt":text_node.text})
        case _:
            raise ValueError("not a valid text_type")

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    text_type = TextType.TEXT
    match delimiter:
        case "**":
            text_type = TextType.BOLD
        case "`":
            text_type = TextType.CODE
        case "_":
            text_type = TextType.ITALIC
        case _:
            raise ValueError("unsupported delimiter")
    
    return_nodes = []
    for node in old_nodes:
        split_text = [txt for txt in node.text.split(delimiter) if txt != ""]
        delimiter_count = node.text.count(delimiter)
    
    ## this doesn't handle for multiple iterations of the delimiter. One instance yields three items, two instances yields four items, three instances

    return return_nodes
