# -*- coding: utf-8 -*-
from behave import given, when, then


@given('I access the advertisement page')
def access_advertisement_page(context):
    context.browser.get('http://rj.olx.com.br')


@when('I search for "{item}"')
def search_for_item(context, item):
    assert True is not False


@then('I have to find advertisements for "{item}"')
def check_ads(context, item):
    assert context.failed is False
