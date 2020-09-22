Py Holiday Calendar
============================

**py_holiday_calendar** is a Python package containing methods to manipulate date columns of pandas dataframes
adjusting for business days and holidays.

.. image:: https://travis-ci.com/Parasgupta44/py_holiday_calendar.svg?branch=master
    :target: https://travis-ci.com/Parasgupta44/py_holiday_calendar
.. image:: https://img.shields.io/pypi/v/py-holiday-calendar.svg
    :target: https://img.shields.io/pypi/v/py-holiday-calendar
.. image:: https://img.shields.io/pypi/status/py-holiday-calendar.svg
    :target: https://img.shields.io/pypi/status/py-holiday-calendar
.. image:: https://img.shields.io/pypi/format/py-holiday-calendar.svg
    :target: https://img.shields.io/pypi/format/py-holiday-calendar
.. image:: https://img.shields.io/pypi/dw/py-holiday-calendar.svg
    :target: https://img.shields.io/pypi/dw/py-holiday-calendar

Usage
^^^^^^^^^^^^^
Just run the following snippet in your python env and start using the package.

.. code-block:: python

    pip install -v py-holiday-calendar

Docs
^^^^^^^^^^^^^

You can find the docs `here <https://py-holiday-calendar.readthedocs.io/en/latest/>`_.

Example
^^^^^^^

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

To-Dos
^^^^^^^
* Add remaining methods.
* Add the tests.

