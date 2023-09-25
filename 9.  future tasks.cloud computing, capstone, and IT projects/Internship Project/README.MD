# Amazon Scraper and Data Processing

This project consists of two main Python scripts that scrape product data from Amazon and then process and store the retrieved data in a PostgreSQL database.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

1. **Scraping Script**: This script utilizes Selenium and BeautifulSoup to scrape product information from Amazon for predefined categories such as Smartphones, Laptops, Video Games, Dresses, Shoes, and Accessories. The scraped data includes:
   - Product ID
   - Product Name
   - Price
   - Ratings
   - Number of Reviews
   - Review Information (Up to 5 reviews per product)
   - URL of the Product
   - Category

2. **Data Processing Script**: This script loads the scraped JSON data into a Pandas DataFrame, cleans, and formats it, ensuring that any missing values are handled appropriately. The processed data is then inserted into a PostgreSQL table, and any inconsistencies in the URLs are resolved. Additionally, the DataFrame is saved to a CSV file for further use.

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL
- Selenium WebDriver
- BeautifulSoup

### Installing Dependencies
```sh
pip install selenium beautifulsoup4 pandas psycopg2-binary word2number webdriver-manager
```

### Database Setup
- Ensure that PostgreSQL is installed and running.
- Create a database and user, and grant the necessary permissions.
- Update the database connection parameters in the script.

### Selenium WebDriver
- The script uses the Edge WebDriver, ensure that it is installed and available in the system PATH.

## Usage

1. **Running the Scraping Script**: 
   ```sh
   python scraper_script.py
   ```
   The script will scrape product data for the predefined categories and save the results in a JSON file named `amazon_data_ext.json`.

2. **Running the Data Processing Script**: 
   ```sh
   python data_processing_script.py
   ```
   This script will read the `amazon_data_ext.json`, process the data, insert it into the PostgreSQL table, and save it to a CSV file named `amazon_data_ext.csv`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source. Feel free to use, modify, and distribute the code as you see fit.