# for holiday_calendar
import pandas as pd
from business_calendar import Calendar, MO, TU, WE, TH, FR
# import from py_holiday_calendar
from py_holiday_calendar import py_holiday_calendar as check

df = {
    'day': ['1/1/2018', '4/8/2019', '12/13/2019', '1/2/2019'],
    'temp': [44, 45, 87, 66],
    'str': ['GSIB', 'Data', 'GSIB', 'data'],
    'drake': ['eminem', 'marshall', 'drogon', 'eminem'],
    'day1': ['1/5/2018', '4/12/2019', '12/31/2019', '1/8/2019'],
}
df = pd.DataFrame(df)

df['day'] = pd.to_datetime(df['day'])
df['day1'] = pd.to_datetime(df['day1'])
print(df.dtypes)

# have to initialise obj_cal for calendar project
check.calc_diff_with_holidays(df, 'day', 'day1', 'new_date')
print(df)

check.add_bus_days_with_holidays(df, 'day', 'temp', 1)
print(df)
