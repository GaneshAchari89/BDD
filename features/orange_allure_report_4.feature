Feature: OrangeHRm Login

  Scenario Outline: Login to OrangeHRM with different parameter
    Given Browser launch
    When Opening Home page of OrangeHRM
    And Mention username "<username>" and password "<password>"
    And Clicking login button
    Then User successful login

    Examples:
      | username | password |
      | admin    | admin123 |
      | adm      | admin123 |
      | admin    | admi     |
      | adm      | admi23   |