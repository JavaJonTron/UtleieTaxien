from datetime import datetime
# Not testable due to having to use the same code for test

month = int(datetime.today().strftime('%m')) - 1
year = int(datetime.today().strftime('%Y')) - 1900
day = int(datetime.today().strftime('%d'))
