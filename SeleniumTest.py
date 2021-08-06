from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome()
driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#https://www.python.org/search/?q=pycono&submit=
url = driver.current_url
text = url.split('&')[0]
finalText = text.split('q=')[1]
print("Texto pesquisado: {}".format(finalText))
assert "No results found." not in driver.page_source
driver.quit()


