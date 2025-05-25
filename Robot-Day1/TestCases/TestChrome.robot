*** Settings ***

Documentation    Testing the guvi.in homepage

Library    SeleniumLibrary

*** Variables ***

${BASE_URL}    https://www.guvi.in/
${TESTER_NAME}    Tester1

*** Test Cases ***

TestCase-1
    [Documentation]    Start automation
    [Tags]    homepage, start
    Open Browser     ${BASE_URL}    chrome

TestCase-2
    [Documentation]    Stop automation
    [Tags]    homepage, stop
    Close All Browsers

