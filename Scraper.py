import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Apple-iPhone-Xs-Max-256GB/dp/B07J318ZLF/ref=sr_1_1?keywords=Iphone&qid=1563108919&s=gateway&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

def check_price():



    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[4:6])

    if (converted_price < 1.100):

        send_mail()

    print(converted_price)
    print(title.strip())

    if (converted_price > 1.100):

        send_mail()

def send_mail():
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() 
    """!Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol 
                  !(ESMTP) command sent by an email server to identify itself when connecting to another
                  !email server to start the process of sending an email. 
                  !It is followed with the sending email server's domain name"""
    server.starttls()
    server.ehlo()
    server.login('Email', 'Password')	#Enter your Email and password
    subject = 'Price fell down!!!'
    Body = 'Check the Amezon link https://www.amazon.in/Apple-iPhone-Xs-Max-256GB/dp/B07J318ZLF/ref=sr_1_1?keywords=Iphone&qid=1563108919&s=gateway&sr=8-1'

    msg = f"Subject:{subject}\n\n{Body}"

    server.sendmail(
        'Enter sender Email',	#Enter sender Email
        'Enter Reciver Email',	#Enter Reciver Email
        
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!!!')
    server.quit()

check_price()
"""
def time():

    while(True):
        check_price()
        time.sleep(86400)
        """
