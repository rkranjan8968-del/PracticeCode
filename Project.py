
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)  # don't auto-close browser   # Keeps the browser open


service = Service()
Service("C://Users//rajee//Downloads//chromedriver-win64//chromedriver-win64//chromedriver.exe")  # update path
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")



# time.sleep(50)  # keeps browser open for 10 seconds






# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--start-maximized")  # optional: opens browser in full screen

# # This will always download the correct ChromeDriver version matching your Chrome
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get("https://www.google.com")