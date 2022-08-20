import pytest
import re
import time
import logging

from playwright.sync_api import sync_playwright


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

my_address_mail = "deborah270401@gmail.com"
my_passwd = "deborah"
my_account = "Deborah Shoshana"


def test_login():
    if not isinstance(my_address_mail, str):
        raise TypeError("the address email must to be a string , try again !")
    if not isinstance(my_passwd, str):
        raise TypeError("error!! the password must to be a string , try again !!")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        pg = context.new_page()
        pg.goto("http://automationpractice.com/index.php")
        pg.locator("a.login").click()
        time.sleep(2)
        pg.locator("input#email").fill(my_address_mail)
        pg.locator("input#passwd").fill(my_passwd)
        pg.locator("#SubmitLogin").click()
        time.sleep(2)




def test_find_cheapest_item_in_summer(mail=None, passwd=None):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        pg = context.new_page()
        pg.goto("http://automationpractice.com/index.php")
        pg.locator("a.login")
        pg.click()
        time.sleep(2)
        pg.locator("input#email").fill(mail)
        pg.locator("input#passwd").fill(passwd)
        pg.locator("#SubmitLogin")
        pg.click()
        time.sleep(2)
        assert "Welcome to your account" in pg.locator("body").inner_html()
        pg.locator('#search_query_top').fill('summer')
        pg.locator('button.button-search').click()
        header = pg.locator("h1.page-heading:has-text('SUMMER')")
        assert "summer" in header.inner_html()
        products = pg.locator('ul.product_list li')
        prices = pg.locator('ul.product_list li .product-price')
        time.sleep(2)
        prices = []
        for price in prices.all_inner_texts():
            prices.append(re.sub('[^\d\.]', "", price))
        cheap = products.locator(f".product-container:has-text('${(min(prices))}')")
        cheap.hover()
        pg.wait_for_timeout(123)
        cheap.locator("text='Add to cart'").click()
        pg.locator("text='Proceed to checkout'")
        pg.click()
        time.sleep(2)
        pg.locator("#center_column >> text='Proceed to checkout'")
        pg.click()
        pg.locator("button >> text='Proceed to checkout'")
        pg.click()
        pg.locator("input#cgv")
        pg.click()
        pg.locator("button >> text='Proceed to checkout'")
        pg.click()
        total_of_price = pg.locator("#total_product").inner_text()
        assert min(prices) == re.sub('[^\d\.]', "", total_of_price)
        pg.locator("text='Pay by bank wire'")
        pg.click()
        pg.locator("button >> text='I confirm my order'")
        pg.click()
        time.sleep(1)
        assert "The order was successfully completed." in pg.locator('body').inner_html()
