*** Settings ***

Documentation    Testing the automationcrm website

Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://automationplayground.com/crm/index.html
${USERNAME}    basil@gmail.com
${PASSWORD}    Secret@123
${EMAIL}    test@example.com
${FIRST_NAME}    Automation
${LAST_NAME}    Tester
${CITY}    Chennai


*** Keywords ***

Start automation
    [Documentation]    Start the robot automation
    [Tags]    start
    Open Browser    ${BASE_URL}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    10s
    Capture Page Screenshot    ../Screenshots/login_page.png

Sign in to the application
    [Documentation]    Navigating to sign in page
    [Tags]    sign_in
    Click Element    name=sign-in-link
    Capture Page Screenshot    ../Screenshots/signin_page.png

Add Sign up credentials
    [Documentation]    Enter the login credentials
    [Tags]    login
    Input Text    id=email-id    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=submit-id
    Capture Page Screenshot    ../Screenshots/after_login.png

Add a new customer
    [Documentation]    Adding a new customer
    [Tags]    customer
    Click Element    id=new-customer
    Input Text    id=EmailAddress    ${EMAIL}
    Input Text    id=FirstName    ${FIRST_NAME}
    Input Text    id=LastName    ${LAST_NAME}
    Input Text    id=City    ${CITY}
    Select From List By Value    id=StateOrRegion    AZ
    Select Radio Button    gender    male
    Scroll Element Into View    xpath=//button[@type='submit']
    Click Button    xpath=//button[@type='submit']
    Capture Page Screenshot    ../Screenshots/added_customer.png

Confirm the user
    [Documentation]    Confirm the newly added user
    [Tags]    verification
    Wait Until Page Contains    Success! New customer added.
    Capture Page Screenshot    ../Screenshots/customer_verified.png

Shutdown automation
    [Documentation]    Shut down the browsers
    [Tags]    stop
    Close All Browsers