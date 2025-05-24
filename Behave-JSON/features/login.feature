Feature: Login functionality of SauceDemo

  Scenario: Login with multiple credentials using JSON
    Given the browser is launched
    When user attempts login with multiple credentials from json
    Then update the test results into json