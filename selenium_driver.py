from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://ictd.gov.bd/')

from selenium.webdriver.common.by import By

element = driver.find_element(By.NAME, 'title')
element.send_keys('Python website testing')
element.submit()

# Close the browser
driver.quit()