Usage
^^^^^^^^^^^^^
You can provide custom business and holidays list to the methods. The date conversions will happen
according to the python `datetime <https://docs.python.org/3/library/datetime.html>`_.

* For custom business days, use literals MO, TU, WE, TH, FR.
* For custom holidays list, just pass the dates as a list.
* If not provided, by default business days will be considered from Monday to Friday with no Holidays.

