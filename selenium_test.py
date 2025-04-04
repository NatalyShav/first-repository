from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch")

print(browser.title)
assert "Search - Wikipedia" in browser.title
time.sleep(5)

search_box = browser.find_element(By.ID, "ooui-php-1")
search_box.send_keys("Искусственный интеллект")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_element(By.PARTIAL_LINK_TEXT, "Zen")
a.click()
time.sleep(5)


