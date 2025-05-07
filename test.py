import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://bina.az/items/all"
headers = {'User-Agent': 'Mozilla/5.0'}

def get_links_from_base():
    # Send a request to the base URL
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    # Select all ad links from the page
    for a in soup.select("a.items-i-link"):  # This class matches the ad links
        href = a.get("href")
        if href:
            links.append(href)
    return links

def scrape_detail_page(relative_url):
    # Combine base URL and relative URL to form a complete URL
    FULL_url = base_url + relative_url
    response = requests.get(FULL_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Initialize empty data dictionary to store the scraped values
    data = {
        "id": relative_url.split("/")[-1],
        "kateqoriya": None,
        "sahe": None,
        "cixaris": None,
        "mertebe": None,
        "otaq_sayi": None,
        "temir": None,
        "location": None
    }

    # Extract values based on label texts (e.g., "Kateqoriya")
    for label in soup.find_all("label"):
        label_text = label.text.strip()
        if label_text == "Kateqoriya":
            span = label.find_next("span")
            if span:
                data["kateqoriya"] = span.text.strip()
            break

    # Look for other labels and fill the corresponding fields
    for label in soup.find_all("label"):
        label_text = label.text.strip()
        if label_text == "Sahə":
            span = label.find_next("span")
            if span:
                data["sahe"] = span.text.strip()
        elif label_text == "Çıxarış":
            span = label.find_next("span")
            if span:
                data["cixaris"] = span.text.strip()
        elif label_text == "Mərtəbə":
            span = label.find_next("span")
            if span:
                data["mertebe"] = span.text.strip()
        elif label_text == "Otaq Sayı":
            span = label.find_next("span")
            if span:
                data["otaq_sayi"] = span.text.strip()
        elif label_text == "Təmir":
            span = label.find_next("span")
            if span:
                data["temir"] = span.text.strip()
        elif label_text == "Location":
            span = label.find_next("span")
            if span:
                data["location"] = span.text.strip()

    return data

def main():
    # Get all the links from the base page
    links = get_links_from_base()
    print(f"[DEBUG] Found {len(links)} links.")

    # Open CSV file for writing
    with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "kateqoriya", "sahe", "cixaris", "mertebe", "otaq_sayi", "temir", "location"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Loop through each link and scrape the data
        for idx, link in enumerate(links):
            print(f"\n[DEBUG] Processing link {idx+1}/{len(links)}: {link}")
            data = scrape_detail_page(link)
            if data:
                # Write the extracted data to CSV
                writer.writerow(data)
                print(f"[RESULT] Written to CSV: {data}")
            time.sleep(1)  # Slight delay to avoid overloading the server

if __name__ == "__main__":
    main()
