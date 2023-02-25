
Feature: User information
   @browser
   Scenario Outline: Check the price of first product
      Given the price of first product is "<price>"
      Examples: Credentials
         | price  | 
         | $29.50 | 
         | $28.00 |