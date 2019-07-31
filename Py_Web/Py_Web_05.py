'''1.selenium修改input输入框和单选框
   2.selenium处理页面弹窗，alert和comfirm
        win = driver.switch_to_alert()
        win.accept()  #确定
        win.dismiss()  #取消
   3.自动化常见验证码解决方案
        1.破解验证码
            OCR识别:tesseract=ocr
            AI机器学习
        2.绕过
            让开发人员关闭验证码  安全性需要保密，一般在开发测试环境使用
            提供一个万能验证码    安全性需要保密，一般在开发测试环境使用
            使用cookie （登录主要时为了拿cookie，获取登录凭证）
   '''
#   4.自动化测试实战进阶操作cookie和使用场景
#from selenium import  webdriver
#from time import sleep
#from selenium.webdriver.common.action_chains import ActionChains
#
#driver = webdriver.Firefox()
#driver.get("https://xdclass.net")
#print(driver.title)
#sleep(3)
#driver.add_cookie({"name":"name","value":"123456"})
#driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTguanBlZyIsImlkIjoxMTY5NywibmFtZSI6IjEyMzQ1NiIsImlhdCI6MTU2NDU3NDc1NiwiZXhwIjoxNTY1MTc5NTU2fQ.uRIp_tAAF1YHnF83xZ91SKfYU_Itlc6c04ZMH2YZe4M"})
#
#video_ele = driver.find_element_by_css_selector('[title="19年录制互联网架构之分布式缓存Redis从入门到高级实战"]')
#video_ele.click()
#sleep(3)
#driver.switch_to_window(driver.window_handles[1])
#buy_btn = driver.find_element_by_class_name("buy_tolearn")
#buy_btn.click()
#print("进入下单页面")

#5.webdriver自动截图
from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://xdclass.net")
print(driver.title)
sleep(3)
driver.find_element_by_css_selector(".login > span:nth-child(2)").click()
sleep(3)
driver.find_element_by_css_selector('[placeholder="请输入手机号"]').send_keys("17606863713")
sleep(3)
driver.find_element_by_css_selector('[placeholder="请输入6-16位密码"]').send_keys("123456")
sleep(3)
driver.find_element_by_css_selector(".btn").click()
sleep(3)
try:
    driver.find_element_by_css_selector('[href="#/message"]').click()
except:
    driver.get_screenshot_as_file("./error.png")