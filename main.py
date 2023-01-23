from selenium import webdriver
import time 
import yagmail
import os
 
def get_driver(): 
  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", 
                                  ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver= webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver 

def clean_text(text):
    output = float(text.split(" ")[0])
    return output

def emailsend(price):
  rec=input("enter the email you want the stock to be notified on:")
  sender='aryangoel540@gmail.com'
  reciever= rec
  subject="The stock price went below -1.10%"
  contents=f"""
  The new price is {price}%
  """
  yag= yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
  yag.send(to=reciever,subject=subject,contents=contents)
  
def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath",value= '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
  price= clean_text(element.text)

  if price < -0.10:
    emailsend(price)

  else :
    print("price is above -1.10%")

main()
    