from scraper import scrape_rss
from utils import validate_articles

def test_keyword_scraper():
    articles = scrape_rss("India")
    assert validate_articles(articles)
    assert len(articles) > 0