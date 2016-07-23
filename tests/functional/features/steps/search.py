# -*- coding: utf-8 -*-

from behave import given, when, then
from tests.functional.pages.search import Search

root_uri = 'http://rj.olx.com.br'


@given('I access the advertisement page')
def access_advertisement_page(context):
    context.browser.get('http://rj.olx.com.br')


@when('I search for "{item}"')
def search_for_item(context, item):
    search_page = Search(context.browser)
    search_page.search_field = item
    search_page.search_button.click()


@then('I have to find advertisements for "{item}"')
def check_ads(context, item):
    search_page = Search(context.browser)
    assert len(search_page.ads) >= 1


@then('I dont find advertisements')
def check_no_ads_behave(context):
    search_page = Search(context.browser)

    assert len(search_page.ads) == 0
    assert search_page.section_not_found
    assert search_page.not_found_msg_box.text == u"Nenhum anúncio foi encontrado."
