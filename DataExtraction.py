
#######################  DATA EXTRACTION FROM REMOTE API ##########################################################

import os
import requests
import gzip
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = "https://www.ncei.noaa.gov/pub/data/noaa/"

def download_file(url, directory):
    filename = url.split("/")[-1]
    file_path = os.path.join(directory, filename)
    with open(file_path, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)
    return file_path

def unzip_file(file_path):
    with gzip.open(file_path, 'rb') as f_in:
        with open(file_path[:-3], 'wb') as f_out:
            f_out.write(f_in.read())
    os.remove(file_path)

def main():
    for year in range(1976, 2025):
        year_url = urljoin(base_url, str(year) + "/")
        response = requests.get(year_url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href.startswith("039620") and href.endswith(".gz"):
                file_url = urljoin(year_url, href)
                directory = "./data"
                os.makedirs(directory, exist_ok=True)
                file_path = download_file(file_url, directory)
                unzip_file(file_path)

if __name__ == "__main__":
    main()
