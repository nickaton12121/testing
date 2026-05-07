from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage
import time

def test_open_s6(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_galaxy_s6()
    
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')
    
    
def test_two_monitors(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_monitor_category()
    time.sleep(2)
    home_page.check_products_count(2)
    