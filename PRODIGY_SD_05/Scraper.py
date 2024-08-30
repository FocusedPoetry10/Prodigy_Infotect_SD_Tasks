import requests
from bs4 import BeautifulSoup
import csv

# URL of the Books to Scrape website
url = 'http://books.toscrape.com/'

# Send a request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Open a CSV file to write the data
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability', 'Rating'])  # Write the header row

    # Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]

        # Write book information to CSV
        writer.writerow([title, price, availability, rating])

print('Data has been successfully written to books.csv')
