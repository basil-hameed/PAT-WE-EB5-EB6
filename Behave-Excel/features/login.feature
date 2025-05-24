Feature: Saucedemo login validation using Excel Data

  Scenario: Login with multiple credentials
    Given the Excel file is loaded
    When I try to login with all data sets
    Then the login results are updated