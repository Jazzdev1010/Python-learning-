import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urljoin
import io
from PIL import Image



def download_and_save_image(image_url):
    filepath = "images/"+image_url.split('/')[-1]
    r = requests.get(image_url)
    if r.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(r.content)

def download_img(image_url):
    w, h = 800, 600
    filepath = "images/"

    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        img = Image.open(io.BytesIO(r.content))
        # Save image to file
        img.save(filepath)


# input url 
input_url = "https://www.cuh.ac.in/"
# get request
html_doc = requests.get(input_url).text
# pass html text content to beautifulsoup 
soup = BeautifulSoup(html_doc, 'html.parser')
# find all img tag
image_urls = soup.find_all("img")
# extract src
for image_url in image_urls:
    image_url_full = urljoin(input_url,image_url.get("src"))
    print(image_url_full)    
    #download_img(image_url_full)
    download_and_save_image(image_url_full)
# print unique url

# use python OS module to print image details
# use llm visual model to get image text, detail and caption.

    