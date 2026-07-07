from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType




def markdown_to_htmlnode(markdown_text: str) -> ParentNode:
    """ converts a full markdown document into a single parent HTMLNode. 
    That one parent HTMLNode should (obviously) contain many child HTMLNode 
    objects representing the nested elements. """


    blocks = markdown_to_blocks(markdown_text)
    

    for block in blocks:
        





def text_to_childern(text: str) -> list[HTMLNode]:
    """ function tha:t works for all block types. It takes a string of 
    text and returns a list of HTMLNodes that represent the inline markdown 
    using previously created functions (think TextNode -> HTMLNode).   """

    txt_node = text_to_textnode(text)
    node_list = []
    for txtn in txt_node:
        node_list.append(text_node_to_html_node(txt_node))

    return node_list


            













