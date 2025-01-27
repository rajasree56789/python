from generic import SeleniumWrapper
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
    def login(self,username,password):
        s=SeleniumWrapper(self.driver)
        s.enter_element((("id","Email")),value=username)
        s.enter_element((("id","Password")),value=password)
        s.click_element(("xpath","//input[@value='Log in']"))