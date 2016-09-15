from selenium import webdriver

# Firefox
driver = webdriver.Firefox()

# ------------------------------
# The actual test : open chat on site

# Go to privatmarket.ua
driver.get('https://privatmarket.ua/')

# Open chat window
search_chat_button = driver.find_element_by_xpath('/html/body/div[1]/div/header/nav/div/div[1]/p[2]/button')
search_chat_button.click()

# Make this an actual test.
assert "Задайте вопрос" in driver.page_source


print (driver.page_source)
# Close the browser!
driver.quit()