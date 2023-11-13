import re
from lxml import html
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# just using it for error handling part
check = 0

print("HEY THERE ! , NOW YOU CAN COMPARE PRICES OF YOUR FAVOURITE CLOTHING ACROSS MULTIPLE SITES")
print("")

# Getting Snapdeal url from user
print("Enter Snapdeal url")
snapdeal_url = input()
print("")

# Getting redwolf url from user
print("Enter Redwolf url")
Redwolf_url = input()
print("")

# Getting bewakoof url from user
print("Enter Bewakoof url")
Bewakoof_url = input()
print("")

# Providing header to be passed as argument in requesting page 
headers = {"user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"}



# FOR SNAPDEAL :--->

# Requsesting the page and parsing it 
page = requests.get(url=snapdeal_url, headers=headers)
# ERROR HANDELING :
if page.status_code == 200 :
    soup = BeautifulSoup(page.content, 'lxml')

    # Extracting the title from the HTML page recieved via url
    title = soup.find("h1" , class_="pdp-e-i-head" )
    text = title.get_text() 
    product_title = text.strip() 
    p1 = "snapdeal : "+product_title

    # Extracting the price from HTML page recieved via url
    price = soup.find("span" , "payBlkBig")
    snapdeal_price_value = price.get_text().strip()
    # Removal of rupee symbol , and than converting price to float [which was intitially recieved as string]
    snapdeal_price_value = re.sub(r'₹', '', snapdeal_price_value)
    snapdeal_price_value = float(snapdeal_price_value.replace(",", "").strip())

else :
    check+=1
    print("!!! Please Enter a valid Snapdeal URL !!!")


# FOR BEWAKOOF :--->

# Requsesting the page and parsing it 
page = requests.get(url=Bewakoof_url, headers=headers)
if page.status_code == 200 :
    soup = BeautifulSoup(page.content, 'lxml')

    # Extracting the title from the HTML page recieved via url
    title = soup.find(id="testProName" )
    text = title.get_text() 
    product_title = text.strip()
    p2 = "Bewakoof :"+product_title

    # Extracting the price from HTML page recieved via url
    price = soup.find("span" , class_="sellingPrice mr-1")
    bewakoof_price_value = price.get_text().strip()
    # Removal of rupee symbol , and than converting price to float [which was intitially recieved as string]
    bewakoof_price_value = re.sub(r'₹', '', bewakoof_price_value)
    bewakoof_price_value = float(bewakoof_price_value.replace(",", "").strip())

else :
   check+=1
   print("!!! Please Enter a valid Bewakoof URL !!!") 

# FOR REDWOLF :--->

# Requsesting the page and parsing it 
page = requests.get(url=Redwolf_url, headers=headers)
if page.status_code == 200 :
    soup = BeautifulSoup(page.content, 'lxml')

    # Extracting the title from the HTML page recieved via url
    title = soup.find("h1" , class_="page-title" )
    text = title.get_text() 
    product_title = text.strip()
    p3 = "RedWolf :"+product_title 

    # Extracting the price from HTML page recieved via url
    price = soup.find("span" , class_="special-price")
    redwolf_price_value = price.get_text().strip()
    # Removal of Rs symbol , and than converting price to float [which was intitially recieved as string]
    redwolf_price_value = re.sub(r'Rs\. ', '', redwolf_price_value)
    redwolf_price_value = float(redwolf_price_value.replace(",", "").strip())

else :
    check+=1
    print("!!! Please Enter a valid RedWolf URL !!!")



# COMPAIRING THE PRICES WITH HELP OF GRAPHS :-

# Ensuring all URLS were valid , only then trying to plot graph :
if check == 0 :
    # Setting the x-axis :
    websites = [p1, p2, p3]
    # Setting the y-axis :
    prices = [float(snapdeal_price_value), bewakoof_price_value, float(redwolf_price_value)]

    # Plotting Bar Graph :
    plt.bar(websites, prices)
    # Setting Y limits to make graph look more appealing and , assuring it always start from 0
    plt.ylim(0, max(prices) + 1000) 
    # Setting the title of Bar-Graph 
    plt.title('Price Comparison for Clothing')
    # Setting X-Label :
    plt.xlabel('Websites')
    # Setting Y-Label :
    plt.ylabel('Price (INR)')

    # Making bar show their height in X.00 format :
    for i, price in enumerate(prices):
        plt.text(websites[i], price, f'{price:.2f}', ha='center', va='bottom')
    # Showing the graph:
    plt.show()
