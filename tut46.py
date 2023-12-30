# Creatng command line utilities 

# The command-line utility is a.n example of an application that uses the service interface to run and manage services.

import argparse
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size= 8192):
                f.write(chunk)
    return local_filename
parser = argparse.ArgumentParser()

# Add command line arguments 
parser.add_argument("url", help = "Url of the file to download")
# parser.add_argument("output", help = "by which name do you want to save your file")
parser.add_argument("-o", "--output", help = "Name of the file", default = None)  # -o is used for optional

# Parse the arguments 
args = parser.parse_args()

# Use the arguments in our code 
print(args.url)
print(args.output)
download_file(args.url, args.output)

# command - py file_name link or py file_name link -o image_name.jpg