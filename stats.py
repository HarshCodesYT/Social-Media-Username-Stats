from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

media = input(str("Choose One from 'Facebook , Instagram , Twitter , Twitch': "))
media = str.casefold(media)
if media == "":
    print("Invalid!")

username = input("Enter Username: ")
if username == "":
    print("Invalid!")

path = 'C:\Program Files (x86)\chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://socialblade.com/')

if media == "facebook":
    try:
        social = WebDriverWait(driver , 30).until(
            ec.presence_of_element_located((By.CLASS_NAME , 'dd-container'))
        )
        social.click()

        options = WebDriverWait(driver , 60).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME , 'dd-option'))
        )
        options[2].click()
        
        name = WebDriverWait(driver , 60).until(
            ec.presence_of_element_located((By.ID , 'SearchInput'))
        )
        name.send_keys(username)
        name.send_keys(Keys.RETURN)

    except:
        driver.quit()

if media == "twitch":
    try:
        social = WebDriverWait(driver , 30).until(
            ec.presence_of_element_located((By.CLASS_NAME , 'dd-container'))
        )
        social.click()

        options = WebDriverWait(driver , 60).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME , 'dd-option'))
        )
        options[1].click()
        
        name = WebDriverWait(driver , 60).until(
            ec.presence_of_element_located((By.ID , 'SearchInput'))
        )
        name.send_keys(username)
        name.send_keys(Keys.RETURN)

    except:
        driver.quit()

if media == "instagram":
    try:
        social = WebDriverWait(driver , 30).until(
            ec.presence_of_element_located((By.CLASS_NAME , 'dd-container'))
        )
        social.click()

        options = WebDriverWait(driver , 60).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME , 'dd-option'))
        )
        options[3].click()
        
        name = WebDriverWait(driver , 60).until(
            ec.presence_of_element_located((By.ID , 'SearchInput'))
        )
        name.send_keys(username)
        name.send_keys(Keys.RETURN)

    except:
        driver.quit()


if media == "twitter":
    try:
        social = WebDriverWait(driver , 30).until(
            ec.presence_of_element_located((By.CLASS_NAME , 'dd-container'))
        )
        social.click()

        options = WebDriverWait(driver , 60).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME , 'dd-option'))
        )
        options[4].click()
        
        name = WebDriverWait(driver , 60).until(
            ec.presence_of_element_located((By.ID , 'SearchInput'))
        )
        name.send_keys(username)
        name.send_keys(Keys.RETURN)

    except:
        driver.quit()