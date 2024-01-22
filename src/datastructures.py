
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members =[ 
            {
                "id": self. _generateId(),
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self. _generateId(),
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self. _generateId(),
                "first_name": "Jimmi",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
            },
            {
                "id": self. _generateId(),
                "first_name": "Jorge",
                "last_name": "Jackson",
                "age": 38,
                "lucky_numbers": [8,6,100]
            },
            {
                "id": self._generateId(),
                "first_name": "Hely",
                "last_name": "Jackson",
                "age": 19,
                "lucky_numbers": [15,21,30]
            },
            {
                "id": self._generateId(),
                "first_name": "Mariu",
                "last_name": "Jackson",
                "age": 36,
                "lucky_numbers": [25,50,150]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)

    def delete_member(self, member_id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == member_id:
                self._member.remove(member)
                return True
            return False

    def get_member(self, member_id):
        for member in self.members:
            if member['id'] == member_id:
                return member
            return None
        
        # fill this method and update the return
        def get_member(self, member_id):
            for member in self.members:
                if member['id'] == member_id:
                    return member
                return None
            
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
