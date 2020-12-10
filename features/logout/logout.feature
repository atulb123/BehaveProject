Feature: Check logout functionality

  Background:
    Given I launch the webiste
  @smoke @regression
  Scenario: Check user is able to logout after logging in
    When I enter credentails username as "atulb" and password as "ab00338092"
    When I click on logout link
    Then I should be redirected back to login page