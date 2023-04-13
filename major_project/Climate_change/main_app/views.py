from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    import requests

# Set up API key and search engine ID
    api_key = 'AIzaSyDRXVYng56GJNHm-YtIdsPqmVIftfiJcmk'
    search_engine_id = 'c13c46cfbee6641cf'

# Construct API request
    query = 'impact of climate change book'
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'

    # Send API request
    response = requests.get(url)

    # Parse JSON response
    json_data = response.json()
    books = []
    for item in json_data['items']:
        book = {
            'title': item['title'],
            'snippet': item['snippet'],
            'link': item['link'],
            'image_url': None  # Initialize image URL to None
        }
        if 'pagemap' in item and 'thumbnail' in item['pagemap']:
            # Extract image URL if available
            book['image_url'] = item['pagemap']['thumbnail'][0]['src']
        books.append(book)

    context = {
        'books': books
    }

    return render(request, 'index.html', context)