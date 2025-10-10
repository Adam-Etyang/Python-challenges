"""
Imagine you have a function `get_data_from_database()` That returns a list of dicts but the list could be very large
Create a generator expression that takes the list of dict extracts a specific value from each dict and converts that value to an int, but ony for dicst where a certain flag is True
The generator expression should only yield integers for valid data
Demonstrate consuming the first two items from the generator expression.
"""


def get_data_from_database() -> list:
    return [
        {"id": 1, "value": "10", "flag": True},
        {"id": 2, "value": "20", "flag": False},
        {"id": 3, "value": "30", "flag": True},
        {"id": 4, "value": "abc", "flag": True},  # This one will cause an error
        {"id": 5, "value": "50", "flag": True},
    ]


def safe_int_conversion(value: str):
    try:
        return int(value)
    except ValueError:
        return None


if __name__ == "__main__":
    raw_data = get_data_from_database()
    for record in raw_data:
        print(record)

    print("---- Transformed Data ----")
    transformed_data = (
        safe_int_conversion(data["value"]) for data in raw_data if data["flag"] is True
    )
    print(list(transformed_data))
