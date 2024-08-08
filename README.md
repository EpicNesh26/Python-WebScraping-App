# Web Scraping App

### Overview
This Web Scraping App is a Python-based GUI tool designed to scrape quotes, authors, and tags from the website "http://quotes.toscrape.com" and save the data to a CSV file.

### Features
- **URL Input**: Specify the base URL to scrape.
- **Page Selection**: Define the number of pages to scrape.
- **Data Display**: View scraped data in a treeview.
- **Save Functionality**: Save the scraped data to a CSV file.

### Requirements
- Python 3.x
- requests
- beautifulsoup4
- pandas
- lxml
- tkinter

### Installation
1. Clone this repository:
```sh
git clone https://github.com/EpicNesh26/Python-WebScraping-App.git
cd web-scraping-app
```
2. Install the required packages:
```sh
pip install requests beautifulsoup4 pandas lxml
```

### Usage
1. Run the application:
```sh
python app.py
```
2. Enter the base URL (http://quotes.toscrape.com).
3. Enter the number of pages to scrape.
4. Click "Scrape" to fetch and display the quotes.
5. Click "Save to CSV" to save the data to a CSV file.

### Code
Here's a brief overview of the code:

- fetch_page(url): Fetches the HTML content of the given URL.
- parse_quotes(html_content): Parses the HTML content to extract quotes, authors, and tags.
- save_to_csv(data, filename): Saves the extracted data to a CSV file.
- scrape_quotes(): Scrapes quotes from the specified URL and number of pages.
- save_data(): Saves the displayed data to a CSV file.

### Contributing
Feel free to fork this project, make improvements, and submit pull requests. Any contributions are welcome!

### License
This project is licensed under the MIT License.
