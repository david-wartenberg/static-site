from htmlnode import HTMLNode

node = HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
})

if __name__ == "__main__":
    print(node)
