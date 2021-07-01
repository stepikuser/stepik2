import pytest
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_link_on_the_main_page(browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.btn-add-to-basket")
