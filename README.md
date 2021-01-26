# bdo-market-utils


Collect data from Black Desert Online's marketplace and analyze it too!  
Note: I've kinda dropped this project bc I stopped playing Black Desert Online. Feel free to use it tho, whoever's out there.

## Features
- Prices from `market.blackdesertonline.com` API
- Dump item data to CSV
- Analyzer to find items of interest (and why)
- Soon to be unit tested with Pytest/unittest! (if you care) (also if I can get the package structure correct)
- Note: Does not have item IDs for Hashinshin gear (yet)

## Credentials for API calls
You can use the developer tools in your browser to look at network requests.

1. Go to https://market.blackdesertonline.com/ and sign in
2. Open `Developer Tools` for your browser and select `Network`.
    - Usually you can just press F12 to open this up. Otherwise, see below
    - For Chrome it's `Ctrl+Shift+I` and click `Network` tab.
    - For Firefox it's `Ctrl+Shift+E` to open `Network` tab.
3. Click on any item, then click on "See Details" button
4. You'll see GetItemSellBuyInfo and/or GetWorldMarketSubList. Click on either one
5. In Headers, you'll want the following information:
    - `cookie` is found in ` Request Headers` under `Cookie` -> `__RequestVerificationToken`.
    - `token` is found in `Form Data` under `__RequestVerificationToken`.

## Usage
1. Configure config.py
```
{
    "input": "filename with list of items to get prices for",
    "output": "filename of where to dump CSV data",
    "cookie": "__RequestVerificationToken obtained from session",
    "token": "__RequestVerificationToken obtained from making a request",
    "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "url": "regional URL"
}
```
2. Get a CSV dump of everything in the market, or selected items
```
cd src
python market_scraper.py
```
You'll get something like this:
```
ID, Name, Category, Sub-Category, Enhancement, Grade, Price, Trades, Stock, History(89 days), Bid-Ask Spread
206, Flashbang, Consumables, Siege Items, +0, 0, 90000, 6830, 0, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 90000, 15/0/83500, 10/0/84000, 0/0/84500, 0/0/85000, 0/0/85500, 0/0/86000, 2/0/86500, 0/0/87000, 0/0/87500, 0/0/88000, 0/0/88500, 5/0/89000, 10/0/89500, 844/0/90000,
207, Fire Shot, Consumables, Siege Items, +0, 0, 70000, 20411, 73, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66500, 66500, 66500, 66500, 66500, 66500, 66500, 66500, 66500, 66500, 66500, 66500, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 66000, 65000, 65000, 65000, 66500, 66500, 66500, 66500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68500, 68000, 68000, 68000, 68000, 70000, 70000, 0/0/65000, 0/0/65500, 0/0/66000, 0/0/66500, 0/0/67000, 0/0/67500, 0/0/68000, 0/0/68500, 0/0/69000, 0/0/69500, 0/0/70000, 0/39/70500, 0/34/71000, 0/0/71500, 0/0/72000, 0/0/72500, 0/0/73000, 0/0/73500, 0/0/74000, 0/0/74500, 0/0/75000,
208, Poison Shot, Consumables, Siege Items, +0, 0, 61000, 678, 0, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 61000, 0/0/56500, 0/0/57000, 0/0/57500, 0/0/58000, 0/0/58500, 1/0/59000, 0/0/59500, 0/0/60000, 0/0/60500, 309/0/61000,
212, Capturing Rope, Material, Misc., +0, 0, 1580, 1038360, 427, 1560, 1560, 1610, 1580, 1580, 1640, 1640, 1590, 1570, 1630, 1600, 1630, 1640, 1640, 1550, 1650, 1630, 1640, 1510, 1360, 1160, 1330, 1170, 1210, 1160, 1080, 990, 990, 1100, 1030, 1030, 1110, 1170, 1250, 1290, 1290, 1110, 1130, 1130, 1000, 1000, 1010, 1030, 1030, 1070, 1100, 1170, 1080, 1080, 885, 955, 945, 1010, 1090, 1020, 950, 900, 880, 1040, 1190, 1100, 1070, 955, 970, 875, 930, 995, 995, 1040, 1080, 1080, 1050, 1110, 1180, 1180, 1310, 1300, 1320, 1380, 1620, 1620, 1450, 1450, 1240, 1370, 1370, 1570, 1470, 1430, 0/112/1470, 0/0/1480, 0/0/1490, 0/0/1500, 0/0/1510, 0/0/1520, 0/0/1530, 0/0/1540, 0/0/1550, 0/0/1560, 0/0/1570, 0/8/1580, 0/0/1590, 0/1/1600, 0/2/1610, 0/90/1620, 0/4/1630, 0/2/1640, 0/208/1650,
```
3. Take the CSV dump and analyze it with my basic analyzer, or do whatever you want with the data.
```
python market_analzyer.py current_marketplace.csv
```
