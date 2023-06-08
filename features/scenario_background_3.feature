# Background is for common steps

Feature: Scenario Background

  Background: Common steps
    Given launch browser
    When open homepage

  Scenario: Logo presence on OrangeHRM home page
    Then verify that the logo present
    And close the browser

  Scenario: Login to OrangeHRM with valid parameter
    When Enter user "admin" and password "admin123"
    And Click login button
    Then User must successfully login to the dashboard