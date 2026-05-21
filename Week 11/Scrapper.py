import requests
from bs4 import BeautifulSoup
import csv

car = input("Enter manufacturer name: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com"
}

url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'

response = requests.get(url, headers=headers)

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(["Car Name", "Price"])

        writer.writerows(data)

    print(f"Data saved successfully in {filename}")

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')

    car_data = []

    for table in tables:

        rows = table.find_all('tr')

        for row in rows:

            cols = row.find_all('td')

            if len(cols) >= 2:

                name = cols[0].get_text(strip=True)

                price = cols[1].get_text(strip=True)

                print(f"Car Name: {name} - Price: {price}")

                
                car_data.append([name, price])

    save_to_csv(car_data, f"{car}_cars.csv")

else:
    print("Page not available!")