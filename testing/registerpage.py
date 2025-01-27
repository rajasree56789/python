from generic import SeleniumWrapper
class RegisterPage:
    def __init__(self,driver):
        self.driver=driver
    def register(self,firstname,lastname,email,password,confirmpassword):
        s=SeleniumWrapper(self.driver)
        s.click_element(("id","gender-female"))
        s.enter_element(("id","FirstName"),value=firstname)
        s.enter_element(("id", "LastName"), value=lastname)
        s.enter_element(("id", "Email"), value=email)
        s.enter_element(("name","Password"),value=password)
        s.enter_element(("name","ConfirmPassword"),value=confirmpassword)
        s.click_element(("xpath","//input[@value='Register']"))