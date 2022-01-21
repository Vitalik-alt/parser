import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup

import re
import os

os.system("cls")

'''
self.assertIn("Python", driver.title)
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
assert "No results found." not in driver.page_source
'''

def slow_type(element, text, delay = 0.1):
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

######################################################################
source_data = page.page_source
soup = BeautifulSoup(source_data, "html.parser")
#print(soup)
shedule = soup.find_all('div', {'class':['col-md-6']})

#print(shedule)

#print(soup.div.h4.text)
#print(soup.div.tbody.get_text(separator = " ").strip())
date = number = time_start = time_end = name = ""
for data in shedule:
#	print(soup.div.table.get_text(separator = " ").strip())
#	print(data.text, sep = ' ', end = '\n\n\n\n\n')
#	line = print(data.get_text(separator = " ").strip(), sep = ' ', end = '\n\n\n\n\n')
	line = data.get_text(separator = " ").strip()
	lesson = re.split("(\d \d{2}:\d{2} \d{2}:\d{2})", str(line))
	for i, el in enumerate(lesson):
#		print(el)
		if i == 0:
			date = re.findall("\d{2}.\d{2}.\d{4}", el)
#			print(date)
#			if date == []: continue
		
		if i % 2 == 1:
			number = re.findall("\d ", el)[0]
#			print(number)

			time_start = re.findall("\d{2}:\d{2}|$", el)[0]
#			print(time_start)
			
			time_end = re.findall("\d{2}:\d{2}", el)[1]
#			print(time_end)
		if i % 2 == 0:
			name = el
#			print(name)
		data = (str(date), number, str(time_start), str(time_end), str(name))
		print(data)



'''
	tmp = data.get_text(separator = " ").strip()
	date = re.findall("\d{2}.\d{2}.\d{4}", tmp)
	print(date)
	
	lesson = re.findall("\d \d{2}:\d{2}", tmp)
	print(lesson)

	print("\n\n\n\n\n")
'''

#	link = re.findall("\d{2}.\d{2}.\d{4}", shedule)

'''
allNews = soup.findAll('a', class_='lenta')
for data in allNews:
    if data.find('span', class_='time2 time3') is not None:
        filteredNews.append(data.text)
'''

#html = BeautifulSoup(page.text, "html.parser")
#print(html.title)
#print(html.title.text)
