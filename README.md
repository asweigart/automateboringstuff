automateboringstuff
===================


This package installs the modules used in "Automate the Boring Stuff with Python", 2nd Edition.

This book, along with all of Al Sweigart's programming books, is freely available under a Creative Commons license at https://inventwithpython.com

The online video course that follows the content of "Automate" can be found at https://inventwithpython.com/automateudemy

You can install this package by running `pip` (or `pip3` on macOS and Linux):

    pip install --user automateboringstuff

You can also run Pip as a Python module by running (use `python3` on macOS and Linux):

    python -m pip install --user automateboringstuff

This will install the following modules:

* `send2trash==1.5.0`
* `requests==2.21.0`
* `beautifulsoup4==4.7.1`
* `selenium==3.141.0`
* `openpyxl==2.6.1`
* `PyPDF2==1.26.0`
* `python-docx==0.8.10`
* `imapclient==2.1.0`
* `twilio`
* `ezgmail`
* `ezsheets`
* `pyinputplus`
* `pillow==6.0.0`
* `pyautogui`

Note About Pyzmail36
===================

This module doesn't install `pyzmail36`. The latest version of Python's `setuptools` module has deprecated some functionality, and trying to install `pyzmail36` with it results in a "use_2to3 is invalid" error message.

To install `pyzmail36`, you need to first install version 58.0.0 of `setuptools` with the following command:

    pip install --user setuptools==58.0.0

Then you can install `pyzmail36`:

    pip install --user pyzmail36==1.0.4

Then you can update `setuptools` to the latest version again:

    pip install --user -U setuptools

I'm currently working with the maintainer of `pyzmail36` to have this issue fixed.
