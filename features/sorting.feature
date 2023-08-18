Feature: Saucedemo web page sorting functionality verification
    As a user,
    I want to use the Saucedemo web application sorting features,
    So that I can verify their functionality.

    Background:
        Given I log in with the standard user.

    @sorting
    Scenario: Sorting products by price, high to low is working.
        When I sort products by price, high to low.
        Then The first price is higher than the second price.

    Scenario: Sorting products by price, low to high is working.
        When I sort products by price, low to high.
        Then The first price is lower than the second price.

    Scenario: Sorting products in alphabetical order is working.
        When I sort products in alphabetical order.
        Then The sorted products are in alphabetical order.

    Scenario: Sorting products in reverse alphabetical order is working.
        When I sort products in reverse alphabetical order.
        Then The sorted products are in reverse alphabetical order.