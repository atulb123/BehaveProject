from behave import given, when, then
class LoginSteps:
    @given(u'I launch the webiste')
    def launch_website(context):
        context.driver.get("https://www.redmine.org/login")

    @then(u'I should see be able to login to application')
    def i_shd_see_user_is_able_to_login(context):
        assert context.driver.current_url == "https://www.redmine.org/my/page"