import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrom_driver_path = "C:\selenium\chromedriver.exe"

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

my_address_mail = "deborah270401@gmail.com"
my_passwd = "deborah"
my_account = "Deborah Shoshana"


def test_open_website():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    # driver.get('https://www.google.com')
    driver.get('http://automationpractice.com/index.php')
    driver.quit()


def test_login():
    # test Email input
    if not isinstance(my_address_mail, str):
        raise TypeError("the address email must to be a string , try again !")
    # test Password input
    if not isinstance(my_passwd, str):
        raise TypeError("error!! the password must to be a string , try again !")

    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.CLASS_NAME, "login").click()
    driver.find_element(By.ID, "email").send_keys(my_address_mail)
    driver.find_element(By.ID, "passwd").send_keys(my_passwd)
    driver.find_element(By.ID, 'SubmitLogin').click()
    driver.quit()




def test_find_cheapest_item_in_summer():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')


    # login into the site
    log.info("login into the site")
    driver.find_element(By.CLASS_NAME, "login").click()
    driver.find_element(By.ID, "email").send_keys(my_address_mail)
    driver.find_element(By.ID, "passwd").send_keys(my_passwd)
    driver.find_element(By.ID, 'SubmitLogin').click()
    time.sleep(2)
    name_account = driver.find_element(By.CLASS_NAME, "header_user_info")
    assert name_account.text == my_account

    # search summer
    log.info("test of search summer dress")
    search_box = driver.find_element(By.ID, "search_query_top")
    search_box.send_keys("summer")
    search_btn = driver.find_element(By.NAME, "submit_search")
    search_btn.click()
    time.sleep(5)
    search_result_header = driver.find_element(By.CSS_SELECTOR, "#center_column>h1")
    time.sleep(5)
    assert 'SEARCH  "SUMMER"' in search_result_header.text

    # search cheap item in summer
    product_containers = driver.find_elements(By.CLASS_NAME, "product-container")
    min_product_price = 123
    min_product_container = product_containers
    for product_containers in product_containers:
        right_block = product_containers.find_element(By.CLASS_NAME, "right-block")
        content_price = right_block.find_element(By.CLASS_NAME, "content_price")
        price = content_price.find_element(By.CLASS_NAME, "price").text
        num_of_price = float(price[1:len(price)])
        if min_product_price > num_of_price:
            min_product_price = num_of_price
            min_product_container = product_containers
    right_block = min_product_container.find_element(By.CLASS_NAME, "right-block")
    product_name = right_block.find_element(By.CLASS_NAME, "product-name")
    product_name.click()
    time.sleep(5)

    # Completion of an order
    log.info("testing to completion of an order")
    driver.find_element(By.CSS_SELECTOR, "button.exclusive").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, '.button-container a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'a[href="http://automationpractice.com/index.php?controller=order&step=1"]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[name=processAddress]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[type=checkbox]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[name=processCarrier]').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "bankwire").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.button-medium").click()
    time.sleep(2)
    ord_success = driver.find_element(By.CLASS_NAME, "cheque-indent").find_element(By.CLASS_NAME, "dark")
    assert "Your order on My Store is complete." in ord_success.text
    driver.quit()




