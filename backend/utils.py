def validate_articles(articles):
    return all('title' in a and 'link' in a for a in articles)