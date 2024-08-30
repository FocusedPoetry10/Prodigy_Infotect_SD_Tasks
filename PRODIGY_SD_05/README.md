# 📚 Python Web Scraper for "Books to Scrape"

## Overview

This project is a Python-based web scraper designed to extract book details from the [Books to Scrape](http://books.toscrape.com/) website. The scraper collects key information such as book titles, prices, availability, and ratings and stores it in a CSV file for further analysis.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Data Extraction**: Automatically extracts book details including title, price, availability, and rating.
- **CSV Output**: Saves the extracted data in a CSV file, making it easily accessible and ready for analysis.
- **Python Libraries**: Utilizes `requests` for making HTTP requests, `BeautifulSoup` for parsing HTML, and `csv` for writing data to a file.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/web-scraper-books.git
    cd web-scraper-books
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**
    ```bash
    python scraper.py
    ```

2. **View the output:**
   - The script will generate a file named `books.csv` in the project directory, containing all the extracted book data.

## Code Explanation

### Importing Libraries
```python
import requests
from bs4 import BeautifulSoup
import csv
```
 - **requests:** Used to send HTTP requests to fetch the webpage content.
 - **BeautifulSoup:** Used to parse and navigate the HTML content of the webpage.
 - **csv:** Used to write the extracted data to a CSV file.

### Fetching the Webpage
```python
url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
```
  - The URL of the "**Books to Scrape**" website is stored in the '**url**' variable.
  - '**requests.get(url)**' fetches the content of the webpage.
  - The content is then parsed using '**BeautifulSoup**' to make it easier to extract specific elements.

### Writing data to CSV
```python
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability', 'Rating'])
```
  - Opens a new CSV file called '**books.csv**' in write mode.
  - The first row of the CSV file contains headers: '**Title**', '**Price**', '**Availability**', and '**Rating**'.

### Extracting the Writing Book Data
```python
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    rating = book.p['class'][1]

    writer.writerow([title, price, availability, rating])
```
  - '**soup.find_all()**' finds all instances of the HTML element '**<article>**' with the class '**product_pod**', which represents individual books.
  - For each book, it extracts:
    - '**Title**': From the '**<a>**' tag inside '**<h3>**'.
    - '**Price**': From the '**<p>**' tag with the class '**price_color**'.
    - '**Availability**': From the '**<p>**' tag with the class '**instock availability**', with leading/trailing whitespace removed using '**.strip()**'.
    - '**Rating**': Extracted from the second class of the '**<p>**' tag that contains the rating.
  - Each book's data is then written as a row in the CSV file.

### Final Output Message
```python
print('Data has been successfully written to books.csv')
```
 - Displays a confirmation message once the CSV file has been successfully created.

## Output
- '**books.csv**': A CSV file that includes the following columns:
    - '**Title**': The title of the book.
    - '**Price**': The price of the book.
    - '**Availability**': The stock status of the book.
    - '**Rating**': The rating of the book (e.g., One, Two, Three Stars).
 
## Contributing
Contributions are welcome! If you'd like to enhance this project, feel free to fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the '**LICENSE**' file for more details.

## Acknowledgements
  - Books to Scrape for providing a great site to practice web scraping.
  - BeautifulSoup for making web parsing easy.
  - The open-source community for continuous support and inspiration.
