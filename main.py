from bs4 import BeautifulSoup
import requests
import html5lib
import smtplib
import time


def userInput():
    global flipkartProductURL
    global amazonProductURL
    flipkartProductURL = input('Enter the flipkart product URL:')
    amazonProductURL = input('Enter the amazon product URL:')
def trackPrices():
    headers = {'User-Agent should be added here.'}
    if flipkartProductURL and amazonProductURL:
        flipkartResponse = requests.get(flipkartProductURL,headers=headers)
        amazonResponse = requests.get(amazonProductURL,headers=headers)
        flipkartSoup = BeautifulSoup(flipkartResponse.content,'html5lib')
        amazonSoup = BeautifulSoup(amazonResponse.content,'html5lib')
        flipkartProductPrice = float(flipkartSoup('div',attrs='The flipkart div class should be added here.').text.replace(',','')[1:])
        amazonProductPrice = float(amazonSoup.find('span',attrs='priceBlockDealPriceString').text.replace(',','')[1:])
        print('Flipkart product is ', str(flipkartProductPrice))
        print('Amazon Product Price is ',str(amazonProductPrice))
        if flipkartProductPrice and amazonProductPrice:
            sendEmail(amazonProductPrice,flipkartProductPrice)

def sendEmail(amazonPrice, flipkartPrice):
    message = ''
    if amazonPrice and flipkartPrice and (amazonPrice > flipkartPrice):
        message = 'Flipkart price is low.Price is Rs.' +str(flipkartPrice)
    elif flipkartPrice > amazonPrice:
        message = 'Amazon Price is very low. Price is Rs.' +str(amazonPrice)
    fromEmail = 'The email will be attached here.'
    toEmail = 'The email will be attached here.'
    server = smtplib.SMTP('smtp.bitvoo.com',587)
    server.starttls()
    server.login(fromEmail,'The email password will be added here.')
    server.sendmail(fromEmail,toEmail,message)
    print('Mail send Successfully')
    server.quit()

userInput()

while True:
        trackPrices()
        time.sleep(5)

