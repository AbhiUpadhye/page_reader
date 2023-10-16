import requests
from bs4 import BeautifulSoup
import re
import argparse

def get_text_from_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract all text from the HTML
            text = ' '.join(soup.stripped_strings)
            # Remove HTML tags and extra spaces
            text = re.sub(r'<[^>]+>', '', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def calculate_reading_time(text, words_per_minute=200):
    words = text.split()
    num_words = len(words)
    reading_time_minutes = num_words / words_per_minute
    return reading_time_minutes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate estimated reading time for an HTML page.')
    parser.add_argument('url', help='URL of the HTML page to analyze')
    parser.add_argument('words_per_minute', type=int, default=200, help='Average reading speed in words per minute')

    args = parser.parse_args()

    html_text = get_text_from_html(args.url)

    if html_text:
        reading_time = calculate_reading_time(html_text, args.words_per_minute)
        print(f'Estimated reading time: {reading_time:.2f} minutes at {args.words_per_minute} words per minute')
    else:
        print('Failed to fetch the HTML page.')
