from behave import *


class Logout:
    @when(u'I enter credentails username as "{username}" and password as "{password}"')
    def enter_user_name_and_password(context,username,password):
        context.driver.find_element_by_id("username").send_keys(username)
        context.driver.find_element_by_id("password").send_keys(password)
        context.driver.find_element_by_xpath("//*[@name='login']").click()

    @when(u'I click on logout link')
    def step_impl(context):
        print("***********************")
        print(context.config.userdata.get("browser", "chrome"))
        print(context.config.userdata.get("env", "prod"))
        print("***********************")
        context.driver.find_element_by_xpath("//a[.='Sign out']").click()

    @then(u'I should be redirected back to login page')
    def step_impl(context):
        assert context.driver.current_url == "https://www.redmine.org/"
