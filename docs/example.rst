Example
^^^^^^^
A simple snippet showing the use case of the module.

.. code-block:: python

    import pandas as pd
    from py_holiday_calendar import py_holiday_calendar as check

    # Making a dummy dataframe
    df = {
    'day': ['1/1/2018', '4/8/2019', '12/13/2019', '1/2/2019'],
    'temp': [44, 45, 87, 66],
    'str': ['Brake', 'Data', 'Gimp', 'data'],
    'drake': ['eminem', 'marshall', 'drogon', 'eminem'],
    'day1': ['1/5/2018', '4/12/2019', '12/31/2019', '1/8/2019'],
    }
    df = pd.DataFrame(df)

    # Explicitly conveerting the columns to datetime (with which the package works)
    df['day'] = pd.to_datetime(df['day'])
    df['day1'] = pd.to_datetime(df['day1'])

    # Pass in the arguments to cal diff between two date columns
    check.calc_diff_with_holidays(df, 'day', 'day1', 'new_date')
    print(df)

    # Can also pass in custom business days as well as holidays
    check.calc_diff_with_holidays(df, 'day', 'day1', 'new_date', workdays=[MO, TU, WE, TH])
    print(df)

    # Add custom business days to the provided column
    check.add_bus_days_with_holidays(df, 'day', 'temp', 1)
    print(df)
