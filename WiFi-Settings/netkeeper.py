from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


if __name__ == "__main__":
    c_service = Service('D:\chromedriver\chromedriver.exe')#驱动路径
    c_service.command_line_args()
    c_service.start()
    chrome_options = Options()
    chrome_options.add_argument('--headless')#隐藏浏览器显示
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://user:password@192.168.123.1/Advanced_WAN_Content.asp')#登录进去的账号密码
    '''
    elem = driver.find_element_by_xpath('//*[@id="tbl_vpn_control"]/tbody/tr[4]/td/input')
    elem.clear()
    elem.send_keys('xxxxxx') #这里输入闪讯账号
    '''
    elem = driver.find_element_by_xpath('//*[@id="wan_pppoe_passwd"]')
    elem.clear()
    print("请输入闪讯验证码：")
    elem.send_keys(input())
    driver.find_element_by_xpath('//*[@id="ruleForm"]/div/div/div[2]/div/div/div/div/div/table[8]/tbody/tr/td/center/input').click()
    time.sleep(0.5)
    driver.quit()
    c_service.stop()
    print('Password changed successfully!')
