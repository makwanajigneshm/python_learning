import sys
from lxml import html
import requests,bs4
#Redirect output to the file
sys.stdout = open('D:\\Users\\jmakwana\\Documents\\myscript\\episode_list.txt', 'w')
#Open the web page
page = requests.get('http://apne.tv/Hindi-Serial/episodes/Sher-E-Punjab-Maharaja-Ranjit-Singh')
#BeautifulSoup parser 
Sp=bs4.BeautifulSoup(page.content,'html.parser')
# Iterate thrue each  unsorted list where class is matching to below value.
#There we have the episode list. As we want the first episode only, we are breaking the loops
for ultag in Sp.find_all('ul',{"class":"episodes_list limited_episode moblie_episode"}):
	for iltag in ultag.find_all('li'):
		for atag in iltag.find_all('a'):
			EpURL=atag.get('href')
			break
		break
	break
print('Done Extracing URL ')
print('					  '  + EpURL)
print('					  ')
#Now we have the URL for the specifc episodes, we will iterate thrue and find out all the links to videos 
page = requests.get(EpURL) 
Sp=bs4.BeautifulSoup(page.content,'html.parser')
for ultag in Sp.find_all('div',{"class":"channel_cont"}):
	for iltag in ultag.find_all('li'):
		for atag in iltag.find_all('a'):
			print(atag.get('href'))
			EpURL=atag.get('href')
print('					  ')
print('					  ')
print('Done Extracing URLs ')
