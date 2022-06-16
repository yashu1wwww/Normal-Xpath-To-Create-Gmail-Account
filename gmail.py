from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://support.google.com/mail/answer/56256?hl=en")

input=driver.find_element_by_xpath('//*[@id="hcfe-content"]/section/div/div[1]/article/section/div/div[1]/div/p[1]/a').click()

input=driver.find_element_by_xpath('//*[@id="firstName"]').send_keys("gamer")
input.send_keys(Keys.RETURN)

input=driver.find_element_by_xpath('//*[@id="lastName"]').send_keys("game")
input.send_keys(Keys.RETURN)

input=driver.find_element_by_xpath('//*[@id="username"]').send_keys("naatu123")

input=driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys("smash1@#$")

input=driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys("smash1@#$")

input=driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/div[3]').click()

input=driver.find_element_by_xpath('//*[@id="phoneNumberId"]').send_keys("smash1@#$")

time.sleep(20)

input=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

input=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[3]').click()

time.sleep(10)

input=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span').click()

input=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/span').click()

input=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]').click()

time.sleep(20)
