import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        print("Scraping:", url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url,headers=headers,timeout=15,allow_redirects=True)

        if response.status_code != 200:
            return f"Failed to fetch {url}. Status code: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts/styles
        for script in soup(["script", "style", "noscript"]):
            script.extract()

        text = soup.get_text(separator=" ")
        text = " ".join(text.split())

        print("Scraped text length:", len(text))

        if len(text) < 50:
            return "No meaningful content found on this page."

        return text

    except Exception as e:
        return f"Error scraping website: {str(e)}"