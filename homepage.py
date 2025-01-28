from generic import SeleniumWrapper
class HomePge:
    def __init__(self,driver):
        self.driver=driver
    def click_login(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(("link text","Log in"))
    def click_register(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(("link text","Register"))