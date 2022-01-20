import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
import requests

'''
self.assertIn("Python", driver.title)
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
assert "No results found." not in driver.page_source
'''

def slow_type(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

page = webdriver.Chrome()
page.get('https://dekanat.nung.edu.ua/cgi-bin/timetable.cgi')
page.encoding = 'windows-1251'

select = Select(page.find_element_by_name('faculty'))
select.select_by_visible_text("Інститут інформаційних технологій")

#teacher = page.find_element_by_tag_name("input")
teacher = page.find_element_by_name("teacher")
#teacher.send_keys("Мельничук Степан Іванович")
slow_type(teacher, "Мельничук Степан Іванович")
'''
text = "text to enter"
for character in text:
	teacher.send_keys(character)
    time.sleep(0.3)
'''

#group = page.find_element_by_name("group")
#group.send_keys("ВК-19-1")
#slow_type(group, "ВК-19-1")
date_from = "01.12.2021"
date_to = "31.12.2021"

field_from = page.find_element_by_name("sdate")
slow_type(field_from, date_from)
#field_from.sendKeys(Keys.ENTER)
field_from.submit()

field_to = page.find_element_by_name("edate")
slow_type(field_to, date_to)
field_to.submit()

send = page.find_element_by_tag_name('button')
send.click()

