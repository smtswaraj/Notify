from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = ".\img\coronavirus-gd22081992_640.ico",
        timeout = 15
    )


def getData(url):
    r = requests.get(url)
    return r.text



if __name__ == '__main__':
    notifyme("swaraj","hello")

