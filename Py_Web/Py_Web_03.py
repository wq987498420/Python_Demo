'''
selenium 八种定位网页元素方法
    1.id属性定位：find_element_by_id()
    2.name属性定位：find_element_by_name()
    3.class name属性定位：find_element_by_class_name()  定位方式和id定位相似，id、那么、和class一般在网页都至少会有其中的以重
    4.tag name标签定位：find_element_by_tag_name() 通过标签名取定位，用的很少
    5.link text超链接内容定位：find_element_by_link_text()
    6.partial link text超链接模糊内容定位：find_element_by_partial_link_text()
使用python判断是否正确跳转至理想页面
    driver.title 或者 driver.current_url
'''
from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
#driver.get("https://www.baidu.com")
#print(driver.title)

# 1.id属性定位：find_element_by_id()
#driver.find_element_by_id("kw").send_keys("python")
#driver.find_element_by_id("su").click()

#2.name属性定位：find_element_by_name()
#driver.find_element_by_name("wd").send_keys("python")
#3.class name属性定位：find_element_by_class_name()
#driver.find_element_by_class_name("s_btn").click()
#sleep(3)
#driver.close()

#5.link name超链接内容定位：find_element_by_link_text()
#driver.find_element_by_link_text("hao123").click()
#sleep(3)
##6.partial link text超链接模糊内容定位：find_element_by_partial_link_text()
#driver.find_element_by_partial_link_text("人民").click()
#sleep(3)
#driver.close()

'''7.css selector元素定位：find_element_by_css_selector()  
        css定位策略：  
            1.id选择器：  #id  以#号修饰
            2.class选择器：  .class  以.修饰
            3.属性选择器：[id="id"]  或#id
                        [class="class"]  或.class
                        [其他属性="其他属性"]
            4.层级：  p input/p>input
            5.层级带属性：p[属性名="属性值"]>input
                        p#id>input
                        p.class>input
            6.元素选择器：  element
            7.CSS延伸：  
                        input[type^="p"]    说明：type以p字母开头的元素                     
                        input[type$="d"]    说明：type以d字母结尾的元素                      
                        input[type*="w"]    说明：type包含w字母的元素                      
        '''
#driver.get("https://login.taobao.com")
#print(driver.title)
#driver.find_element_by_partial_link_text("密码登录").click()
#driver.find_element_by_css_selector("input#TPL_username_1").send_keys("123123132")
#driver.find_element_by_css_selector("[class='login-text'][id='TPL_password_1']").send_keys("123123132")
'''8.xpath路径定位：find_element_by_xpath()
        xpath定位策略：
            1.路径定位
                1).绝对路径   以单斜杠开头  如：/html/body/form/div/fieldser/p[1]/input
                2).相对路径   双斜杠揩油   如//input
                注意：  /或//后跟的必须为元素标签或*
            2.利用元素属性-定位
            3.层级与属性结合-定位
            4.属性与逻辑结合-定位
            注意：在XPATH路径定位中，元素所有的属性必须以@修饰
            
        延伸：
            //*[text()="xxx"]     文本内容是xxx的元素
            //*[starts-with(@attribute.'xxx')]    属性以xxx开头的元素
            //*[containss(@attribute.'Sxxx')]     属性中包含有xxx的元素
            
            
            '''

'''定位方式分类-汇总：
        1).id、name、class name（元素class属性）：为元素属性定位
        2).tag_name：为元素标签名称
        3).link_text,partial_link_text: 为超链接定位（a标签）
        4).Xpath：为元素路径定位
        5).Css：为Css选择器定位
        
    元素属性（id、name、class）区别：
        1.id一般为唯一      <input type="text"  id=id>
        2.name可以重名      <a name = name1/> <div name = name1/>
        3.class可以多个     class = name1 name2 name3
        
    元素常用操作方法：
        1.clear()     清空文本
        2.send_keys   模拟输入
        3.click()     单击元素
        
        4.back()      后退页面
        5.maximize_window()   最大化窗口（模拟浏览器最大化按钮）
        6.submit      提交表单
        7.refresh()   刷新（模拟浏览器F5刷新）
        8.close()     关闭（模拟浏览器关闭按钮（关闭单个窗口））
        9.quit()      关闭（关闭所有WebDriver启动的窗口）
        10.text       获取元素的文本
        11.tiele      获取页面title
        12.current_url 获取当前页面URL
    操作鼠标方法：WebDriver操作鼠标的方法封装在ActionChains类中
        1.double_click()    双击（模拟鼠标双击效果）
        2.drag_and_drop()   拖动（模拟鼠标拖动效果）
        3.move_to_element() 悬停（模拟鼠标悬停效果）
        4.perform()         执行（执行以上所有鼠标方法）
        
        '''


