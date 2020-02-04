print('Hello World!')



from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True


binary = FirefoxBinary('C:\\Users\\summe\\AppData\\Local\\Mozilla Firefox\\firefox.exe')


options = Options()
#options.add_argument('-headless')



driver = Firefox(firefox_binary=binary, executable_path="C:\\WebDriver\\bin\\geckodriver.exe", firefox_options=options, capabilities=cap)




driver.get("https://www.codeauthority.com/")

#element = driver.find_elements_by_name("username")
#print (element)
#print("First element:", element[0])

print ("\n\n")

driver.implicitly_wait(5)



#driver.find_element_by_xpath("/html/body/div[6]/div[5]/table/tbody/tr/td/div[2]/div[4]/form/div/div[1]/div[2]/input").send_keys("ve");


#driver.find_element_by_xpath("/html/body/div[6]/div[5]/table/tbody/tr/td/div[2]/div[4]/form/input[2]").click()




print('LOADING')
driver.implicitly_wait(5)


for entry in driver.get_log('browser'):
    print (entry)


print('End!')
print('End!')



#driver.quit()

