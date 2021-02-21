from time import sleep
from notification_manager import NotificationManager
from search_manager import ApartmentHuntBot


bot = ApartmentHuntBot()
notification = NotificationManager()

bot.search_input()
sleep(5)

bot.get_search_results()

bot.driver.quit()
