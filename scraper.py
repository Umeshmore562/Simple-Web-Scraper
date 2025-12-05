import requests
from bs4 import BeautifulSoup
import csv

def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("Input disrupted. Please run the script from CMD/Terminal.")
        exit()

def scrape_website():
    url = safe_input("Enter the website URL to scrape: ").strip()

    file_name = safe_input("Enter a CSV file name (example: output.csv): ").strip()

    if not file_name.endswith(".csv"):
        file_name += ".csv"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print("Error: Unable to open URL.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")

    data = [[p.get_text(strip=True)] for p in paragraphs if p.get_text(strip=True)]

    try:
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Extracted Text"])
            writer.writerows(data)
    except:
        print("Error: Could not save CSV file.")
        return

    print(f"\nSuccess! Data stored in '{file_name}'")

scrape_website()
