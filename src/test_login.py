from generic import SeleniumWrapper
from homepage import HomePge
from loginpage import LoginPage
from pytest import mark
from time import sleep
header="username,password"
data=[("raj@company.com","password@1345"),
      ("harish12@gmail.com","password@134")]
@mark.parametrize(header,data)
def test_login(setup_and_teardown,username,password):
    s=SeleniumWrapper(setup_and_teardown)
    homepage=HomePge(setup_and_teardown)
    homepage.click_login()
    login=LoginPage(setup_and_teardown)
    login.login("raj@company.com","password@1345")

# header="username,password"
# data=[("rajasree123456@gmail.com","password@123"),
#       ("harish12@gmail.com","password@134"),
#       ("raj123467@gmail.com","password@1234")]
# @mark.parametrize(header,data)
# def test_login_positive(setup_and_teardown,username,password):
#     s=SeleniumWrapper(setup_and_teardown)
#     homepage=HomePge(setup_and_teardown)
#     homepage.click_login()
#     loginpage=LoginPage(setup_and_teardown)
#     loginpage.login("rajasree123456@gmail.com","password@123")