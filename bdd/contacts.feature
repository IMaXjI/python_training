Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <id>, <firstname> and <lastname>
  When I add new contact to the list
  Then the new contact list is equal to the old list with new contact


  Examples:
  |  id  | firstname  | lastname  |
  |  id1 | firstname1 | lastname1 |
  |  id2 | firstname2 | lastname2 |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the group from the list
  Then the new contact list is equal to the old list without deleted contact