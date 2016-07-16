Feature: Search

  Scenario: User search for an item and find advertisements
     Given I access the advertisement page
      when I search for "apartamento"
      then I have to find advertisements for "apartamento"
  
  
  Scenario: User search for an item and don't find advertisements
     Given I access the advertisement page
      when I search for "foobarxpty"
      then I dont find advertisements
