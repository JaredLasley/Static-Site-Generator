import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_TextNode(self):
        node = TextNode("Text node test text",TextType.BOLD)
        node2 = TextNode("Text node test text",TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_text(self):
        node = TextNode("Text one is different from text two", TextType.TEXT)
        node2 = TextNode("Text two is different from text one",TextType.TEXT)
        self.assertNotEqual(node,node2)
        
    def test_url(self):
        node = TextNode("Text node test text", TextType.BOLD, url=None)
        node2 = TextNode("Text node test text", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_diff_url(self):
        node = TextNode("Text node test text", TextType.BOLD, url="https://www.boot.dev")
        node2 = TextNode("Text node test text", TextType.BOLD)
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()