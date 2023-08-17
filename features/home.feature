Feature: Verify SauceLabs Home Page

  Scenario: Logo presence on SauceLabs home page
    Given launch chrome browser
    When open SauceLabs webpage
    Then verify that the logo present on page
    And close browser