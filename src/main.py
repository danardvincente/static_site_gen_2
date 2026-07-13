import os
import shutil
import sys

from copy_static_content import copy_source_to_destination
from generate_webpage import generate_pages_recursive



static_path = "./static"
#public_path = "./public"
public_path = "./docs"
content_path = "./content"
template_path = "./template.html"
default_basepath = "/"




def main():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

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
    generate_pages_recursive(content_path, template_path, public_path, basepath)




if __name__ == "__main__":
    main()










