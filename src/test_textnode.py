import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.italic)
        node2 = TextNode("This is a different node", TextType.italic)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.italic)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()