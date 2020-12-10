Feature: Check login functionality
  @regression
  Scenario: Check user is able to login when valid credentails are entered
    Given I launch the webiste
    When I enter credentails username as "atulb" and password as "ab00338092"
    Then I should see be able to login to application