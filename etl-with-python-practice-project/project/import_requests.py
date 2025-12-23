import requests
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd


BASE_URL = "https://web.archive.org/web/20230908091635/https://www.pakwheels.com/used-cars/karachi/24857"
OUTPUT_FILE = "pakwheels_cars.csv"

response = requests.get(BASE_URL)
soup =  BeautifulSoup(response.text, "html.parser")
cars_list = soup.find_all("li", class_="classified-listing")

# print(cars_list)


# -----------------------------
# Helper: Clean extracted text
# -----------------------------
def clean(text):
    return text.replace("\n", "").replace("\t", "").strip() if text else ""


# -----------------------------
# Extract single car data
# -----------------------------
def parse_car(card):
    data = {}

    # Title
    title_tag = card.find("a", class_="car-name")
    data["title"] = clean(title_tag.text) if title_tag else ""

    # Price
    price_tag = card.find("div", class_="price-details")
    data["price"] = clean(price_tag.text) if price_tag else ""

    # Car URL
    data["url"] = "https://www.pakwheels.com" + title_tag["href"] if title_tag else ""

    # Meta Data (city, year, mileage, fuel, engine, transmission)
    meta1 = card.find_all("ul", class_="search-vehicle-info")
    meta2 = card.find_all("ul", class_="search-vehicle-info-2")

    if meta1:
        lis1 = meta1[0].find_all("li")
        if lis1: data["city"] = clean(lis1[0].text)

    if meta2:
        lis2 = meta2[0].find_all("li")
        if len(lis2) >= 5:
            data["year"] = clean(lis2[0].text)
            data["mileage"] = clean(lis2[1].text)
            data["fuel"] = clean(lis2[2].text)
            data["engine_cc"] = clean(lis2[3].text)
            data["transmission"] = clean(lis2[4].text)

    # Updated time
    updated = card.find("div", class_="dated")
    data["updated"] = clean(updated.text) if updated else ""

    return data


# -----------------------------
# Extract cars for 1 page
# -----------------------------
def extract_page(url):
    print(f"Scraping: {url}")
    
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    cars_list = soup.find_all("div", class_="search-list")
    print(cars_list)

    results = []

    for card in cars_list:
        car_data = parse_car(card)
        results.append(car_data)

    return results


# -----------------------------
# Write CSV Once
# -----------------------------
def write_csv(data):
    keys = ["title", "price", "city", "year", "mileage", "fuel", "engine_cc", "transmission", "updated", "url"]
    
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)



# results = []

# for card in cars_list:
#     car_data = parse_car(card)
#     results.append(car_data)


# print(results)


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    all_data = []

    # Scrape first 5 pages (you can increase limit)
    for page in range(1, 2):
        url = BASE_URL + f"?page={page}"
        all_data.extend(extract_page(url))
        time.sleep(1)  # respectful delay

    # write_csv(all_data)
    # print(f"\n✔ Scraping completed. Data saved into '{OUTPUT_FILE}'")
    

df= pd.read_csv("pakwheels_cars.csv")
# print(pw_data)

def clean_price(p):
    p = str(p).lower().replace("pkr", "").replace(",", "").strip()
    if "lacs" in p:
        return float(p.replace("lacs", "").strip()) * 100000
    return float(p) if p.isnumeric() else None

# df["price_num"] = df["price"].apply(clean_price)

# df["mileage_num"] = (
#     df["mileage"]
#     .astype(str)
#     .str.replace("km", "")
#     .str.replace(",", "")
#     .str.strip()
#     .astype(float)
# )

# import matplotlib.pyplot as plt

# plt.figure(figsize=(8,5))
# plt.hist(df["price_num"].dropna(), bins=20)
# plt.title("Car Price Distribution")
# plt.xlabel("Price (PKR)")
# plt.ylabel("Count")
# plt.show()


# plt.figure(figsize=(8,5))
# plt.hist(df["mileage_num"].dropna(), bins=20)
# plt.title("Mileage Distribution")
# plt.xlabel("Mileage (km)")
# plt.ylabel("Count")
# plt.show()

# plt.figure(figsize=(8,5))
# df["year"].value_counts().sort_index().plot(kind="bar")
# plt.title("Cars Count by Year")
# plt.xlabel("Year")
# plt.ylabel("Cars Listed")
# plt.show()


