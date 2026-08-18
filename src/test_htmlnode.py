import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag="p", props={"class": "intro", "id": "header"})
        correct_string = ' class="intro" id="header"'
        self.assertEqual(node.props_to_html(),correct_string)

    def test_props_nospace(self):
        node = HTMLNode(tag="p", props={"class": "intro", "id": "header"})
        incorrect_string = 'class="intro" id="header"'
        self.assertNotEqual(node.props_to_html(),incorrect_string)

    def test_tohtml(self):
        node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(NotImplementedError,node.to_html)

    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://www.google.com", "target": "_blank"})
        correct_string = "HTMLNode(tag = a, value = Click here, children = None, props = {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node),correct_string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_leafnode(self):
        node = LeafNode("a","Testing testing testing")
        node2 = LeafNode("p","Testing testing testing")
        self.assertNotEqual(node,node2)

    def test_leafnode_eql(self):
        node = LeafNode("p","Testing testing testing")
        node2 = LeafNode("p","Testing testing testing")
        self.assertEqual(node,node2)