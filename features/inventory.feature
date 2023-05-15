Feature: Test add to cart functionality

  Scenario Outline: add to cart Sauce Labs Bike Light
    Given I am logged into the app
    When I click Add to chart button to the item "<item>"
    Then The Remove button is displayed for the item "<item>"
    When I check the basket page
    Then The item "<item>" is displayed in basket
    When I remove the item "<item>" from the cart
    When I go back to shopping list
    Then The Add to chart button is displayed for the item "<item>"

    Examples:
    |item                   |
    |sauce-labs-bike-light  |
    |sauce-labs-bolt-t-shirt|
    |sauce-labs-backpack    |
    |sauce-labs-fleece-jacket|
    |sauce-labs-onesie       |
    |test.allthethings()-t-shirt-(red)|