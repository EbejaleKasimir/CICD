
# Amazon Web Scraping Project

This project scrapes product data from Amazon and stores it in a PostgreSQL database.

## Usage

The main scraping logic is in `scrape_amazon.py`. It extracts product details like name, price, ratings, reviews, category and URL from Amazon search result pages.

To run it:

```
python scrape_amazon.py
```

This will scrape data for the categories defined in `categories` and save the JSON output to `amazon_data.json`.

`process_data.py` then:

- Loads the JSON data into a Pandas DataFrame
- Cleans the data
- Creates a PostgreSQL table
- Inserts the data into the table 

To run it:

```
python process_data.py
```

The data is also saved to `amazon_data.csv`.

## Requirements

- Python 3
- BeautifulSoup 4
- Selenium
- Pandas
- psycopg2

## Database Schema

The PostgreSQL database contains a single table `amazon_data` with the following columns:

- `product_id` - TEXT, Amazon ASIN 
- `product` - TEXT, product name
- `price` - NUMERIC, product price
- `ratings` - NUMERIC, product rating 
- `reviews` - INTEGER, number of reviews
- `category` - TEXT, search category 
- `url` - TEXT, product URL

## Notes

- Only the first 10 pages are scraped for each category. This can be configured by changing the page limit in `scrape_amazon.py`.
- I appended `.json` and `.csv` to the output files but these can be named anything.

Let me know if you would like me to explain or expand on any part of the project!