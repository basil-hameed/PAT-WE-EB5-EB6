*** Settings ***
Documentation    Validating the login into the SauceDemo Page

Library    SeleniumLibrary

*** Variables ***

${SAUCEDEMO_URL}    https://www.saucedemo.com/
${BROWSER}    chrome
${USERNAME}    standard_user
${PASSWORD}    secret_sauce

*** Test Cases ***

TestCase-1
    [Documentation]    Start automation
    [Tags]    start
    Open Browser    ${SAUCEDEMO_URL}    ${BROWSER}
    Maximize Browser Window
    Set Browser Implicit Wait    10s

TestCase-2
    [Documentation]    Add the login credentials
    [Tags]    login
    Element Should Be Visible    name=user-name
    Input Text    name=user-name    ${USERNAME}
    Element Should Be Visible    name=password
    Input Text    name=password  ${PASSWORD}
    Element Should Be Enabled    xpath=//input[@id="login-button"]
    Click Element    xpath=//input[@id="login-button"]
    Page Should Contain    Products

TestCase-3
    [Documentation]    Validating product added to cart
    [Tags]    add_to_cart
    Element Should Be Enabled    id=add-to-cart-sauce-labs-backpack
    Click Element    id=add-to-cart-sauce-labs-backpack
    Element Should Be Enabled    class=shopping_cart_link
    Click Element    class=shopping_cart_link
    Page Should Contain    Sauce Labs Backpack

TestCase-4
    [Documentation]    Stop the automation
    [Tags]    stop
    Close All Browsers





