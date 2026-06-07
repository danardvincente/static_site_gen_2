from textnode import TextNode, TextType



def split_nodes_delimiter(
        old_nodes: list[TextNode], 
        delimiter: str, 
        text_type: TextType) -> list[TextNode]:

    #delimiter_lst = []
    new_nodes = []
    for txt_node in old_nodes:
        if txt_node.text_type != TextType.TEXT:
            # Non-TEXT nodes pass through unchanged — only TextType.TEXT nodes need splitting.
            new_nodes.append(txt_node)
        else:
            delimiter_lst = []
            sections = txt_node.text.split(delimiter)
            
            """ Even/odd index trick — after splitting, even-indexed sections (0, 2, 4, ...) 
            are plain text, odd-indexed ones (1, 3, 5, ...) are the delimited (e.g. bold/italic/code) 
            content. This works because delimiters always come in pairs.   """
            if len(sections) % 2 == 0:
                # Even-length check catches unclosed delimiters — a properly closed delimiter always produces an odd                # number of sections
                raise ValueError(f"missing closing delimiter({delimiter})")

            for s in range(len(sections)):
                if sections[s] == "":
                    """ Empty strings are skipped — if the text starts or ends with a delimiter,
                    .split() produces an empty string at the boundary, which we ignore to avoid 
                    creating empty nodes.   """
                    continue
                elif s % 2 == 0:
                    delimiter_lst.append(TextNode(sections[s], TextType.TEXT))
                else:
                    delimiter_lst.append(TextNode(sections[s], text_type))

    new_nodes.extend(delimiter_lst)


    return new_nodes

        







