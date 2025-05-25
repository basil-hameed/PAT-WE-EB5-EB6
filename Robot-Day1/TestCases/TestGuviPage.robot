*** Settings ***

Documentation    Validate the title and url of guvi homepage

Library    SeleniumLibrary

*** Variables ***

${BASE_URL}    https://www.guvi.in/
${WRONG_URL}    https://www.saucedemo.com/
${EXPECTED_TITLE}    GUVI | Learn to code in your native language

*** Test Cases ***

TestCase-1
    [Documentation]    Start the automation
    [Tags]    start, homepage
    Open Browser    ${BASE_URL}    chrome
    Maximize Browser Window


TestCase-2
    [Documentation]    Validate URL - Positive
    [Tags]    homepage, url
    ${URL} =    Get Location
    Log To Console    ${URL}
    Should Be Equal    ${URL}    ${BASE_URL}

TestCase-3
    [Documentation]    Validate URL - Negative
    [Tags]    homepage, url
    ${URL} =    Get Location
    Log To Console    ${URL}
    Should Not Be Equal    ${URL}    ${WRONG_URL}

TestCase-4
    [Documentation]    Validate Title
    [Tags]    homepage, title
    ${TITLE} =    Get Title
    Log To Console    ${TITLE}
    Should Be Equal     ${TITLE}    ${EXPECTED_TITLE}

TestCase-5
    [Documentation]    Stop automation
    [Tags]    stop
    Close All Browsers