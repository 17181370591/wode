from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr = webdriver.Firefox()
dr.get(r'http://www.baidu.com')
#截图并保存
driver.save_screenshot(r'C:\Users\Administrator\Desktop\1\screenshot.png')


#返回当前url
dr.current_url


#前进和后退
dr.forward()
dr.back()


#获取cookies
dr.get_cookies()


#获取cookie
cookie=dr.get_cookies()


#查找，下面的每个方法有对应的find_elements
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector


#查找a标签的text='Continue'
continue_link = dr.find_element_by_link_text('Continue')
#查找a标签的text含有'Conti'
continue_link = dr.find_element_by_partial_link_text('Conti')


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#打开百度，打开贴吧，搜索'软件考试'，进入该贴吧
#click部分可以用send_keys(Keys.ENTER)和send_keys(Keys.RETURN)代替
#WebDriverWait里的10参数表示最大等待时间，单位秒，超时会报TimeoutException错误
dr = webdriver.Firefox()
dr.get(r'http://www.baidu.com')

#等待text='贴吧'的a标签出现后选择
tb=WebDriverWait(dr,10).until(EC.presence_of_element_located((By.LINK_TEXT,'贴吧')))
tb.click()

#等待id='wd1'的标签出现后选择，该标签是输入框，输入'软件考试'
e1=WebDriverWait(dr,10).until(EC.presence_of_element_located((By.ID,'wd1')))
e1.send_keys('软件考试')
e2=dr.find_element_by_link_text('进入贴吧')
e2.click()


#判断是否出现弹出框（alert，confirm，prompt），出现则返回alert对象，否则返回false
e=EC.alert_is_present()
a=e(dr)
a.send_keys('good')
#判断locator对象(By.ID,'answer568245X722X154701')是否被选中，出现则返回alert对象，否则返回false
e=EC.element_located_to_be_selected((By.ID,'answer568245X722X154701'))
e(dr)
#判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'
EC.visibility_of_element_located((By.ID,'authcode'))
e(dr)
#判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement
EC.presence_of_element_located((By.ID,'authcode'))
e(dr)


#运行js代码，滚动滚动条
dr.execute_script('window.scrollTo(0,document.body.scrollHeight)')
dr.execute_script('window.scrollTo(110,0)')
#jquery代码
dr.execute_script('$(window).scrollTop($("html").height());')


#设置代理ip，http和https的ip都能使用
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '221.226.20.158')
profile.set_preference('network.proxy.http_port', 8080)  # int
profile.update_preferences()
dr = webdriver.Firefox(firefox_profile=profile)
dr.get('http://httpbin.org/get')


#删除，添加，获取cookie
dr.delete_all_cookies()
dr.add_cookie({'name':'ABC','value':'DEF'})
dr.get_cookies()


#最大化窗口
dr.maximize_window()
#设置窗口宽，高
dr.set_window_size(width,height)
#设置窗口位置
dr.set_window_position(x,y)
 
