
from selenium import webdriver

# Firefox
driver = webdriver.Firefox()

# ------------------------------
# The actual test : open site privatmarket.ua

# Go to privatmarket.ua
driver.get('https://privatmarket.ua/')
print("test passed " + driver2.current_url)

# Make this an actual test.
assert "ПриватМаркет – Площадка для торговли товарами и услугами клиентов ПриватБанка" in driver.title

print("Opened site " + driver.current_url)
# Close the browser!
driver.quit()
