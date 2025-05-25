*** Settings ***
Documentation    Drag and Drop using robot framework

Library    SeleniumLibrary

*** Variables ***

${BASE_URL}    https://qavbox.github.io/demo/dragndrop/
${BROWSER}    chrome

*** Test Cases ***

TestCase-1
    [Documentation]    Start the automation
    [Tags]    start
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Browser Implicit Wait    10s

TestCase-2
    [Documentation]    Perform the drag and drop action
    [Tags]    dragdrop
    Drag And Drop    id=draggable    id=droppable
    Element Text Should Be    id=droppable    Dropped!
    Sleep    4s

TestCase-3
    [Documentation]    Stop the automation
    [Tags]    stop
    Close All Browsers

