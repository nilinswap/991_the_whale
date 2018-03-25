from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import os
#os.system("pactl set-sink-mute 0 1")

def initial_url():
	driver = webdriver.Firefox()
	driver.get("http://991thewhale.com/listen-live/popup/")
	while True:
		try:
			el = driver.find_element_by_xpath('//*[@id="player-content"]/div/div/div/section/iframe')
			break;
		except NoSuchElementException:
			print("NoSuchElementException here for iframe link")
			continue
	
	
	p = el.get_attribute('src')
	driver.close()
	return p


	


def main_loop():
	src = initial_url()
	driver = webdriver.Firefox()
	driver.get(src)
	time.sleep(2)
	pst = ''
	while True:
		while True:
			try:
				el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[1]')
				break;
			except NoSuchElementException:
				print("still no element, let us refresh a bit")
				driver.refresh()
				time.sleep(5)
				continue
		st = el.text # name of the song

		if st == pst:
			time.sleep(20)
			driver.refresh()
			continue
		pst = st
		while True:
			try:
				el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[2]/span')
				break;
			except NoSuchElementException:
				print("still no element, let us refresh a bit")
				driver.refresh()
				time.sleep(5)
				continue
		

			
		st = st + ', ' + el.text + '\n' # new el.text gives band's name
		st = st.lower()
		file_ob = open("songs.txt", "r+")
		st_lines = file_ob.readlines()
		file_ob.close()
		print(st)
		#print(st_lines)
		print(st in st_lines)
		if st not in st_lines:
			file_ob = open("songs.txt", "a+")
			file_ob.write(st )
			file_ob.close()

		time.sleep(60)
		driver.refresh()
		time.sleep(5)
	driver.close()
if __name__ == '__main__':
	os.system("pactl set-sink-mute 0 1")
	#print( os.system('sudo osascript -e "set Volume 0"'))
	main_loop()


