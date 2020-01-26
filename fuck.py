print('Hello World!')



from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True


binary = FirefoxBinary('C:\\Users\\summe\\AppData\\Local\\Mozilla Firefox\\firefox.exe')


options = Options()
options.add_argument('-headless')


#browser = webdriver.Firefox(capabilities=cap, executable_path="C:/WebDriver/bin/geckodriver.exe")

browser = Firefox(firefox_binary=binary, executable_path="C:\\WebDriver\\bin\\geckodriver.exe", firefox_options=options, capabilities=cap)

browser.get('http://google.com/')
browser.quit()





'''

#Simple assignment
from selenium.webdriver import Firefox



Firefox(executable_path='C:/WebDriver/bin/geckodriver.exe')



driver = Firefox()

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False


Firefox(executable_path='C:/WebDriver/bin/geckodriver.exe')

driver = Firefox()


driver.get("http://www.neopets.com/dome/fight.phtml")

element = driver.find_element_by_id("nextstep").click()


#http://www.neopets.com/dome/arena.phtml


#element = driver.find_element_by_id("start")

print(element)



# Now click on button
#driver.find_element_by_id('start').click()

print('End')

WebDriverWait(driver, timeout=3)

browser.quit()

#Or use the context manager
#from selenium.webdriver import Firefox



#mvn test -Dwebdriver.gecko.driver=C:WebDriver/bin/

#with Firefox() as driver:
   #your code inside this indent
   
   '''
