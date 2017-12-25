from selenium import webdriver

driver = webdriver.Chrome()
url='https://passport.jd.com/new/login.aspx?'
driver.get(url)

driver.add_cookie({'name':'TrackID','value':'14qbpI4wjVu13RNnXOTRQAIDddXqFp\
Oj4KkgddMeH4WC7oEThLEqxochX3KcIh3lpPsPU8Jt3W08KqUCL8HVzOMDT1PdvwVHQVeSrZj7T964'})
driver.add_cookie({'name':'thor','value':'376E279740F11E64EADEE9AF3\
50006C463B5D10B600F2AB8860237345064427F65E7DA16A45AEB6570AF64DD55515\
9893B2D967F3D1C2AEC8B88681CA4AD38281A0543F6DB8924E9E9D6465564E8AB123A\
7F642FC0120E38549F3A07982FDCE869BA6C9A966CF4125E376FE5639BDC852027AB02FB3\
43BC7A801F659AD9BC304B4D0CC4CB544659462F90A0496A9CF49B0386D145073595A6C21E66E99C67AA6'})
#driver.add_cookie({'name':'_t=','value':'nbbmPgRFtO/SW5r75P6tI5pkWM0TBsbPt2XY+ACYvFI='})
#driver.add_cookie({'name':'ol','value':'1'})
driver.add_cookie({'name':'ceshi3.com','value':'201'})

driver.get(r'https://www.jd.com/')



with open(r'g://1.txt','w',encoding='utf-8') as f:
    f.write(driver.page_source)



