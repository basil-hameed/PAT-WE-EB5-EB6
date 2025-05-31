*** Settings ***

Documentation    Validating sign up page of QAV website

Library    SeleniumLibrary

*** Variables ***

${BASE_URL}    https://qavbox.github.io/demo/signup/
${FULL_NAME}    Basil
${EMAIL_ID}     tester@gmail.com
${TELEPHONE}    9756748748
${GENDER}        Male
${EXPERIENCE}    five
${SKILLS}    automationtesting
${AUTOMATION_TOOLS}    Selenium

*** Keywords ***
Start sign up page
    [Documentation]    Open browser and navigate to sign up page
    [Tags]    start
    Open Browser    ${BASE_URL}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    10s
    Capture Page Screenshot    ../Screenshots/start_page.png

Fill the signup form
    [Documentation]    Fill the signup form
    [Tags]    form_filling
    Input Text    id=username    ${FULL_NAME}
    Input Text    id=email    ${EMAIL_ID}
    Input Text    id=tel    ${TELEPHONE}
    Select From List By Label    name=sgender    ${GENDER}
    Click Element    xpath=//input[@value='${EXPERIENCE}']
    Click Element    xpath=//input[@value='${SKILLS}']
    Select From List By Label    id=tools    ${AUTOMATION_TOOLS}
    Capture Page Screenshot    ../Screenshots/filled_form.png

Submit and validate form
    [Documentation]    Submit the form and validate submission
    [Tags]    submit_form, validate
    Click Button    id=submit
    Alert Should Be Present    Registration Done!
    Capture Page Screenshot    ../Screenshots/submitted_form.png

Shutdown automation
    [Documentation]    Shutdown all browsers
    [Tags]    stop
    Close All Browsers



