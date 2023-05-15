from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.open_login_page()

@when('I insert the username "{username}" and the password "{password}"')
def step_impl(context, username, password):
    context.login_page.insert_username(username)
    context.login_page.insert_password(password)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_btn()

@then('I am successful logged into the app')
def step_impl(context):
    context.login_page.check_successful_login()

@then('I receive the error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_login_error_message(error_message)