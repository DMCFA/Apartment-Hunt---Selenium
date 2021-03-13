from time import sleep
from notification_manager import NotificationManager
from search_manager import ApartmentHuntBot
from data_form import DataForm


bot = ApartmentHuntBot()
notification = NotificationManager()
data = DataForm()

bot.search_input()
sleep(5)

bot.get_search_results()
sleep(5)

data.get_data_fields()
sleep(5)
data.send_data()

bot.driver.quit()
