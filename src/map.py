import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

step = ['V&A Museum','London','England','United Kingdom','Europe','Japan','Honshu','Tokyo','Tokyo Olympic Stadium']	# locations to go through

driver = webdriver.Chrome()  			# Optional argument, if not specified will search paths in etc/paths.
driver.implicitly_wait(20) 				# max seconds to wait for the element to be loaded

driver.get('https://goo.gl/V4uV5P')		# open V&A inside street view
time.sleep(3)

driver.get('https://goo.gl/9L8DqQ') 	# open Google Maps at V&A location - start
time.sleep(3)

search_box = driver.find_element_by_name('q')	# create element for the serach field in Google Maps

for i in range(len(step)):				# loop that searches for each location in steps[]
	print(step[i])

	search_box.clear()
	search_box.send_keys(step[i])		# 'writes' the location to the search box
	search_box.send_keys(Keys.RETURN)	# 'presses' return

	time.sleep(5) 						# wait for X seconds so we can see something

sidepanel = driver.find_element_by_xpath('//*[@id="pane"]/div/div[3]/button')
sidepanel.click()						# hide the side panel
time.sleep(5)

maptype = driver.find_element_by_xpath('//*[@id="minimap"]/div/div[2]/button')
maptype.click()							# switch map/earth view
time.sleep(5)

tilt = driver.find_element_by_xpath('//*[@id="tilt"]/div/button')
tilt.click()							# go to 3D mode
time.sleep(3)

for i in range(4):						# pan around - 4 x 90 degrees
	cwpan = driver.find_element_by_xpath('//*[@id="compass"]/div/button[2]')
	cwpan.click()
	time.sleep(3) 

'''
i = 1

while i <= 3:

	canvas = driver.find_element_by_xpath('//*[@id="scene"]/div[3]/canvas')
	print(canvas)

	time.sleep(3)
	global i
	i = i + 1

while i >= 0:
	zoomout = driver.find_element_by_xpath('//*[@id="zoom"]/div/button[2]')
	zoomout.click()
	time.sleep(3)
	global i
	i = i - 1

zoomin = driver.find_element_by_xpath('//*[@id="zoom"]/div/button[1]')
zoomin.click()

maptype = driver.find_element_by_xpath('//*[@id="minimap"]/div/div[2]/button')
maptype.click()		#switch map/earth 

time.sleep(3) # Let the user actually see something!

search_box.submit()
driver.quit()

'''
