from bs4 import BeautifulSoup

with open("index.html") as htmlfile:
    soup = BeautifulSoup(htmlfile, "lxml")
htmlfile.close()

items = soup.find_all('div', class_='SampleItems')


for item in items:
    name_of_item=item.h2.getText().strip()
    price=item.button.getText().strip()

    print(f"{name_of_item} has {price}")







