from selenium import webdriver


webdriver_bin = '/usr/local/bin/chromedriver'
target_url = 'https://www.vmware.com/jp.html'

# Instanciate with path to chromedriver binary
driver = webdriver.Chrome(executable_path=webdriver_bin)

driver.get(target_url)

driver.quit()
