from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from pytest import fixture
@fixture
def setup_and_teardown():
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=opt)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.close()








