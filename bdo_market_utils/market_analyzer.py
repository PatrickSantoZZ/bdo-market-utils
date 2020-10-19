from helpers import print_progress_bar, append_with_comma
from config import *

class ItemInfo:
    itemID = ""
    name = ""
    category = ""
    subcategory = ""
    enhancement_level = ""
    grade = ""
    price = ""
    trades = ""
    stock = ""
    history = []
    bid_ask_spread = []
    minimum = 0
    maximum = 0
    average1 = 0            # Average from between 90 days ago and 60 days ago
    average2 = 0            # Average from between 60 days ago and 30 days ago
    average3 = 0            # Average from between 30 days ago and now
    moving_averages = []    # Moving 7 day averages
    reason = ""

    def __init__(self, csv):
        self.set_all(csv)

    # Setters
    def set_all(self, csv):
        self.set_itemID(csv[0])
        self.set_name(csv[1])
        self.set_category(csv[2])
        self.set_subcategory(csv[3])
        self.set_price(csv[6])
        self.set_trades(csv[7])
        self.set_enhancement_level(csv[4])
        self.set_stock(csv[8])
        self.set_grade(csv[5])
        history = []
        bid_ask_spread = []
        for value in csv[9:-1]:
            if '/' in value:
                bid_ask_spread.append(value)
            else:
                history.append(int(value))
        self.set_history(history)
        self.set_minimum(min(history))
        self.set_maximum(max(history))
        self.set_average1(average(history[:30]))
        self.set_average2(average(history[30:60]))
        self.set_average3(average(history[60:]))
        self.set_moving_averages(moving_averages(history))
        self.set_bid_ask_spread(bid_ask_spread)

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
        self.history = history

    def set_bid_ask_spread(self, bid_ask_spread):
        self.bid_ask_spread = bid_ask_spread

    def set_minimum(self, minimum):
        self.minimum = minimum

    def set_maximum(self, maximum):
        self.maximum = maximum

    def set_average1(self, avg):
        self.average1 = avg

    def set_average2(self, avg):
        self.average2 = avg

    def set_average3(self, avg):
        self.average3 = avg

    def set_reason(self, reason):
        self.reason = reason

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

    def get_minimum(self):
        return self.minimum

    def get_maximum(self):
        return self.maximum

    def get_average1(self):
        return self.average1

    def get_average2(self):
        return self.average2

    def get_average3(self):
        return self.average3

    def get_reason(self):
        return self.reason

    def to_csv(self):
        csv_line = self.get_itemID()
        csv_line = append_with_comma(csv_line, self.get_name())
        csv_line = append_with_comma(csv_line, self.get_category())
        csv_line = append_with_comma(csv_line, self.get_subcategory())
        csv_line = append_with_comma(csv_line, self.get_enhancement_level())
        csv_line = append_with_comma(csv_line, self.get_grade())
        csv_line = append_with_comma(csv_line, self.get_price())
        csv_line = append_with_comma(csv_line, self.get_trades())
        csv_line = append_with_comma(csv_line, self.get_stock())
        csv_line = append_with_comma(csv_line, self.get_minimum())
        csv_line = append_with_comma(csv_line, self.get_maximum())
        csv_line = append_with_comma(csv_line, self.get_reason())
        return csv_line

def average(numbers):
    return sum(numbers)/len(numbers)

def moving_averages(numbers):
    averages = []
    for i in range(7, len(numbers)):
        averages.append(average(numbers[i-7:i]))
    return averages

def get_trends(moving_averages):
    last_avg = moving_averages[0]
    trends = []
    trend = 0
    min_trend = 0
    max_trend = 0

    for avg in moving_averages:
        if avg > last_avg:
            if trend > 0:
                trend += 1
            else:
                trends.append(trend)
                trend = 1
        elif avg < last_avg:
            if trend < 0:
                trend -= 1
            else:
                trends.append(trend)
                trend = -1
        else:
            trends.append(trend)
            trend = 0
        if trend > max_trend:
            max_trend = trend
        if trend < min_trend:
            min_trend = trend
        if trend >= 3:
            print("increasing")
            return
        if trend <= -3:
            print("decreasing")
            return


    trends_without_zero = list(filter((0).__ne__, trends))
        last_avg = avg
    trends_text += "Fluctuates a lot. "
    trends_text += "On the down. "
    trends_text += "On the up. "
    trends_text += "Used to be high. "
    trends_text += "Used to be low. "
    trends_text += "Steady. "
    trends_text += ""
    return trends

def is_rising(trends):
    back_trend = trends[::-1]
    trend = 0
    for i in back_trend:
        if i == 0:
            pass
        elif i > 0 and trend >= 0:
            trend += 1
        elif i < 0 and trend <= 0:
            trend -= 1



def analyze(inputfile, outputfile):
    items_of_interest = []
    with open(inputfile) as f:
        f.readline()
        for i in f:
            item_info = ItemInfo(i.split(", "))
            if item_info.get_minimum() == 0:
                item_info.set_reason("New item. "
                                     "May want to keep tabs on the price of "
                                     "this item until price settles.")
                items_of_interest.append(item_info)
            elif get_trends(item_info.get_moving_averages())[-1] < -3:
                item_info.set_reason("Item price is dropping")
            elif get_trends(item_info.get_moving_averages())[-1] > 3:
                item_info.set_reason("Item price is rising")
            elif int(item_info.get_price()) > (item_info.get_average1() * 1.25):
                item_info.set_reason("Item is at a higher price than normal.")
                items_of_interest.append(item_info)
            elif int(item_info.get_price()) < (item_info.get_average1() * .75):
                item_info.set_reason("Item is at a lower price than normal.")
                items_of_interest.append(item_info)

    with open(outputfile, 'w') as f:
        f.write("ID, Name, Category, Subcategory, Enhancement, Grade, Price"
                ", Total Trades, Stock, Minimum, Maximum, Reason\r\n")
        for item in items_of_interest:
            f.write(item.to_csv() + '\r\n')

if __name__ == "__main__":
    analyze(ITEMPRICESFILE, ITEMANALYSISFILE)

