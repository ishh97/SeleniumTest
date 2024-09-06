from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Edge()


driver.get("https://www.simplilearn.com/")
driver.maximize_window()
# time.sleep(3)
driver.implicitly_wait(15)

login = driver.find_element(By.XPATH, "//a[contains(text(),'Log in')]")
login.click()
# time.sleep(3)  
driver.implicitly_wait(15)


email = driver.find_element(By.NAME, "user_login")  
email.send_keys("ishita.161204@gmail.com")

password = driver.find_element(By.NAME, "user_pwd")
password.send_keys("Ishita@16")


password.send_keys(Keys.RETURN)
time.sleep(30)
# driver.implicitly_wait(15)  

assert "Dashboard | Learning on Simplilearn" in driver.title

search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search.send_keys("Selenium")
search.send_keys(Keys.RETURN)
# time.sleep(20)  
driver.implicitly_wait(15)

result = driver.find_element(By.XPATH, "//div[@title='Introduction to Selenium']")
result.click()


time.sleep(10)
video = driver.find_element(By.CSS_SELECTOR , "video.jw-video.jw-reset")
print(video)
arrow = driver.find_element(By.ID, "close-syllabus")
arrow.click()
# # video.click()

time.sleep(15)
driver.back()

# time.sleep(10)

driver.refresh()
# time.sleep(30)
driver.implicitly_wait(30)
time.sleep(10)

grid = driver.find_elements(By.CLASS_NAME, "CourseCard")
for i in grid:
    card = i.find_element(By.CLASS_NAME, "course-content")
    title = card.get_attribute("title")

    if title == "Python for Beginners":
        print(title)
        card.click()
        break


arrow1 = driver.find_element(By.ID, "close-syllabus")
# video.click()
arrow1.click()
time.sleep(30)
# driver.back()
driver.quit()
