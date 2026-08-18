# Amazon Product Web Scraping using Python

 Project Overview:
This project is a Python-based web scraping application that extracts product information from Amazon search results.
The scraper collects product titles and prices from individual product pages and stores the extracted data in a structured CSV file.

Objective:
The main objective of this project is to automate the process of collecting product information from Amazon using Python.

The project demonstrates practical implementation of:
* Web Scraping
* HTML Parsing
* HTTP Requests
* Data Extraction
* Data Cleaning
* Data Storage

## 🛠️ Technologies Used:
* **Python**
* **Requests** – To send HTTP requests and fetch web pages
* **BeautifulSoup4** – To parse HTML and extract required information
* **Pandas** – To store, process and export scraped data
* **NumPy** – To handle missing values
* **CSV** – To store the final scraped data

## 📊 Data Extracted
The project extracts the following information:

 Field          Description                     
 -------------  ------------------------------- 
 Product Title  Name/title of the product       
 Product Price  Current displayed product price 

## 🔄 Project Workflow:
```
Amazon Search Page
        ↓
Send HTTP Request using Requests
        ↓
Parse HTML using BeautifulSoup
        ↓
Extract Product Links
        ↓
Visit Individual Product Pages
        ↓
Extract Product Title and Price
        ↓
Store Data in Dictionary
        ↓
Convert Data into Pandas DataFrame
        ↓
Clean Missing Values
        ↓
Export Data to CSV
```

## 🔧 Main Features

### 1. HTTP Request
The `Requests` library is used to send HTTP requests to the Amazon website.

### 2. HTML Parsing
BeautifulSoup is used to parse the HTML response and locate required HTML elements.

### 3. Product Link Extraction
The scraper identifies product links from the Amazon search results page and visits each product page.

### 4. Product Information Extraction
The scraper extracts:

* Product Title
* Product Price

### 5. Exception Handling
`try-except` blocks are used so that missing product information does not stop the entire scraping process.

### 6. Data Cleaning
Empty product titles are converted to missing values using NumPy and then removed using Pandas.

### 7. CSV Export
The final cleaned dataset is exported as:

`Amazon_Data.csv`

## 📁 Project Structure
```
Amazon-Web-Scraping/
│
── amazon_scraper.py
── Amazon_Data.csv
── requirements.txt
── README.md
```

## ▶️ How to Run the Project
*Sample data shown for demonstration purposes.*

## 📚 Python Concepts Used
This project helped demonstrate practical use of:

* Functions
* `try-except`
* Dictionaries
* Lists
* Loops
* File handling
* HTTP requests
* HTML parsing
* Data cleaning
* Pandas DataFrame
* CSV file handling

## 🚀 Future Improvements
The project can be extended to extract additional product information such as:

* Product Rating
* Number of Reviews
* Product Availability
* Product URL
* Product Image
* Brand Name

The scraper can also be enhanced with pagination and better error handling.


**Love Kumar**
B.Tech (Information Technology)

### Skills Demonstrated
`Python` `Requests` `BeautifulSoup` `Pandas` `NumPy` `Web Scraping` `Data Cleaning`
