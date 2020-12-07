from first_scraper.scraper_1 import first_data
from second_scraper.scraper_2 import second_data
import datetime
import time

while True:
    # city = input("Enter: ")
    city = "Minsk"
    data1 = first_data(city)
    data2 = second_data(city)
    now = datetime.datetime.now()

    if type(data1) is str and type(data2) is str:
        print(data1)
        exit()
    else:
        print("Time: %s" % (now.strftime("%Y-%m-%d %H:%M:%S")))
        for key, value in first_data(city).items():
            print(f'{key}: {value}', end='\t')
        print()
        for key, value in second_data(city).items():
            print(f'{key}: {value}', end='\t')
        print()
        time.sleep(60)
