from my_web_scraper.scraper import Scraper
from my_web_scraper.parser import Parser
from my_web_scraper.data_storage import DataStorage

# Create an instance of the Scraper class
scraper = Scraper("https://www.who.int/covid-19/")

# Get the HTML from the website
html = scraper.get_html()

# Create an instance of the Parser class
parser = Parser(html)

# Extract the data from the HTML
data = parser.get_data()

# Create an instance of the DataStorage class (This example is using covid-19 data)
data_storage = DataStorage(data, "covid19_data.csv")

# Save the data to a CSV file
data_storage.to_csv()
