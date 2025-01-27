from generic import SeleniumWrapper
from pytest import mark
from homepage import HomePge
from registerpage import RegisterPage
# def test_Login(Setup_and_Teardown):
#     s=SeleniumWrapper(Setup_and_Teardown)
#     s.click_element(("link text","Register"))
#     s.click_element(("id","gender-female"))
#     s.enter_element((("id","FirstName")),"raj")
#     s.enter_element((("id","LastName")),"sree")
#     s.enter_element((("id","Email")),"rajasree123@gmail.com")
#     s.enter_element((("id","Password")),"raj@123456")
#     s.enter_element((("id","ConfirmPassword")),"raj@123456")
#     s.click_element(("id","register-button"))
# ___________________________________________________________________________________________________________________
# by using pom class
header="firstname","lastname","email","password","confirmpassword"
data=[("raj","sri","raj@company.com","password@1345","password@1345"),
      ("jahn","sleve","jahn@company.com","password@1234","password@1234")]
@mark.parametrize(header,data)
def test_register(setup_and_teardown,firstname,lastname,email,password,confirmpassword):
    s=SeleniumWrapper(setup_and_teardown)
    homepage=HomePge(setup_and_teardown)
    homepage.click_register()
    registerpage=RegisterPage(setup_and_teardown)
    registerpage.register("raj","sri","raj@company.com","password@1345","password@1345")
