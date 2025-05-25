*** Settings ***
Documentation    Testing the guvi.in page with Edge Browser

Library    SeleniumLibrary

*** Variables ***

${BASE_URL}    https://www.guvi.in/

*** Test Cases ***

TestCase-1
    [Documentation]    Start automation
    [Tags]    homepage, start
    Open Browser    ${BASE_URL}    edge

TestCase-2
    [Documentation]    Stop automation
    [Tags]    homepage, stop
    Close All Browsers