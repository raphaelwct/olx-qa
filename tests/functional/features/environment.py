# -*- coding: utf-8 -*-
from selenium import webdriver

BEHAVE_DEBUG_ON_ERROR = False


def before_all(context):
    # appium_URL = 'http://www.google.com.br'
    # desired_caps = {}
    # desired_caps['testdroid_username'] = 'ville-veikko.helppi@bitbar.com'
    # desired_caps['testdroid_password'] = 'xxxxxxxx'
    # desired_caps['testdroid_target'] = 'chrome'
    # desired_caps['testdroid_project'] = 'Appium Chrome'
    # desired_caps['testdroid_testrun'] = 'TestRun 1'
    # desired_caps['testdroid_device'] = 'Asus Google Nexus 7 (2013) ME571KL'
    # desired_caps['platformName'] = 'android'
    # desired_caps['deviceName'] = 'AndroidDevice'
    # desired_caps['browserName'] = 'chrome'
    # driver = webdriver.Remote(appium_URL, desired_caps)
    browser = webdriver.Firefox()
    browser.implicitly_wait(7)
    context.browser = browser


def after_all(context):
    context.browser.close()


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)
