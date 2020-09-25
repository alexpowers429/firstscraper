import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=45.03637000000003&lon=-93.38501999999994#.X24bGZNKg-Q')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')
# print(week)

items = (week.find_all(class_='tombstone-container'))
# print(items[0])

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

##list comprehension 
## write a for loop that will access all of the different classes and grab their data as text using .get_text()
period_names = [item.find(class_="period-name").get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
# print(period_names)
# print(short_descriptions)
# print(temperatures)

##pandas is an easier way to get data into a table than coding CSV files, inside of the object in quotes we have the column title, to its right is the data that will be loaded in as a result

weather_data = pd.DataFrame(
    {'period': period_names,
     'short_descriptions': short_descriptions,
     'temperatures': temperatures
     }
)

print(weather_data)


#panda lets you turn data into csv file
weather_data.to_csv('weatherdata.csv')