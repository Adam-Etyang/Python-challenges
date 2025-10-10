"""
Imagine you have a function `get_data_from_database()` That returns a list of dicts but the list could be very large
Create a generator expression that takes the list of dicst extracts a specific value from each docionary and converts that value to an int, but ony for dicst where a certain flag is True
The generator expression should only yeild integers for velid data
Demonstrate consuming the first two items from the generator expression.
"""

# Sample data
mock_data = [
    {"id": 1, "value": "10", "flag": True},
    {"id": 2, "value": "20", "flag": False},
    {"id": 3, "value": "30", "flag": True},
    {"id": 4, "value": "abc", "flag": True},  # This one will cause an error
    {"id": 5, "value": "50", "flag": True},
]


def get_data_from_database():
    pass


if __name__ == "__main__":
    pass
