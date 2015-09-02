from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Python Thursday Blog' in browser.title
browser.quit()
