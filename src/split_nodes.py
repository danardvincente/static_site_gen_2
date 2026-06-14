from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links




def text_to_textnodes(text: str) -> list[TextNode]:
    

    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    #print(nodes)

    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    
    #print(nodes)

    return nodes






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
            continue
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

        


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for tn in old_nodes:
        if tn.text_type != TextType.TEXT:
            new_nodes.append(tn)
            continue
        else:
            org_text = tn.text
            img_info = extract_markdown_images(org_text)
            if len(img_info) == 0:
                new_nodes.append(tn)
                continue

            for img in img_info:
                sections = org_text.split(f"![{img[0]}]({img[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))

                new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
                org_text = sections[1]

            if org_text != "":
                new_nodes.append(TextNode(org_text, TextType.TEXT))
    
        
    return new_nodes       







def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


""" 
The goal of both split_nodes_image and split_nodes_link is to parse inline markdown elements out of plain TextType.TEXT nodes. They turn a single mixed node into a list of segmented nodes.

Because both functions behave almost identically, we can walk through how split_nodes_image breaks down the problem.

Step 1: Filter and Skip Non-Text Nodes
for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
        new_nodes.append(old_node)
        continue

We only want to parse links and images out of plain text. If a node is already marked as a TextType.BOLD, TextType.IMAGE, etc., we do not want to alter it. We append it to our results list unchanged and move to the next node.

Step 2: Find All Targets
original_text = old_node.text
images = extract_markdown_images(original_text)
if len(images) == 0:
    new_nodes.append(old_node)
    continue

We extract all image metadata (alt texts and URLs) using regex. If there are no images in this block of text, we can append the original node intact and skip the heavy lifting.

Step 3: Split the Text Sequentially
If there are images, we must loop through each match one by one. This is the heart of the algorithm:

for image in images:
    # Split the text exactly once around the CURRENT image match
    sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
    
    if len(sections) != 2:
        raise ValueError("invalid markdown, image section not closed")

The call original_text.split(..., 1) splits the text on the very first occurrence of that specific image markdown. This guarantees we get exactly two halves:

sections[0]: The text before the image.
sections[1]: The text after the image.
Step 4: Process and Append Nodes
    # If there was text before the image, add it as a standard TEXT node
    if sections[0] != "":
        new_nodes.append(TextNode(sections[0], TextType.TEXT))
    
    # Add the IMAGE node itself
    new_nodes.append(
        TextNode(
            image[0],
            TextType.IMAGE,
            image[1],
        )
    )
    
    # Shrink our workspace to the remaining text after the split image
    original_text = sections[1]

By reassigning original_text = sections[1], we ensure that the next iteration of the loop works only on the remaining, unprocessed part of the string.

Step 5: Clean Up Trailing Text
if original_text != "":
    new_nodes.append(TextNode(original_text, TextType.TEXT))

Once we have processed every single image, there might still be some plain text trailing after the very last image. If original_text is not empty, we wrap it in a final TextType.TEXT node and append it.    

"""



