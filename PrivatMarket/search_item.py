from selenium import webdriver

# Firefox
driver = webdriver.Firefox()

# ------------------------------
# The actual test : open search item on site

# Go to privatmarket.ua
driver.get('https://privatmarket.ua/')

# Enter item name
text_area = driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div/div/form/div/div/div[1]/input')
text_area.send_keys("бронежилет")

# Searsh by item name
search_button = driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]/div/div/form/div/div/div[1]/button')
logotip = driver.find_element_by_xpath('/html/body/div[1]/footer/div/div/div[1]/div/a/img')
search_button.click()

# Make this an actual test.
assert " найдено 0 результатов" not in driver.page_source

# Close the browser!
driver.quit()