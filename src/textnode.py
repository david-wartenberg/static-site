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
    new_nodes = []
    
    match delimiter:
        case "**":
            node_text_type = TextType.BOLD
        case "`":
            node_text_type = TextType.CODE
        case "_":
            node_text_type = TextType.ITALIC
        case _:
            raise ValueError("unsupported delimiter")

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        tagged_text = []
        splits = node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise ValueError("invalid markdown syntax")

        d_idx = [1 if i % 2 == 1 else 0 for i in range(len(splits))]
        tagged_text.extend(tuple(zip(d_idx, splits)))
    
    
        for i, v in tagged_text:
            if v == "":
                continue

            t_type = TextType.TEXT
            if i == 1:
                t_type = text_type

            new_nodes.append(TextNode(v, t_type))
    ## this doesn't handle for multiple iterations of the delimiter. One instance yields three items, two instances yields four items, three instances
    
    return new_nodes


if __name__ == "__main__":
    node = TextNode("this text has both **bold** and _italic_ elements", TextType.TEXT)
    print(node)
    new_node = split_nodes_delimiter([node], "**", TextType.TEXT)
    print(new_node)
    new_node = split_nodes_delimiter(new_node, "_", TextType.BOLD)
    print(new_node)
