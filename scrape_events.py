from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# Handling scraping websites with Selenium

# Goes to given link and returns the event info
def get_events(link):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    click1 = driver.find_element(By.XPATH, '//*[@id="browse-tabs"]/li[1]/a')
    click1.click()

    # allow page content to load
    wait = WebDriverWait(driver, 20)

    # check if there is page content
    try:
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[1]')))
        event_results = driver.find_element(By.ID, 'eventResults').text
    except TimeoutException:
        event_results = "No Events Today"

    return event_results


# Handles the data and creation of an Event object
class Event:
    def __init__(self, start_time, end_time, activity, location):
        self.start_time = start_time
        self.end_time = end_time
        self.timezone = "ET"
        self.activity = activity
        self.location = location

    def make_dict(self):
        output_dict = {"Start Time": self.start_time, "End Time": self.end_time, 'Event': self.activity,
                       'Location': self.location}
        return output_dict


# takes outputted list from the website and makes it into a usable dictionary
def event_to_dict(event_results):

    if event_results == "No Events Today":
        return "No Events Today"

    else:
        event_results_list = event_results.splitlines()
        remove_list = ["START TIME", "END TIME", "TIME ZONE", "EVENT NAME", "LOCATION", 'Loading...']
        for delete in remove_list:
            event_results_list.remove(delete)

        # Event_list : List of Event Instances
        event_list = []
        word_list = [elem.split() for elem in event_results_list]

        # Loop through the word list, standardize start time, end time, events, and locations
        for num in range(len(word_list)):
            start_time = " ".join(word_list[num][:2])

            end_slice = word_list[num][:4]
            end_time = " ".join(end_slice[2:])

            activity_slice = word_list[num][5:]
            location = " ".join(activity_slice[-5:])

            # Removing duplicates
            for element in activity_slice[-5:]:
                if element in activity_slice:
                    activity_slice.remove(element)

            activity = " ".join(activity_slice)

            event_list.append(Event(start_time, end_time, activity, location))

            # Convert the event objects into a list containing all data nesessary
            final_event_list = [event.make_dict() for event in event_list]

        return final_event_list



