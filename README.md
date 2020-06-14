# Bitcoin-Alert-Python-Project

---

A simple Bitcoin Alert python program which sends notifications of bitcoin price whenever the price goes under user provided threshold.

## Project Overview

---

- Program will send notifications on user selected platform.
- four options for choice of platform(Telegram,Twitter,Email and SMS)
- User will receive updates after a user provided time interval.
- User has the option to select which type of currency he wants the price to be.
- User has to select the Threshold below which he wants to receive the alerts.

## Build With

---

- [Python](https://www.python.org/)
- [Coin Market Cap API](https://coinmarketcap.com/api/)
- [IFTTT](https://ifttt.com/join)

## How to Run

---

- Running with default parameters
  Currency-`USD`
  Threshold-`10000`
  Interval-`5`minutes
  Platform-`telegram`

```shell
>python main.py

```

- Running with sser provided parametes

```shell
>python main.py INR 80000 1 Email

```

## Author

---

Vivek Sharma -
