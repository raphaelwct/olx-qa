# -*- coding: utf-8 -*-
from behave import given, when, then


@given('I access the advertisement page')
def access_advertisement_page(context):
    context.browser.get('http://rj.olx.com.br')


@when('I search for "{item}"')
def search_for_item(context, item):
    search_field = context.browser.find_element_by_id('searchtext')
    search_field.send_keys(item)
    search_button = context.browser.find_element_by_id('searchbutton')
    search_button.click()


@then('I have to find advertisements for "{item}"')
def check_ads(context, item):
    ads = context.browser.find_elements_by_xpath("//ul[@id='main-ad-list']//li")
    assert len(ads) > 2
