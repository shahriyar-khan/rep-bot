from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import smtplib

email = smtplib.SMTP("smtp.gmail.com", 587)


def main():
    # Initialize Driver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.get("https://uta-cobsubjectpool.sona-systems.com/")
    script(driver)


def script(driver):
    # Login Page
    elem_login = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_userid")))
    elem_login.click()
    elem_login.send_keys("username")
    elem_pass = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_pw")
    elem_pass.click()
    elem_pass.send_keys("password")
    elem_loginbtn = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_default_auth_button")
    elem_loginbtn.click()

    # Home Page
    elem_view = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "lnkStudySignupLink")))
    elem_view.click()

    # List Page
    list_btn = "ctl00_ContentPlaceHolder1_repStudentStudies_ctl00_HyperlinkStudentTimeSlot"
    try:
        elem_study = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, list_btn)))
        elem_study.click()
    except TimeoutException:
        driver.quit()
        email.starttls()
        email.login("email_id", "email_id")
        email.sendmail("email_id", "email_id", "\nREP Bot: No studies were found at this time!")
        email.quit()
        exit()

    # Studies Page
    elem_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_lnkNonAdmin")))
    elem_list.click()

    # Signup Page
    try:
        elem_signup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_repTimeSlots_ctl00_Submit_Button")))
        elem_signup.click()
    except TimeoutException:
        driver.quit()
        email.starttls()
        email.login("email_id", "email_id")
        email.sendmail("email_id", "email_id", "\nREP Bot: You've already claimed this study!")
        email.quit()
        exit()

    # Confirmation Page
    elem_confirm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_Submit_Button")))
    elem_confirm.click()
    email.starttls()
    email.login("email_id", "email_id")
    email.sendmail("email_id", "email_id", "\nREP Bot: You successfully claimed a study!")
    email.quit()
    driver.quit()


if __name__ == "__main__":
    main()
