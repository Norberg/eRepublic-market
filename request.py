from xml.dom.minidom import parse
import urllib2
req = urllib2.urlopen("http://api.erepublik.com/v2/feeds/market/7/38/")
xml = parse(req)
