from scrape import SiteData
import json
from scrape_events import event_to_dict, get_events



# ----- Gym Percentage Data -----
# Make Class instance of how full the gym is
gym_percents = SiteData(
    "https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7",
    "circleChart",
    'class_name',
    'Gym-Availability-Percentage')

gym_list = [
    'Marino Center - 2nd Floor',
    'Marino Center - Gymnasium',
    'Marino Center - 3rd Floor Weight Room',
    'Marino Center - 3rd Floor Select & Cardio',
    'Marino Center - Track',
    'SquashBusters - 4th Floor']

# Creates dictionary with name of component of gym as key, and an integer representing percent full as value.
percent_list = [int(percent.text[0:-1]) for percent in gym_percents.scrape_site()]

# Add the data to the class
setattr(gym_percents, "data", dict(zip(gym_list, percent_list)))


# ----- Operating Hour Data -----
# Make instance of the hours of operation of the gym
operating_hours_days = SiteData(
    "https://www.northeastern.edu/campusrec/",
    "/html/body/section[2]/div/header/table/tbody/tr/th[1]/p[2]",
    'xpath',
    'operating-hours')

# Turns string into single item list.
days_hours = [item.text for item in operating_hours_days.scrape_site()]
days_hours = days_hours[0].split('\n')

# Create separate lists of dates and times.
open_date = [elem.split(': ')[0] for elem in days_hours]
open_date = [elem.split(', ')[1] for elem in open_date]
open_hours = [elem.split(': ')[1] for elem in days_hours]

# Add data to instance
setattr(operating_hours_days, "data", dict(zip(open_date, open_hours)))


# Combines dict of open hours and dict of percent full values into one list.
marino_info = {gym_percents.title: gym_percents.data, operating_hours_days.title: operating_hours_days.data}


# event links
event_links = {
    'Court 2': 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=8dCpAXZOtNUwCu7Xw7lFdvnMLXWJvC%2fXnljDAys%2fqmQx5OHc0kgRwku22rLLnqz9V187%2fQc5LcOubs4EolABUmZFwTbc8EyCREjolwr1Ekq69xl3QSidow%3d%3d#dailyContainer',
    'Court 3': 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=pw7uNs6e9v8qbfdIsvc5fDYq1MFunilYcWUxDMrP56yKqAjIwwaKA11U%2fQckiFjB2tWbX%2fc8606fDHS3t5PPuSnrcoE8cTQGmAOsO4wdf4ZaUfDtNt1OGQ%3d%3d',
    'Sports Court': 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=2sdeuuZ3cxh0hVZgJYA84txwBAjutRyjhYavKNQt%2f1ZU02OX1qeFfxh8QvnmqjnnvPoiPyTnIl8ZtHpxkgfPUK6dvglR7G8DdxFP69QIaS4hyDGPHot7LbGnj5jMFpqD'
}
event_out = {}
for key in event_links:

    event_out[key] = event_to_dict(get_events(event_links[key]))


# add events
marino_info["Events"] = event_out

# puts whole list of dict in json
with open("gym_percents.json", "w") as outfile:
    json.dump(marino_info, outfile, indent=2, sort_keys=True)
