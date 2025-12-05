--Simple Web Scraper--

A simple Python script to scrape all paragraph (`<p>`) text from any website and save it into a CSV file.

--Features

- Scrapes all `<p>` tags from a given website URL.

- Cleans and extracts only the visible text.

- Saves the extracted text into a CSV file.

- Handles input disruptions gracefully (useful for running in CMD/Terminal).

--Requirements

- Python 3.x  

- `requests` library  

- `beautifulsoup4` library  

--You can install the required libraries using pip:

--bash
pip install requests beautifulsoup4

--Usage

1.Run the script:
  
  python scraper.py
  
2.Enter the website URL when prompted.

3.Enter a name for the CSV file (e.g., output.csv).

4.The script will scrape all paragraphs and save them into the specified CSV file.

--Example:

Enter the website URL to scrape: https://en.wikipedia.org/wiki/Artificial_intelligence

Enter a CSV file name: ai_paragraphs.csv

Success! Data stored in 'ai_paragraphs.csv'

--Notes

Ensure the URL is valid and accessible.

The CSV file will be created in the same directory as the script.

Only <p> tag text is extracted; other content (headings, links, tables) is ignored.
