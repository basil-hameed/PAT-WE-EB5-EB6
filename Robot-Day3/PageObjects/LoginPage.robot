*** Settings ***
Documentation  PageObjects related to login page

Library    SeleniumLibrary
Resource    ../Resources/Variables.robot

*** Keywords ***
Click Login Button
    Wait Until Element is Enabled    id=login2
    Click Element    id=login2

Enter Login Credentials
    Wait Until Element is Visible    id=loginusername
    Input Text    id=loginusername    ${USER_NAME}
    Input Text    id=loginpassword    ${PASSWORD}
    Click Button    xpath=//button[text()="Log in"]

Verify Login Successful
    Wait Until Element is Visible    id=nameofuser
    Element Should Contain    id=nameofuser    Welcome
    Capture Page Screenshot    ../Screenshots/login_page.png

