Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <id>, <firstname>, <lastname>
  When I add new contact to the list
  Then the new contact list is equal to the old list with new contact



  Examples:
  |  id  | firstname  | lastname  |
  |  id1 | firstname1 | lastname1 |
  |  id2 | firstname2 | lastname2 |