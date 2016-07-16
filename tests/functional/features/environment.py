from selenium import webdriver


def before_all(context):
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    context.browser = browser


def after_all(context):
    context.browser.close()
