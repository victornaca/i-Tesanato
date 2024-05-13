import shutil
import os
from datetime import datetime

def injest_csv():
    source_directory = "SFTP"
    destination_directory = "datalake/landing/csv-price-search/new"

    file_name = "price.csv"
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_file_name = f"price_{current_datetime}.csv"

    if os.path.isfile(os.path.join(source_directory, file_name)):
        try:
            shutil.copy(os.path.join(source_directory, file_name), os.path.join(destination_directory, new_file_name))
            print(f"the archive '{file_name}' copy with success for '{destination_directory}/{new_file_name}'")
        except Exception as e:
            print(f"Error the copy archive '{file_name}': {e}")
    else:
        print(f"The archive '{file_name}' not found in diretory '{source_directory}'")