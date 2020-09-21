import pandas as pd
import datetime
from business_calendar import Calendar, MO, TU, WE, TH, FR


# obj_cal = Calendar(workdays=[MO, TU, WE, TH, FR], holidays=[])

def _initialise_cal_obj(workdays, holidays=[]):
    """Function to initialise custom calendar object.

    The return value must be the custom calendr object.

    Parameters
    ----------
    workdays
        List of custom workdays.
    holidays
        List of custom holidays.

    Returns
    -------
    Object
        Custom calendar object.

    """
    obj_cal = Calendar(workdays=workdays, holidays=holidays)
    return obj_cal


def calc_diff_with_holidays(df, start, end, new_col, workdays=[MO, TU, WE, TH, FR], holidays=[]):
    """Calculate difference between pandas df columns adjusting for custom bus and holidays. Start date is not included.

    The return type will be the pandas dataframe.

    Parameters
    ----------
    df
        The pandas dataframe to work on.
    start
        Start Date column in the df.
    end
        End Date column in the df.
    new_col
        New column to be generated containing the difference.
    workdays
        List of custom workdays.
    holidays
        List of custom holidays.

    Returns
    -------
    Dataframe
        Modified dataframe with new_col for difference between dates.

    """
    # Cast to datetime if not already
    df[start] = pd.to_datetime(df[start])
    df[end] = pd.to_datetime(df[end])
    obj_cal = _initialise_cal_obj(workdays, holidays)
    df[new_col] = 0
    # iterate over the cols
    for i in range(df.shape[0]):
        df.at[i, new_col] = obj_cal.busdaycount(df[start][i], df[end][i])
    return df


def add_bus_days_with_holidays(df, col_op, col_res, days, workdays=[MO, TU, WE, TH, FR], holidays=[]):
    """Add business days to a column in pandas dataframe (holidays can be considered).

    The return type must be the modified df containing a new column with the result after adding business days.

    Parameters
    ----------
    df
        The pandas dataframe to work on.
    col_op
        Column with dates to add bus days to.
    col_res
        New col with the modified dates.
    days
        Number of business days to add.
    workdays
        List of custom workdays.
    holidays
        List of custom holidays.

    Returns
    -------
    Dataframe
        Modified dataframe with new_col containg new business dates.

    """
    # Cast to datetime if not already
    df[col_op] = pd.to_datetime(df[col_op])
    obj_cal = _initialise_cal_obj(workdays, holidays)
    df[col_res] = df[col_op].apply(lambda x: obj_cal.addbusdays(x, days))
    return df


def add_bus_days(df, col_op, col_res, days, workdays=[MO, TU, WE, TH, FR]):
    """Add business days to a column in pandas dataframe (to consider holidays, use the method with holidays).

    The return type must be the modified df containing a new col with the results after adding provided business days.

    Parameters
    ----------
    df
        The pandas dataframe to work on.
    col_op
        Column with dates to add bus days to.
    col_res
        New col with the modified dates.
    days
        Number of business days to add.
    workdays
        List of custom workdays.

    Returns
    -------
    Dataframe
        Modified dataframe with new_col containg new business dates.

    """
    # Cast to datetime if not already
    df[col_op] = pd.to_datetime(df[col_op])
    obj_cal = _initialise_cal_obj(workdays)
    df[col_res] = df[col_op].apply(lambda x: obj_cal.addworkdays(x, days))
    return df


def calc_workday_diff(df, start, end, new_col, workdays=[MO, TU, WE, TH, FR]):
    """Calculate difference between(to consider holidays as well, use the other method). Start Date not included.

    The return type must be the modified df containing a new column with the diff result.

    Parameters
    ----------
    df
        The pandas dataframe to work on.
    start
        Start Date column in the df.
    end
        End Date column in the df.
    new_col
        New column containing the diff between the date cols provided.
    workdays
        List of custom workdays.

    Returns
    -------
    Dataframe
        Modified dataframe with new_col containing dif between business dates among provided cols.

    """
    # Cast to datetime if not already
    df[start] = pd.to_datetime(df[start])
    df[end] = pd.to_datetime(df[end])
    obj_cal = _initialise_cal_obj(workdays)
    df[new_col] = 0
    # iterate over the cols
    for i in range(df.shape[0]):
        df.at[i, new_col] = obj_cal.workdaycount(df[start][i], df[end][i])
    return df
