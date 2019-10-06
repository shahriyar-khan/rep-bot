from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import smtplib

sendEmail = smtplib.SMTP("smtp.gmail.com", 587)
messageYes = "\nREP Bot: You successfully claimed a study!"
messageNo = "\nREP Bot: No studies were found at this time!"
messageClaimed = "\nREP Bot: You've already claimed this study!"


def main():
    # Initialize ChromeDriver and get URL
    initChromeDriver()
    # Identify login elements and login with credentials
    loginPage()
    # Proceed to view studies from home page
    homePage()
    # Available study = view available studies
    # No studies = print text placeholder and quit driver
    listPage()
    # View available studies again
    studiesPage()
    # Proceeds to final sign-up confirmation page
    # Return warning message if study is already claimed and quit driver
    signupPage()
    # Sign-up/claim the available study. Return success after sign-up is successful.
    confirmPage()
    # Quit driver and flush previous data
    quitDriver()


def initChromeDriver():
    global driver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.get("https://uta-cobsubjectpool.sona-systems.com/")


def loginPage():
    elemLogin = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_userid")))
    elemLogin.click()
    elemLogin.send_keys("username")
    elemPass = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_pw")
    elemPass.click()
    elemPass.send_keys("password")
    elemLoginbtn = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_default_auth_button")
    elemLoginbtn.click()


def homePage():
    elemView = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "lnkStudySignupLink")))
    elemView.click()


def listPage():
    listPageButton = "ctl00_ContentPlaceHolder1_repStudentStudies_ctl00_HyperlinkStudentTimeSlot"
    try:
        elemStudy = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, listPageButton)))
        elemStudy.click()
    except TimeoutException:
        driver.quit()
        sendEmail.starttls()
        sendEmail.login("email_id", "email_id")
        sendEmail.sendmail("email_id", "email_id", messageNo)
        sendEmail.quit()
        exit()


def studiesPage():
    elemList = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_lnkNonAdmin")))
    elemList.click()


def signupPage():
    try:
        elemSignUp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_repTimeSlots_ctl00_Submit_Button")))
        elemSignUp.click()
    except TimeoutException:
        driver.quit()
        sendEmail.starttls()
        sendEmail.login("email_id", "email_id")
        sendEmail.sendmail("email_id", "email_id", messageClaimed)
        sendEmail.quit()
        exit()


def confirmPage():
    elemConfirm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_Submit_Button")))
    elemConfirm.click()
    sendEmail.starttls()
    sendEmail.login("email_id", "email_id")
    sendEmail.sendmail("email_id", "email_id", messageYes)
    sendEmail.quit()


def quitDriver():
    driver.quit()


if __name__ == "__main__":
    main()
