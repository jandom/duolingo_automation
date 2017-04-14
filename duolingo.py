from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from translations import translations
import os, sys

#setup

# fp = webdriver.FirefoxProfile()
# fp.set_preference("webdriver.load.strategy", "unstable");
# driver = webdriver.Firefox(firefox_profile=fp)

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

#driver.maximize_window()


#login
driver.get("https://tinycards.duolingo.com")
driver.find_element_by_class_name("_2A2uR").click()
driver.find_element_by_class_name("_2a16Y").send_keys(username)
driver.find_element_by_class_name("_3FjlE").send_keys(password,Keys.RETURN)
WebDriverWait(driver, 10, 0.05).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/profile']")))

driver.get(url)

try:
	WebDriverWait(driver, 10, 0.05).until(EC.presence_of_element_located((By.CLASS_NAME, "_3rQ1C")))
	driver.find_element_by_class_name("_3rQ1C").click()

	cards = driver.find_elements_by_css_selector("._2qbTM")
	print(len(cards))
	for card in cards[-1:]:
		left, right = card.find_elements_by_css_selector("textarea")
		left.send_keys("foo")
		right.send_keys("bar")

 	


except Exception as e:
	print e
	driver.get(url)
	try:
	    WebDriverWait(driver, 3).until(EC.alert_is_present(),
	                                   'Timed out waiting for PA creation ' +
	                                   'confirmation popup to appear.')

	    alert = driver.switch_to_alert()
	    alert.accept()
	    print "alert accepted"
	except TimeoutException:
	    print "no alert"
