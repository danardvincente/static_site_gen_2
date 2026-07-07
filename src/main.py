import os
import shutil


from copy_static_content import copy_source_to_destination
from generate_webpage import generate_pages_recursive



static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"


def main():

    print("Deleting public directory...")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("Copying static files to public directory...")
    copy_source_to_destination(static_path, public_path)

    print("Generating webpage...")

    """ generate_page(
            os.path.join(content_path, "index.md"),
            template_path,
            os.path.join(public_path, "index.html")
        ) """
    generate_pages_recursive(content_path, template_path, public_path)




if __name__ == "__main__":
    main()










