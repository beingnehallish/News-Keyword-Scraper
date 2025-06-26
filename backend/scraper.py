import feedparser

def scrape_rss(keyword):
    feeds = [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.hindustantimes.com/feeds/rss/india-news/rssfeed.xml",
    ]

    keyword = keyword.lower()
    results = []

    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if keyword in entry.title.lower() or keyword in entry.get("summary", "").lower():
                results.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.get("summary", ""),
                    "time": entry.get("published", "Unknown time")
                })

    return results