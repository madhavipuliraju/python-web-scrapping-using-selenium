from selenium import webdriver

def getdriver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  driver = webdriver.Chrome(options=options)

  driver.get("https://www.vlab.co.in/")
  element = driver.find_element(by="xpath", value="//*[  @id='objective']/div[2]/div/div/p[1]")
  return element.text

print(getdriver())