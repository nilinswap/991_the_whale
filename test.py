from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def initial_url():
	driver = webdriver.Safari()
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
		el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[1]')
		st = el.text

		if st == pst:
			time.sleep(10)
			continue
		pst = st
		el = driver.find_element_by_xpath('//*[@id="recently-played"]/div[2]/ul/li[1]/div[2]/div[1]/div[2]/span')
		st = st + ' ' + el.text
		file_ob = open("songs.txt", "a+")
		file_ob.write(st + '\n')
		file_ob.close()
		time.sleep(10)
		driver.refresh()
		time.sleep(5)
if __name__ == '__main__':
	main_loop()


