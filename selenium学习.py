from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get(r'http://www.w3school.com.cn/tiy/t.asp?f=html_form_radio')
assert "Python" in driver.title     #浏览器的标题
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


#close是关闭当前标签页，quit是关闭浏览器
#driver.close()


element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    #获取属性
    print("Value is: %s" % option.get_attribute("value"))
    option.click()


from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

#取消所有选择
select = Select(driver.find_element_by_id('id'))
select.deselect_all()

#列出所有已经选择的选项
select = Select(driver.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected_options

获得所有选项:
options = select.options


#可以使用拖放，无论是移动一个元素，或放到另一个元素内:
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")
from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


#dr.window_handles返回当前浏览器的所有标签的句柄（str）
for i in dr.window_handles:
    #激活句柄为i的标签页
	dr.switch_to_window(i)


#跳转到弹出的alert/confirm/prompt对话框
alert = driver.switch_to_alert()
a.accept()                  #按确认键
a.dismiss()                 #按取消键
a.send_keys('asd')          #输入'asd'，这里必须是prompt
a.text                      #返回对话框的文本





