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

   **Data Dictionary**

      **Dictionary:**
      **Product_ID:** The unique identifier for the product.\n
      **product:** The name and description of the product.\n
      **price in dollars:** The price of the product.\n
      **star ratings:** The average star rating of the product.\n
      **Total Ratings:** The total number of reviews for the product.\n
      **url:** The URL of the product’s review page.\n
      **category:** The category to which the product belongs.\n
      **Customer_i_ID:** The unique identifier for the customer.\n
      **Customer_i_Star_Rating:** The star rating given by the customer.\n
      **Customer_i_Comment:** The review comment made by the customer.\n
      **Customer_i_buying_influence:** A measure of how influential this customer’s review is in terms of influencing other customers’ buying decisions.\n
      **For both top positive and critical reviews:**
      **Review_Cust_ID:** The unique identifier for the customer who wrote the review.\n
      **Review_Cust_Name:** The name of the customer who wrote the review.\n
      **Review_Cust_Influenced:** A measure of how influential this review is in terms of influencing other customers’ buying decisions.\n
      **Review_Cust_Comment:** The content of the review.\n
      **Review_Cust_Comment_Title:** The title of the review.\n
      **Review_Cust_Date:** The date when the review was posted.\n
      **Review_Cust_Star_Rating:** The star rating given by this reviewer.\n
      **Top_Positive_Review_Cust_ID:** The unique identifier for the customer who wrote the top positive review.\n
      **Top_Positive_Review_Cust_Name:** The name of the customer who wrote the top positive review.\n
      **Top_Positive_Review_Cust_Influenced:** A measure of how influential this top positive review is in terms of influencing other customers' buying decisions.\n
      **Top_Positive_Review_Cust_Comment:** The content of the top positive review.\n
      **Top_Positive_Review_Cust_Comment_Title:** The title of the top positive review.\n
      **Top_Positive_Review_Cust_Date:** The date when the top positive review was posted.\n
      **Top_Positive_Review_Cust_Star_Rating:** The star rating given by the customer who wrote the top positive review.\n



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