from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
def initial_url():
	driver = webdriver.Firefox()
	driver.get("http://991thewhale.com/listen-live/popup/")
	el = driver.find_element_by_xpath('//*[@id="player-content"]/div/div/div/section/iframe')
	p = el.get_attribute('src')
	driver.close()
	return p
def main_loop():
	src = initial_url()
	driver = webdriver.Firefox()
	driver.get(src)
	pst = ''
	while (1):
		try:
			el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[1]')
		except NoSuchElementException:
			print("NoSuchElementException occured!, let us wait and see")
			time.sleep(2)
			el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[1]')
			if not el:
				print("still no element, let us refresh a bit")
				driver.refresh()
				time.sleep(2)
				el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[1]')
				continue
		st = el.text

		if st == pst:
			time.sleep(10)
			continue
		pst = st
		try:
			el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[2]/span')
		except NoSuchElementException:
			print("NoSuchElementException occured!, let me refresh and see")
			time.sleep(2)
			el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[2]/span')
			if not el:
				print("still no element, let us refresh a bit")
				driver.refresh()
				time.sleep(2)
				el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[2]/span')
				continue

			
		st = st + ', ' + el.text + '\n'
		st = st.lower()
		file_ob = open("songs.txt", "r+")
		st_lines = file_ob.readlines()
		file_ob.close()
		print(st)
		print(st_lines)
		print(st in st_lines)
		if st not in st_lines:
			file_ob = open("songs.txt", "a+")
			file_ob.write(st )
			file_ob.close()

		time.sleep(10)
		driver.refresh()
		time.sleep(5)
	driver.close()
if __name__ == '__main__':
	main_loop()


