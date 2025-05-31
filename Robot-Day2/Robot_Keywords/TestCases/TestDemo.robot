*** Settings ***
Documentation    Testing the guvi.in homepage

Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://www.guvi.in
${BROWSER}    chrome

*** Test Cases ***

TestCase-1
    Start automation

TestCase-2
    Stop automation

*** Keywords ***

Start automation
    [Documentation]    Start automation
    [Tags]    start, home
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Browser Implicit Wait    10s
    Capture Page Screenshot    ../Screenshots/image_1.png

Stop automation
    [Documentation]    Stop the automation
    [Tags]    stop, home
    Close All Browsers