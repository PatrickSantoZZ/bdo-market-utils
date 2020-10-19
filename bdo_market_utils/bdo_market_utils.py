import market_scraper
import market_analyzer

scrape_and_save("marketplace_items.json", "current_marketplace.csv")
analyze("current_marketplace.csv", "items_of_interest.csv")

