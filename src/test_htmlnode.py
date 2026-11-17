import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node  = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(print(node), print(node2))

    def test_noteq(self):
        node  = HTMLNode("p")
        node2 = HTMLNode("h")
        self.assertNotEqual(node.tag, node2.tag)

    def test_props_to_html(self):
        node  = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), f' href="https://www.google.com" target="_blank"')

    def test_noprops(self):
        node  = HTMLNode()
        self.assertEqual(node.props, None)

if __name__ == "__main__":
    unittest.main()
