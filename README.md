# Scrapy Project

## Introduction
This repository contains a web scraping project implemented using the Scrapy framework in Python. The project showcases the ability to extract data from websites using Scrapy.

## Project Description
The Scrapy Spider in this project scrapes the reviews of a specific product from an e-commerce website. It extracts the reviewer's name, rating, and comment for each review.

## Usage
1. Install Scrapy framework: `pip install scrapy`
2. Run the spider: `scrapy runspider product_reviews_spider.py -o reviews.json`
3. Replace `product_reviews_spider.py` with the actual spider file name.
4. The reviews will be saved in a JSON file named `reviews.json`.

## Contributing
Contributions are welcome! If you have any suggestions, ideas, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
