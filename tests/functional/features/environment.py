# -*- coding: utf-8 -*-
from selenium import webdriver


def before_all(context):
    browser = webdriver.PhantomJS()
    browser.set_window_size(1120, 550)
    browser.implicitly_wait(5)
    context.browser = browser


def after_all(context):
    context.browser.quit()
