import json
import pprint
import re
import requests
import sys
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from config import *
from helpers import *

class Item:
    itemID = ""
    name = ""
    category = ""
    subcategory = ""
    enhancement_level = ""
    grade = ""
    price = ""
    trades = ""
    stock = ""
    history = ""
    bid_ask_spread = ""

    def __init__(self, json):
        self.set_all(json)

    # Setters
    def set_all(self, json):
        self.set_itemID(json['mainKey'])
        self.set_name(json['name'])
        self.set_category(get_main_category(json['mainCategory']))
        self.set_subcategory(get_subcategory(json['mainCategory'], 
                                           json['subCategory']))
        self.set_price(json['pricePerOne'])
        self.set_trades(json['totalTradeCount'])
        self.set_enhancement_level(get_enhancement(json['subKey']))
        self.set_stock(json['count'])
        self.set_grade(json['grade'])

    def set_itemID(self, itemID):
        self.itemID = itemID

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def set_subcategory(self, subcategory):
        self.subcategory = subcategory

    def set_enhancement_level(self, enhancement_level):
        self.enhancement_level = enhancement_level

    def set_grade(self, grade):
        self.grade = grade

    def set_price(self, price):
        self.price = price

    def set_trades(self, trades):
        self.trades = trades

    def set_stock(self, stock):
        self.stock = stock

    def set_history(self, history):
        self.history = self.history_helper(history)

    def set_bid_ask_spread(self, bid_ask_spread):
        self.bid_ask_spread = self.bid_ask_spread_helper(bid_ask_spread)

    # Getters
    def get_itemID(self):
        return self.itemID 

    def get_name(self):
        return self.name 

    def get_category(self):
        return self.category 

    def get_subcategory(self):
        return self.subcategory 

    def get_enhancement_level(self):
        return self.enhancement_level 

    def get_grade(self):
        return self.grade 

    def get_price(self):
        return self.price 

    def get_trades(self):
        return self.trades 

    def get_stock(self):
        return self.stock 

    def get_history(self):
        return self.history

    def get_bid_ask_spread(self):
        return self.bid_ask_spread

    def history_helper(self, history):
        # Regex to join list of prices for past 90 days
        # returns "price1, price2, ..."
        return ", ".join(re.findall(r':(\d+)', history))

    def bid_ask_spread_helper(self, bid_ask_list):
        # Formats bid ask spread to a string of bid/ask/price, ...
        bid_ask_spread = ""
        for price in bid_ask_list:
            bid_ask_spread += str(price['buyCount']) + '/'
            bid_ask_spread += str(price['sellCount']) + '/' 
            bid_ask_spread += str(price['pricePerOne']) + ', '
        return bid_ask_spread

    def to_CSV(self):
        csv_line = self.get_itemID()
        csv_line = append_with_comma(csv_line, self.get_name())
        csv_line = append_with_comma(csv_line, self.get_category())
        csv_line = append_with_comma(csv_line, self.get_subcategory())
        csv_line = append_with_comma(csv_line, self.get_enhancement_level())
        csv_line = append_with_comma(csv_line, self.get_grade())
        csv_line = append_with_comma(csv_line, self.get_price())
        csv_line = append_with_comma(csv_line, self.get_trades())
        csv_line = append_with_comma(csv_line, self.get_stock())
        csv_line = append_with_comma(csv_line, self.get_history())
        csv_line = append_with_comma(csv_line, self.get_bid_ask_spread())
        return csv_line

def get_world_market_sublist(session, i):
    data = dict(DATA)
    data['mainKey'] = i['id']
    result = session.post(MARKETURL, headers=HEADERS, cookies=COOKIES, 
                          data=data, timeout=2)
    return result

def get_item_sell_buy_info(session, item, subkey=0):
    data = dict(DATA)
    data['keyType'] = '0'
    data['mainKey'] = item.get_itemID()
    data['subKey'] = subkey
    data['isUp'] = "true"
    result = session.post(ITEMURL, headers=HEADERS, cookies=COOKIES, 
                          data=data, timeout=2)
    return result

def save(item, file):
    file.write(item.to_CSV() + '\r\n')

def scrape_and_save(session, new_item, file):
    scraped_item = get_world_market_sublist(session, new_item)
    item = Item(scraped_item.json()["detailList"][0])
    if is_enhanceable(scraped_item):
        for i in scraped_item.json()["detailList"]:
            item = Item(i)
            subkey = i['subKey']
            item_sb_info = get_item_sell_buy_info(session, item, subkey=subkey)
            item.set_enhancement_level(get_enhancement(subkey))
            item.set_history(item_sb_info.json()['resultMsg'])
            item.set_bid_ask_spread(item_sb_info.json()['marketConditionList'])
            save(item, file)
    else: 
        item_sb_info = get_item_sell_buy_info(session, item)
        item.set_history(item_sb_info.json()['resultMsg'])
        item.set_bid_ask_spread(item_sb_info.json()['marketConditionList'])
        save(item, file)

def market_scraper(inputfile, outputfile):
    with open(inputfile) as f:
        marketplace_items = json.load(f)

    # POST requests by default do not have a retries parameter in python. 
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    with open(outputfile, "w") as f:
        f.write("ID, Name, Category, Sub-Category, Enhancement, Grade, Price,"\
                " Trades, Stock, History(89 days), Bid-Ask Spread\r\n")
        curr_progress = 0
        print_progress_bar(curr_progress, len(marketplace_items), 
                           prefix='Progress:', suffix='Complete', length=50)
        for item in marketplace_items:
            scrape_and_save(session, item, f)
            curr_progress += 1
            print_progress_bar(curr_progress, len(marketplace_items), 
                               prefix = 'Progress:', suffix = 'Complete', 
                               length = 50)

def is_enhanceable(item):
    if len(item.json()['detailList']) > 1:
        return True
    return False

if __name__ == "__main__":
    market_scraper(ITEMINPUTFILE, ITEMPRICESFILE)
