from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

# driver.get("https://www.google.com/")
# driver.find_element(By.LINK_TEXT,'About').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'How').click()
# driver.quit()
    
driver.get("https://ictd.gov.bd")
driver.find_element(By.LINK_TEXT,'ভিশন ও মিশন').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'How').click()
driver.quit()