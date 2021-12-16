from Scrape_Percentages import scrape_site

# Test file

#  Xpaths from court 2
# '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[1]',
# '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[2]',
# '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[3]',
# '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[4]',
# '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[5]'

court_2 = scrape_site(
    'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=8dCpAXZOtNUwCu7Xw7lFdvnMLXWJvC%2fXnljDAys%2fqmQx5OHc0kgRwku22rLLnqz9V187%2fQc5LcOubs4EolABUmZFwTbc8EyCREjolwr1Ekq69xl3QSidow%3d%3d',
    'ellipsis',
    'class_name')

print(court_2)
for x in court_2:
    print(x.text)