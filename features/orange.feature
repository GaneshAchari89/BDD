Feature: OrangeHRM logo

  Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orangeHRM homepage
    Then verify that the logo present on page
    And close browser