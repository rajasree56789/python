from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
def wait(func):
    def wrapper(*args,**kwargs):
        instance,locator=args
        w=WebDriverWait(instance.driver,10)
        v=visibility_of_element_located(locator)
        w.until(v)
        return func(*args,**kwargs)
    return wrapper
def wait_cls(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key!="__init__":
            setattr(cls,key,wait(value))
    return cls
@wait_cls
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    def enter_element(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)
        self.driver.find_element(*locator).clear()
