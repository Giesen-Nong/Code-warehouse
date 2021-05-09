from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


if __name__ == "__main__":
    c_service = Service('D:\chromedriver\chromedriver.exe')#这里是驱动路径
    c_service.command_line_args()
    c_service.start()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://user:password@192.168.123.1/Advanced_Extensions_SS.asp')#登录进去的账号密码
    driver.find_element_by_xpath('//*[@id="ss_enable_on_of"]/label/span').click()
    driver.find_element_by_xpath('//*[@id="ruleForm"]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[50]/td/center/input').click()
    time.sleep(0.5)
    driver.quit()
    c_service.stop()
    print('successfully!')
