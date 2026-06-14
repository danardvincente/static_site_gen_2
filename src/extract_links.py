import re



def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    
    patterns = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    
    #mkdwn_imgs = []
    #alt_text = re.findall(r"\[(.*?)\]", text)
    #img_link = re.findall(r"\((.*?)\)", text)

    #for i in range(len(alt_text)):
     #   mkdwn_imgs.append((alt_text[i], img_link[i])) """

    mkdwn_imgs = re.findall(patterns, text)

    
    return mkdwn_imgs


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    
    patterns = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

     
    #mkdwn_links = []
    #anchor_text = re.findall(r"\[(.*?)\]", text)
    #url = re.findall(r"\((.*?)\)", text)

    #for i in range(len(anchor_text)):
      #  mkdwn_links.append((anchor_text[i], url[i])) 
    

    mkdwn_links = re.findall(patterns, text)


    return mkdwn_links




    







