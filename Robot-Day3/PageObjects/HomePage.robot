*** Settings ***
Documentation    PageObjects related  to home page
Library    SeleniumLibrary
Resource    ../Resources/Variables.robot

*** Keywords ***
Navigate to home page
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Browser Implicit Wait    10s
    Capture Page Screenshot    ../Screenshots/home_page.png

Verify the logo is displayed
    Element Should Be Visible    xpath=//a[@class="navbar-brand"]
    Capture Page Screenshot    ../Screenshots/logo.png