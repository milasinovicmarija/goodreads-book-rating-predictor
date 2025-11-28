# Using the ISBN to fetch book information from an external API (Google Books API)
# Since the genre is not directly available in the Goodreads exported data, we will use the ISBN to get more details about the book.

import requests

def fetch_book_info(isbn: str) -> dict:
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()
    
    if "items" not in data:
        return None
    
    info = data["items"][0]["volumeInfo"]
    
    # From the fetched info, we can extract relevant details
    book_details = {
        "title": info.get("title", "N/A"),
        "authors": info.get("authors", []),
        "publishedDate": info.get("publishedDate", "N/A"),
        "categories": info.get("categories", []),
        "pageCount": info.get("pageCount", 0),
        "averageRating": info.get("averageRating", 0),
        "ratingsCount": info.get("ratingsCount", 0),
    }
    return book_details