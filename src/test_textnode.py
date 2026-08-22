import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()