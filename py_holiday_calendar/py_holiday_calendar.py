import pandas as pd
import datetime
from business_calendar import Calendar, MO, TU, WE, TH, FR


# obj_cal = Calendar(workdays=[MO, TU, WE, TH, FR], holidays=[])

def _initialise_cal_obj(workdays, holidays):
    obj_cal = Calendar(workdays=workdays, holidays=holidays)
    return obj_cal


def calc_diff_with_holidays(df, start, end, new_col, workdays=[MO, TU, WE, TH, FR], holidays=[]):
    obj_cal = _initialise_cal_obj(workdays, holidays)
    df[new_col] = 0
    # iterate over the cols
    for i in range(df.shape[0]):
        df.at[i, new_col] = obj_cal.busdaycount(df[start][i], df[end][i])
    return df


def add_bus_days_with_holidays(df, col_op, col_res, days, workdays=[MO, TU, WE, TH, FR], holidays=[]):
    obj_cal = _initialise_cal_obj(workdays, holidays)
    df[col_res] = df[col_op].apply(lambda x: obj_cal.addbusdays(x, days))
    return df
