from behave import *

@given('I am on the home page')
def step_impl(context):
    context.login_page.open_login_page()

@then('I should see the Sauce Labs logo')
def step_impl(context):
    context.login_page.verify_Logo()