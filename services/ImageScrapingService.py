import requests
from bs4 import BeautifulSoup
import urllib.robotparser

class ScrapingService:
    def __init__(self,url):
        self.url = url

    def scrape(self):
        if not self.url:
            raise ValueError("URL cannot be empty.")
        
        print(f"Starting the scraping of images from {self.url} ")
        html= requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        images = []
        for img in soup.find_all('img'):
            img_url = img.get('src') if img.get('src').startswith('https') else img.get('data-src')
            if img_url:
                images.append(img_url)

        if not images:
            raise ValueError("No images found at the provided URL.")
        
        print(f"Found {len(images)} images.")

        with open('images_links.txt', 'w') as f:
            for img_url in images:
                f.write(img_url + '\n')
            
        print("images links saved to images_links.txt")
        return True
    

    def is_allowed_to_scrap(self,url, user_agent="*"):
        site = url.split("/")[0] + "//" + url.split("/")[2]
        robots_url = site + "/robots.txt"

        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()

        return rp.can_fetch(user_agent, url)
