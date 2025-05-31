*** Settings ***

Documentation    Test suite for QAV SignUp Page

Resource    ../PageObjects/SignUpPage.robot

*** Test Cases ***

TestCase-1
    Start sign up page

TestCase-2
    Fill the signup form

TestCase-3
    Submit and validate form

TestCase-4
    Shutdown automation
