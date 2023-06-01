import requests
import datetime as dt
import time
import pandas as pd

if __name__ == '__main__':
    print('init params')

    # init DataFrame
    df = pd.DataFrame(columns=['Time', 'URL', 'Return'])

    # init count
    count = 0

    # init URL
    target_url = 'https://www.youtube.com'

    print('ready for logging')

    while True:
        # init date
        date = dt.datetime.now()

        time.sleep(1)
        # call target_url and append DataFrame
        df.loc[count] = [dt.datetime.now(), target_url, requests.get(target_url)]

        if '200' not in str(df.loc[count, 'Return']):
            print('200 is not exist')
            print(df)

        count += 1

        if date.minute == 59:
            if dt.datetime.now().month < 10:
                filename = str(date.year) + '-0' + str(date.month) + '-' + str(date.day) + '-' + str(date.hour) + ".csv"
            else:
                filename = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '-' + str(date.hour) + ".csv"

            df.to_csv(filename, mode='w')
