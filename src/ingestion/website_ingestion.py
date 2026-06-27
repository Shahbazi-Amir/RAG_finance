import requests
from bs4 import BeautifulSoup
import os

# Base URL for the author's page
AUTHOR_URL = "https://www.fintelligence.ir/Author/Detail/4/دکتر-کمیل-رودی"
BASE_DOMAIN = "https://www.fintelligence.ir"
SAVE_PATH = "../data/raw/webpages"

def fetch_article_links():
    response = requests.get(AUTHOR_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = []
    # logic to find article links based on the structure
    for a in soup.find_all('a', href=True):
        if '/Blog/Detail/' in a['href']:
            links.append(BASE_DOMAIN + a['href'])
    return list(set(links))

# Save links to a text file for tracking
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

links = fetch_article_links()
print(f"Found {len(links)} articles.")
# Save links to a file to be processed later
with open(os.path.join(SAVE_PATH, "links.txt"), "w") as f:
    for link in links:
        f.write(link + "\n")
