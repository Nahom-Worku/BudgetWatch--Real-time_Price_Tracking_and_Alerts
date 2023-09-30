# BudgetWatch--Real-time_Price_Tracking_and_Alerts

Python price tracking tool with GUI for monitoring product prices on eBay, Kijiji, and Nike. Get email alerts when prices match your budget. Real-time web scraping and multi-threading for seamless user experience.

This project allows users to track the prices of products on various online shopping websites and receive email alerts when the prices fall within their specified budget. It includes the following features:

Graphical User Interface (GUI): I created a GUI using the tkinter library, which provides a user-friendly interface for users to input their preferences and start price tracking.

Supported Websites: Users can choose from a list of supported websites, including eBay, Kijiji, Nike, and potentially others.

User Input: Users can input the following information:

Their name Email address The URL of the product they want to track A User-Agent string for their browser The desired price they are willing to pay for the product Real-Time Price Tracking: Your Python code utilizes web scraping techniques (with libraries like BeautifulSoup) to fetch the current price of the product from the provided URL.

Email Notifications: If the product's price falls within the user's budget, the program sends an email notification to the user's specified email address, informing them of the price drop and providing a link to the product.

Multi-Threading: I implemented multi-threading to ensure that the GUI remains responsive while the price tracking runs in the background.

Supported Websites: This project supports multiple websites, and has separate Python scripts (e.g., eBayChecker.py, kijijiChecker.py, nikeChecker.py, bitcoinChecker.py) for each supported website. These scripts contain web scraping logic specific to each site.

Periodic Price Checking: I implemented a loop that periodically checks the price of the product. For example, it checks the price every 30 minutes (as indicated in the code).

In summary, this project is a tool that helps users monitor the prices of products on various online shopping websites, and it sends email notifications when the prices meet the user's budget criteria. It provides a user-friendly GUI for ease of use.
