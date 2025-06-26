from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_rss
from utils import validate_articles

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "Keyword required."}), 400

    articles = scrape_rss(keyword)
    if validate_articles(articles):
        return jsonify({"articles": articles})
    else:
        return jsonify({"error": "Validation failed."}), 400
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    keyword = data.get('keyword', '').strip()
    print("🔍 Keyword received:", keyword)  # Add this

    ...

if __name__ == '__main__':
    app.run(debug=True)