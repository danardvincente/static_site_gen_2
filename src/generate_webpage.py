from markdown_blocks import extract_title, markdown_to_html_node
from pathlib import Path
import re, os


def generate_page(from_path: str, template_path: str, dest_path: str | Path, basepath: str) -> None:

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        from_path_content = file.read()
    #print(from_path_content)


    with open(template_path) as file:
        temp_path_content = file.read()

    pnode = markdown_to_html_node(from_path_content)
    html_content = pnode.to_html()
    
    #splt_from_path_content = from_path_content.split("\n")
    #print(splt_from_path_content)
    the_title = extract_title(from_path_content) 

    with open(template_path) as file:
        template_path_content = file.read()


    title_pattern = r"\{\{\s*Title\s*\}\}"
    content_pattern = r"\{\{\s*Content\s*\}\}"

    title_match = re.findall(title_pattern, template_path_content)
    content_match = re.findall(content_pattern, template_path_content)
    final_template_content = template_path_content.replace(
            title_match[0], the_title).replace(
            content_match[0], html_content)
    final_template_content = final_template_content.replace('href="/', 'href="' + basepath)
    final_template_content = final_template_content.replace('src="/', f"src=\"{basepath}")



    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(final_template_content)
    
    #print(final_template_content)

    #return final_template_content




def generate_pages_recursive(dir_path_cont: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    for filename in os.listdir(dir_path_cont):
        from_path = os.path.join(dir_path_cont, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)










