*** Settings ***

Documentation    Testing the guvi.in homepage with firefox

Library    SeleniumLibrary

*** Variables ***

${BASE_URL}    https://www.guvi.in/

*** Test Cases ***

TestCase-1
    [Documentation]    Start automation
    [Tags]    homepage, start, guvi
    Open Browser    ${BASE_URL}    firefox

TestCase-2
    [Documentation]    Stop automation
    [Tags]    homepage, stop, guvi
    Close All Browsers
