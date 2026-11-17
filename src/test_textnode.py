import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node  = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_imgeq(self):
        node  = TextNode("Text Type == IMG", TextType.IMG, "http://www.imageurl.com/img.jpg")
        node2 = TextNode("Text Type == IMG", TextType.IMG, "http://www.imageurl.com/img.jpg")
        self.assertEqual(node, node2)

    def test_imgnoteq(self):
        node  = TextNode("Text Type == IMG", TextType.IMG)
        node2 = TextNode("Text Type == IMG", TextType.IMG, "http://www.imageurl.com/img.jpg")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
