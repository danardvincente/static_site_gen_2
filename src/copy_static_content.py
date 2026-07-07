import os
import shutil






def copy_source_to_destination(source_path: str, destination_path: str) -> None:
    
    #destination_dir_path = '~/workspace2/github.com/danardvincente/static_site_gen_2/public'
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    for file in os.listdir(source_path):
        destination_file_path = os.path.join(destination_path, file)
        source_file_path = os.path.join(source_path, file)
        print(f" * {source_file_path} -> {destination_file_path}")

        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path, destination_file_path)
        else:
            copy_source_to_destination(source_file_path, destination_file_path)



