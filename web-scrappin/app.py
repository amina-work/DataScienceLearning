import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the website
url = "https://www.getresponse.com/help"
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to retrieve content:", response.status_code)
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, "lxml")

# Find the titles of all the category topics of website
titles = soup.select(".category-topic")

# Check if titles were found
if not titles:
    print("No titles found")
    exit()

# Print the titles
for title in titles:
    print(title.text.strip())

# Write the titles to a CSV file
with open("titles.csv", mode="w") as csv_file:
    writer = csv.writer(csv_file)
    for title in titles:
        writer.writerow([title.text.strip()])
