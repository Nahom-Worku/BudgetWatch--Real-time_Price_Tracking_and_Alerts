import tkinter as tk
from tkinter import ttk
import eBayChecker  
import kijijiChecker
import nikeChecker
import bitcoinChecker

import threading

# Function to execute the checker based on user input
def check_website():
    website = website_var.get()
    userName = username_entry.get()
    URL = url_entry.get()
    userAgent = user_agent_entry.get()
    desiredPrice = float(price_entry.get())
    userEmail = userEmail_entry.get()

    if website == "ebay":
        threading.Thread(target=eBayChecker.eBayChecker, args=(userName, URL, userAgent, desiredPrice, userEmail)).start()
    elif website == "Kijiji":
        threading.Thread(target=kijijiChecker.kijijiChecker, args=(userName, URL, userAgent, desiredPrice, userEmail)).start()
    elif website == "Nike":
        threading.Thread(target=nikeChecker.nikeChecker, args=(userName, URL, userAgent, desiredPrice, userEmail)).start()
    elif website == "Bitcoin" and URL == "https://www.google.com/finance/quote/BTC-CAD?sa=X&ved=2ahUKEwin_6XG19GBAxVgmIkEHZYgCEEQ-fUHegQIBhAf":
        threading.Thread(target=bitcoinChecker.bitcoinChecker, args=(userName, URL, userAgent, desiredPrice, userEmail)).start()
    else:
        result_label.config(text="Invalid input")
        return

# Create the main window
root = tk.Tk()
root.title("Website Checker")

#increase the size of the gui window
root.geometry("700x500")

# Create and configure the main frame
main_frame = ttk.Frame(root)
main_frame.grid(column=0, row=0, padx=90, pady=80)

# Configure ttk.Style to increase line spacing (padding)
style = ttk.Style()
style.configure('TLabel', padding=(0, 10))
style.configure('TEntry', padding=(0, 10))

# Project Title
project_title = ttk.Label(main_frame, text="BudgetWatch: Real-time Price Tracking and Alerts", font=("Helvetica", 15))
project_title.grid(column=0, row=0, columnspan=2)
project_entry = ttk.Entry(main_frame, width=60)

# Label and Entry for website selection
website_label = ttk.Label(main_frame, text="Select Website:", font=("Helvetica", 12))
website_label.grid(column=0, row=1, sticky='w')
website_var = tk.StringVar()
website_combobox = ttk.Combobox(main_frame, textvariable=website_var, values=["Nike", "ebay", "Kijiji", "Bitcoin"], font=("Helvetica", 10))
website_combobox.grid(column=1, row=1)
website_combobox.set("Nike")

# Username Entry
username_label = ttk.Label(main_frame, text="Enter your name:", font=("Helvetica", 12))
username_label.grid(column=0, row=2, sticky='w')
username_entry = ttk.Entry(main_frame, width=40)
username_entry.grid(column=1, row=2)

# UserEmail Entry
userEmail_label = ttk.Label(main_frame, text="Enter your email:", font=("Helvetica", 12))
userEmail_label.grid(column=0, row=3, sticky='w')
userEmail_entry = ttk.Entry(main_frame, width=40)
userEmail_entry.grid(column=1, row=3)

# URL Entry
url_label = ttk.Label(main_frame, text="Enter the URL:", font=("Helvetica", 12))
url_label.grid(column=0, row=4, sticky='w')
url_entry = ttk.Entry(main_frame, width=40)
url_entry.grid(column=1, row=4)

# User-Agent Entry
user_agent_label = ttk.Label(main_frame, text="User-Agent:", font=("Helvetica", 12))
user_agent_label.grid(column=0, row=5, sticky='w')
user_agent_entry = ttk.Entry(main_frame, width=35, font=("Helvetica", 10))
user_agent_entry.grid(column=1, row=5)

# Desired Price Entry
price_label = ttk.Label(main_frame, text="Enter the price you are willing to pay:", font=("Helvetica", 12))
price_label.grid(column=0, row=6, sticky='w')
price_entry = ttk.Entry(main_frame, width=35, font=("Helvetica", 10))
price_entry.grid(column=1, row=6)

# Button to start the check
check_button = ttk.Button(main_frame, text="Check Website", command=check_website)
check_button.grid(column=0, row=9, columnspan=2, sticky='w')

# Label to display the result
result_label = ttk.Label(main_frame, text="")
result_label.grid(column=0, row=7, columnspan=2)

# Start the GUI main loop
root.mainloop()



