
import unittest
from textnode import TextNode, TextType




class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a link text node", TextType.LINK, "https://www.google.com")
        
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a italic text node", TextType.ITALIC, "https://www.google.com")
        node2 = TextNode("This is a italic text node", TextType.ITALIC)

        self.assertNotEqual(node, node2)


    def test_eq4(self):
        node = TextNode("This is a code text node", TextType.CODE, "https://www.google.com")
        node2 = TextNode("This is a code text node", TextType.LINK, "https://www.google.com")

        self.assertNotEqual(node, node2)






if __name__ == "__main__":
    unittest.main()









