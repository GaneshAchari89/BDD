Feature: OrangeHRm Login
  Scenario: Login to OrangeHRM with valid parameter
    Given launch chrome browser
    When open OrangeHRM Home page
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page
