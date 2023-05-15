Feature: Login to Sauce demo page

  Background:
    Given I am on the login page

  @success
  Scenario: successful login
    When I insert the username "standard_user" and the password "secret_sauce"
    When I click the login button
    Then I am successful logged into the app

  @fail
  Scenario Outline: failed login
    When I insert the username "<username>" and the password "<password>"
    When I click the login button
    Then I receive the error message "<error_message>"
    Examples:
      |username  |password |error_message|
      |user_gresit |pass_gresit |Epic sadface: Username and password do not match any user in this service|
      |user_gresit |secret_sauce |Epic sadface: Username and password do not match any user in this service|
      |standard_user |pass_gresit |Epic sadface: Username and password do not match any user in this service|


