*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Verify all products displayed
    Element Should Be Visible    id=tbodyid
    Capture Page Screenshot    ../Screenshots/product_display.png

Click first product
    Click Element    xpath=//a[text()='Samsung galaxy s6']
    Page Should Contain Element    //a[text()='Add to cart']

Verify product details
    Wait Until Page Contains Element    id=more-information
    Element Should be Visible        id=more-information
    Capture Page Screenshot    ../Screenshots/product_details.png