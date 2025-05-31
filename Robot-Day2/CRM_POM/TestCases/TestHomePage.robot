*** Settings ***

Documentation    Testing the automationcrm website

Resource    ../PageObjects/HomePage.robot

*** Test Cases ***

TestCase-1
    Start automation

TestCase-2
    Sign in to the application

TestCase-3
    Add Sign up credentials

TestCase-4
    Add a new customer

TestCase-5
    Confirm the user

TestCase-6
    Shutdown automation

