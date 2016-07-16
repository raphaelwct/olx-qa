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
    assert len(ads) >= 1


@then('I dont find advertisements')
def check_ads(context):
    ads = context.browser.find_elements_by_xpath("//ul[@id='main-ad-list']//li")
    section_not_found = context.browser.find_element_by_xpath("//div[@class='section_not-found']")
    not_found_msg = context.browser.find_element_by_xpath("//div[@class='section_not-found']//h3[@class='subtitle mb5px']")

    assert len(ads) == 0
    assert section_not_found
    assert not_found_msg.text == u"Nenhum anúncio foi encontrado."
