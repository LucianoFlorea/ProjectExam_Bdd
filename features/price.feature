Feature: Verify Pricing Information

  Scenario: Verify product prices on the inventory page
    Given I am logged into the app for price
    When I check the inventory page
    Then  I should see the prices of all products

  Scenario Outline: View product price on the product page
    Given I am logged into the app for price
    When I go to the product page for "<item2>"
    Then I should see the price of the "<item2>"
    Examples:
    |item2                           |
    |Sauce Labs Backpack             |
    |Sauce Labs Bike Light           |
    |Sauce Labs Bolt T-Shirt         |
    |Sauce Labs Fleece Jacket        |
    |Sauce Labs Onesie               |
    |Test.allTheThings() T-Shirt (Red)|



