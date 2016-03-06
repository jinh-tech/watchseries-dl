import urllib, sys, re, os

host = "thewatchseries.to"

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