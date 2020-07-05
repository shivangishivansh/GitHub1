from selenium import webdriver
from Library import Config_Reader

def startbrowser():
    global driver
    if Config_Reader.Readconfigdata("Environment", "Browser") == "Chrome":
        driver = webdriver.Chrome(executable_path="C:/Pycharm/Driver/chromedriver.exe")
    elif Config_Reader.Readconfigdata("Environment", "Browser") == "Firefox":
        driver = webdriver.Firefox(executable_path="C:\Pycharm\Driver\geckodriver.exe")
    driver.maximize_window()
    driver.get(Config_Reader.Readconfigdata("Environment", "URL"))
    return driver

def closebrowser():
    driver.close()
    driver.quit()