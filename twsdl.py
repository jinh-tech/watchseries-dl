import urllib, sys, re, os, base64
'''----------------------------------------------'''

host = "http://thewatchseries.to"
downloader = "youtube-dl "

'''------------------------------------------------'''

def download_url(page_url):
	
	p_url_file = urllib.urlopen(page_url)
	d_url =[]
	
	for line in p_url_file:
		if re.search('<a target=\"_blank\"  href=\"(/cale.*?)\"',line):
			d_url = re.findall('<a target=\"_blank\"  href=\"(/cale.*?)\"',line)
			break
	
	p_url_file.close()
	d_url = re.findall('\?[a-z]=(.*)$',d_url[0])
	return base64.urlsafe_b64decode(d_url[0])

	
	
'''-----------------------------------------------'''

url = sys.argv[1]
urlfile = urllib.urlopen(url)
urltxt = urlfile.read()
urlfile.close()

episode_names = re.findall('&nbsp;&nbsp;&nbsp;(.*) </span>',urltxt)
episode_urls = re.findall('<a href=\"(/episode/.*html)\"  title=\"Unwatched episode\">',urltxt)

no_episodes = len(episode_names)
for i in xrange(0,no_episodes):
	episode_urls[i] = host + episode_urls[i]
	print  str(no_episodes-i) + ". " + episode_names[i]

print "\nEnter the range (inclusive)"
low = int(raw_input())
high = int(raw_input())


for i in xrange(no_episodes-low,no_episodes-high-1,-1):
	print  "\nDownloading " + str(no_episodes-i) + ". " + episode_names[i]
	cmd = downloader + download_url(episode_urls[i])
	os.system(cmd)

print "\nDownloading finished\n"