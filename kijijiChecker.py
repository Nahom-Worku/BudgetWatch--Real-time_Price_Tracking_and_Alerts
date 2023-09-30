import time
import requests
from bs4 import BeautifulSoup
import smtplib

# Define a function for checking Kijiji product prices
def kijijiChecker(userName, URL, userAgent, desiredPrice, userEmail):
    # Set the user-agent for the HTTP request
    headers = {"User-Agent": userAgent}

    # Send an HTTP request to the specified URL
    page = requests.get(URL, headers=headers)

    # Parse the HTML content of the page
    soup = BeautifulSoup(page.content, 'html.parser')

    # Define a function to extract the product title
    def title():
        title_element = soup.find(class_="title-2323565163") 
        
        if title_element is not None:
            return title_element.get_text().strip()
        else:
            return 'No title found'

    # Define a function to extract the product price
    def price():
        price_element = soup.find(class_="currentPrice-2842943473")
        
        if price_element is not None:
            return price_element.get_text()
        else:
            return 'No price found'

    # Define a function to check the product information
    def check_product_info():        
        title()  
        price()  

        price_str = price()[1:].strip().replace('$', '')

        if ',' in price_str:
            # If the price string contains a comma, remove it
            price_str = price_str.replace(',', '')
            price_str = price_str.replace("+ taxes", '')

        convertedPrice = float(price_str[0:])
        
        print("\nName of product: ", title())
        print("\nPrice: ", price())
        print("\nConvertedPrice: ", convertedPrice)

        if(desiredPrice >= convertedPrice):
            sendEmail()
        else:
            print("\nThe price of the product is above $",desiredPrice,"meaning it is out of your budget!")
            print("\nLooking for price updates . . .")

    # Define a function to send an email notification
    def sendEmail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('nahomwork21@gmail.com','mxmj rczh xeaw hpnl')

        subject = 'Exciting News: Product Price Now Fits Your Budget'
        body = 'Link for the product: ', URL
        productTitle = 'Product title: ', title()
        productPrice = 'Product price: ', price()
        moreInfo = 'Great news! The product you\'ve been eyeing has just received an update, and its current price aligns perfectly with your budget.'

        msg = f"Subject: {subject}\n\n\n{'Hello, '}{userName}\n\n\n{moreInfo}\n{'Check the information below:'}\n\n{body}\n\n{productTitle}\n\n{productPrice}\n\n"
        
        server.sendmail(
            'nahomwork21@gmail.com',
            userEmail,
            msg
        )

        print("Message Sent Successfully!")

        server.quit()

    # Continuously check the product information
    while(True):    
        check_product_info()
        time.sleep(60*30)       # Wait for half an hour before checking the price again.
