# -*- coding: utf-8 -*-
from page_objects import PageObject, page_element, MultiPageElement


class Search(PageObject):
    search_field = page_element(id_='searchtext')
    search_button = page_element(id_='searchbutton')
    ads = MultiPageElement(xpath="//ul[@id='main-ad-list']//li")
    section_not_found = page_element(xpath="//div[@class='section_not-found']")
    not_found_msg_box = page_element(xpath="//div[@class='section_not-found']//h3[@class='subtitle mb5px']")
