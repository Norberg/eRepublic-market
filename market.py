import urllib2, datetime, sqlite3
from  xml.etree import ElementTree
MARKETS = {"Food":1, "Weapons":2, "Food_raw":7, "Weapon_raw":12}
CONTRIES = {"Sweden": 38}

def retrive_market_data(country_name, market_name, quality = ""):
	market = MARKETS[market_name]
	country = CONTRIES[country_name]
	print market_name
	print "----------------------------------------"
	req = urllib2.urlopen("http://api.erepublik.com/v2/feeds/market/%s/%s/%s" \
	                       % (market, country, quality))

	tree = ElementTree.parse(req)
	orders = tree.getroot()
	for order in orders.getchildren():
		child = order.getchildren()
		amount = order.find("amount").text
		price = order.find("price").text
		company = order.find("company").text
		print "Company:", company, "Amount:", amount, "Price:", price
		save(country, company, market, quality, amount, price)
	print "\n\n"

def save(country,company, item, quality, amount, price):
	date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	try:
		conn = sqlite3.connect("market.db")
		c = conn.cursor()
		c.execute("INSERT INTO market VALUES(?, ?, ?, ?, ?, ?, ?)",\
	        [date, company, country, item, quality, price, amount])
		conn.commit();
		c.close()
	except Exception as e:
		print "Error:", e

retrive_market_data("Sweden", "Food_raw")
retrive_market_data("Sweden", "Weapon_raw")
retrive_market_data("Sweden", "Food", 1)
retrive_market_data("Sweden", "Food", 2)
retrive_market_data("Sweden", "Weapons", 1)
retrive_market_data("Sweden", "Weapons", 2)
