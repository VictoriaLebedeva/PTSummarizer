from typing import Union
import requests
from bs4 import BeautifulSoup

def parse_article(url: str) -> Union([str, list]):
    """Gets paragraphs and title from the article.
    
    Args:
        url (str): article's url
    
    Returns:
        result: dict with article's title and paragraphs  
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('h1').text
    paragraphs = []
    paragraphs_html = soup.find_all('p', class_='pw-post-body-paragraph')

    for p in paragraphs_html:
        paragraph = p.text.strip('\t')
        paragraphs.append(paragraph)
        
    return title, paragraphs

if __name__ == '__main__':
    url = 'https://medium.com/history-of-yesterday/six-unexplainable-ancient-artifacts-7f909a0a2c7'
    print(parse_article(url))