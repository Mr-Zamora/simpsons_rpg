"""
family.py - Contains the Family class for the Simpsons RPG
"""

# Aggregation Class (Whole in Family aggregation)
# Aggregates 1..* Simpson members.
class Family:
    """
    Represents a Family unit.
    Corresponds to the Family class in the UML diagram.
    Aggregates 1..* Simpson members (the parts).
    """
    def __init__(self, lastName):
        """Initializes a Family."""
        # Attribute: lastName (Public)
        self.lastName = lastName
        # Aggregation: Family has 1..* Simpson members
        # This is implemented by holding a list of Simpson objects.
        self.members = [] # Start with an empty list

    # +add_member(member) (Public method)
    def add_member(self, member):
        """Adds a member to the family."""
        # This method demonstrates aggregation - Family "has" members
        self.members.append(member)
        # Note: In a more complex implementation, we might check if the member
        # is already in the family, or enforce other constraints.
        print(f"{member.name} is now part of the {self.lastName} family.")

    def __str__(self):
        """String representation of the Family."""
        # List all family members in the string representation
        member_names = [member.name for member in self.members]
        return f"The {self.lastName} Family: {', '.join(member_names)}"
