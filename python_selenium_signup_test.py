from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# set a link to main testing page
link = "https://unsplash.com/"

# select the browser for webdriver
driver = webdriver.Chrome()

# go to link using browser
driver.maximize_window()
driver.get(link)

# check the main page loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div/span[contains(text(),'Unsplash')]")))

print("- Main page has been successfully opened")


# find the "Sign Up" button
sign_up_button = driver.find_element(By.XPATH, "//div/a[contains(text(),'Sign up')]")

# select button and click on it
sign_up_button.click()

# check the signup page
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div/h4[contains(text(),'Join Unsplash')]")))

print("- Redirect to the registration page is successful")


# fill out the registration form, input firstname
first_name_field = driver.find_element(By.XPATH, "//div/input[@id='user_first_name']")
first_name_field.send_keys("Firstname")

# input last name
last_name_field = driver.find_element(By.XPATH, "//div/input[@id='user_last_name']")
last_name_field.send_keys("Lastname")

# open new tab to create test email
driver.execute_script("window.open('');")

# switch to new tab and open page with test email
driver.switch_to.window(driver.window_handles[1])
driver.get("https://tempmail.plus/")

# wait until email page load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//head/title[contains(text(),'Temp Mail - Disposable Temporary Email - TempMail.Plus')]")
    ))

print("- Transition to the email page page is successful")


# create new random email
new_email_button = driver.find_element(By.XPATH, "//div/button/span[contains(text(),'New random name')]")
new_email_button.click()

# wait for the new email to be created and copy it
driver.implicitly_wait(10)
copy_email_button = driver.find_element(By.XPATH, "//form/div/button[@id='pre_copy']")
copy_email_button.click()

# close the tab with a test email
driver.close()

# switch back to main tab
driver.switch_to.window(driver.window_handles[0])

# input email
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div/input[@id='user_email']")))
email_field.click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # CONTROL on other OS

# input username
username_field = driver.find_element(By.XPATH, "//div/input[@id='user_username']")
username_field.click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # CONTROL on other OS

# remove the @ and symbols after it from username
username_field.send_keys([Keys.BACKSPACE] * 12)

# input password
password_field = driver.find_element(By.XPATH, "//div/input[@id='user_password']")
password_field.send_keys("password")

# check if the "Join" button to send form is clickable
join_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div/a[contains(text(),'Join')]")))

# click on "Join" button
join_button.click()

print("-Registration form has been successfully completed and sent")


# check the profile button of the logged user
profile_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div/button[@title='Your personal menu button']")))
profile_button.click()

print("- User is successfully authorized")


# logout from account
logout_button = driver.find_element(By.XPATH, "//ul/li/a[contains(text(),'Logout')]")
logout_button.click()

# check the user's exit from the system if there is a "Log in" button
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div/a[contains(text(),'Log in')]")))

print("- User has successfully logged out")


print("\n---TEST PASSED!---")


# close the browser after completing the tests
driver.quit()
