*** Settings ***
Documentation    End-to-End Testing of Demoblaze Website
Library    SeleniumLibrary
Resource    ../PageObjects/HomePage.robot
Resource    ../PageObjects/LoginPage.robot
Resource    ../PageObjects/ProductPage.robot
Resource    ../PageObjects/CartPage.robot
Test Teardown    Close Browser

*** Test Cases ***
Login Test
    Navigate to home page
    Click Login Button
    Enter Login Credentials
    Verify Login Successful

Logo Test
    Navigate to home page
    Verify the logo is displayed

Product Display Test
    Navigate to home page
    Verify all products displayed

Product Details Test
    Navigate to home page
    Click first product
    Verify product details


Add To Cart Test
    Navigate to home page
    Click first product
    Add Product To Cart
    Go To Cart
    Verify Product In Cart