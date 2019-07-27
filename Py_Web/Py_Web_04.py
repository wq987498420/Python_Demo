'''
第五章  selenium实战之模拟事件处理
    1.自动化测试实战之ActionChains模拟用户行为
        简介：讲解使用selenium里面的ActionChains模拟用户行为
        需求：需要模拟鼠标操作才能进行的情况，比如单继、双击、点击鼠标右键、拖拽
        解决：selenium提供了一个类来处理这类事件
              selenium.webdriver.common.action_chains.ActionChains(driver)
        脚本：from selenium.webdriver.common.action_chains import ActionChains
        执行原理：调用ActionChains的方法时不会立即执行，会将所有操作按顺序存放在一个列队里，
                  当调用perform()方法时，队列中的事件会依次执行
        支持链式写法或者分步写法
        ActionChains(driver).click(ele).perform()
        鼠标和键盘方法列表：
                perform()   执行链中的所有动作
                click(on_element=None)      单继鼠标左键
                context_click(on_element=None)    点击鼠标右键
                double_click(on_element=None)     双击鼠标左键
                move_to_element(to_element)       鼠标移动到某个元素
                ele.send_keys(keys_to_send)       发送某个词到当前焦点的元素

                ====不常用====
                click_and_hold(on_element=None)   点击鼠标左键，不松开
                release(on_element=None)          在某个元素位置松开鼠标左键
                key_down(value,element=None)      按下某个键盘上的键
                key_up(value,element=None)        松开某个键
                drag_and_drop(source, target)     拖拽到某个元素然后松开
                drag_and_drop_by_offset(source,xoffset,yoffset)    拖拽到某个坐标然后松开
                move_by_offset(xoffset, yoffset)  鼠标从当前位置移动到某个坐标
                move_to_element_with_offset(to_element, xoffset, yoffset)   移动到距某个元素（左上角坐标）多少距离的位置
                send_keys_to_element(element, keys_to_send)发送某个键到指定元素
'''
#from selenium import webdriver
#from time import sleep
#from selenium.webdriver.common.action_chains import ActionChains
#
#driver = webdriver.Firefox()
#driver.get("https://xdclass.net")
#sleep(3)
#定位鼠标移动到上面的元素
#menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
#ActionChains(driver).move_to_element(menu_ele).perform()
##选中子菜单
#sub_ele = driver.find_element_by_css_selector('[href="#/courselist?cp_id=1&c_id=6"][style=""]')
#sleep(2)
#sub_ele.click()

#login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
#ActionChains(driver).click(login_ele).perform()
##查找输入框，输入账号密码，输入框需提前清理缓存
#driver.find_element_by_css_selector('[type="text"]').clear()
#driver.find_element_by_css_selector('[type="text"]').send_keys("17606863713")
#sleep(2)
#driver.find_element_by_css_selector('[type="password"]').clear()
#driver.find_element_by_css_selector('[type="password"]').send_keys("wq521.")
#sleep(2)
#click_ele = driver.find_element_by_css_selector(".btn")
#ActionChains(driver).click(click_ele).perform()
#sleep(5)
#
#
#suc_login = driver.find_element_by_css_selector('[href="#/personalcenter"]')
#print("---测试结果---")
#print(suc_login.text)
#suc = suc_login.text
#if suc == u"我的学习  ":
#    print("登录成功！！！")
#    sleep(3)
#    driver.close()
#else:
#    print("登录失败！！！")
#    sleep(3)

'''
4.自动化测试实战之网页等待时间：
    1.为什么需要等待时间--》等系统稳定
            网页需要加载对应资源文件、页面渲染、窗口处理等等
    2.自动化测试常用的等待时间：
            1.强制等待：(开发调试代码是常用)
                    from time import sleep  导入sleep包
                    time.sleep  （不管有没有查找到指定操作，都会等待设置的指定时间）
            2.隐形等待：（实际工作中，一般使用隐式等待）
                    driver.implicitly_wait(10)  隐式等待，最长等待十秒
                    等待元素加载指定的时长，超出抛出NoSuchElementException异常。
            3.显示等待：（在元素出现时间较短，难以定位时使用）
                    WebDriverWait  需配合
                    until和until_not，程序每个N秒检查一次，如果成功则执行下一步，否则继续等待直到超出设定时长
                    WebDriverWait(driver,timeout,pool_frequency=0.5,ignored_exceptions=None).until(lambda x:x.find_element_by_css_selector("#userA"))
                    WebDriverWait(driver,timeout,pool_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(BY.ID,"KW"))
                    使用时需导入以下包
                    from selenium.webdriver.support.ui import WebDriverWait
                    from selenium.webdriver.common.by import By
                    from selenium.webdriver.support import expected_conditions as EC
    结论：隐式等待和显示等待可以同时是同，等待时间取两则执教较大值                  
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
#driver.get("http://www.baidu.com")
##强制等待
#sleep(3)
#print(driver.title)
##显示等待
#driver.implicitly_wait(10)
#driver.find_element_by_id("kw").send_keys("python")
#print(driver.title)
#sleep(3)

driver.get("https://baidu.com")
try:
    # 隐式等待
    ele = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID,"kw1")))
    ele.send_keys("小D课堂")
    print("资源加载成功")
    print(driver.title)
except:
    print("资源加载失败，发送警报右键或者短信")
finally:
    print("程序结束（成功与否都会执行）")
    driver.quit()



