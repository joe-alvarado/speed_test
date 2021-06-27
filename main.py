import tkinter as tk
import datetime as dt
today = dt.date.today()
#imports driver
from selenium import webdriver
#imports common keys ENTER, SHIFT etc
from selenium.webdriver.common.keys import Keys
from time import sleep
import smtplib
from email.message import EmailMessage
import imghdr

email = "##"
password = "##"


def test():
    chrome_driver_path = "/Users/joealvarado/Development/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
#Tells driver to navigate to URL
    driver.get("https://fast.com")
    sleep(15)
#click more info, to get upload
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/div[1]/a").click()
    sleep(30)
    driver.save_screenshot("/Users/joealvarado/Development/screenshot.png")
    driver.quit()

def send_r():
    msg = EmailMessage()
    msg['Subject'] = 'Speed test results screenshot'
    msg['From'] = email
    msg['To'] = ['##', '##']
    msg.set_content(f'Speed test results...{today}')

    with open('/Users/joealvarado/Development/screenshot.png', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)

master = tk.Tk()
master.title("Speed Test")
tk.Label(master,
         text="Speed Test GUI", font=("Courier", 23)).grid(row=0, column=0, pady=10, padx=40)


tk.Button(master,
          text='Run Speed Test', command=test).grid(row=1,
                                                       column=0,
                                                       sticky=tk.N,
                                                       pady=10, padx=10)
tk.Button(master,
          text='Email Results', command=send_r).grid(row=2,
                                                       column=0,
                                                       sticky=tk.N,
                                                       pady=10, padx=10)
tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.N,
                                    pady=10, padx=10)

tk.Label(master, text="Joe Alvarado", font=("Courier", 9)).grid(row=17, column=0, sticky="w")
tk.Label(master, text="v 1.0", font=("Courier", 9)).grid(row=17, column=0, sticky="e")

tk.mainloop()
