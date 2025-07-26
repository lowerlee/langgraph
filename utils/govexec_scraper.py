import feedparser
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re
import os
import json


def scrape_govexec_articles(output_path):
    """
    Scrape all articles from the GovExec RSS feed.

    Args:
        output_path (str): Directory to save the scraped articles.

    Returns:
        list: A list of dictionaries containing article details.
    """
    RSS_URL = "https://govexec.com/rss/all/"

    def scrape_govexec():
        feed = feedparser.parse(RSS_URL)
        return [{'title': entry.title,
                 'link': entry.link,
                 'published': datetime(*entry.published_parsed[:6]).strftime('%Y-%m-%d')}
                for entry in feed.entries]

    def extract_clean_content(url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.select_one('h1.content-title')
        title = title.get_text(strip=True) if title else "No title"

        author = soup.select_one('span.authors-multiple a, a.gemg-author-link')
        author = author.get_text(strip=True) if author else "No author"

        main_content = soup.select_one('div.content-body')
        paragraphs = []

        if main_content:
            for element in main_content.find_all(['svg', 'script', 'noscript']):
                element.decompose()

            for p in main_content.find_all('p'):
                text = p.get_text(separator=' ', strip=True)
                text = re.sub(r'\s+', ' ', text).strip()
                text = re.sub(r'\s*,\s*', ', ', text)

                if (len(text) > 30 and
                        not any(phrase in text for phrase in [
                            'Share your', 'NEXT STORY:', 'Help us tailor',
                            'Thank you', 'Stay Connected', 'Newsletter page'
                        ])):
                    paragraphs.append(text)

        return {
            'title': title,
            'author': author,
            'content': ''.join(paragraphs),
            'link': url
        }

    os.makedirs(output_path, exist_ok=True)
    articles = scrape_govexec()
    all_results = []

    for article in articles:
        try:
            print(
                f"Scraping article published on {article['published']}: {article['title']}")
            result = extract_clean_content(article['link'])
            result['published'] = article['published']
            all_results.append(result)
        except Exception as e:
            print(f"Error processing {article['title']}: {e}")

    output_filepath = os.path.join(output_path, "govexec_articles.json")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    return all_results
