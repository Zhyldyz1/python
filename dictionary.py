what can we do with dictionary

In Python, dictionaries are one of the most versatile and widely used data structures.
They store data in key-value pairs, making them ideal for fast lookups, data organization, and mapping relationships.
Here are some common operations and things you can do with dictionaries:

1. Create a Dictionary
You can create a dictionary by enclosing key-value pairs in curly braces {}.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

2. Access Values
You can access values using their keys.
print(my_dict["name"])  # Output: Alice
If the key doesn't exist, it raises a KeyError. To avoid this, use the get() method.
print(my_dict.get("name"))       # Output: Alice
print(my_dict.get("country"))    # Output: None (key doesn't exist)
print(my_dict.get("country", "USA"))  # Output: USA (default value)

3. Add or Update Key-Value Pairs
You can add new key-value pairs or update existing ones.
my_dict["age"] = 26          # Update existing key
my_dict["country"] = "USA"   # Add new key-value pair
print(my_dict)  # Output: {"name": "Alice", "age": 26, "city": "New York", "country": "USA"}

4. Remove Key-Value Pairs
You can remove key-value pairs using del, pop(), or popitem().
del my_dict["city"]          # Removes the key "city"
age = my_dict.pop("age")     # Removes "age" and returns its value
last_item = my_dict.popitem()  # Removes and returns the last inserted key-value pair
print(my_dict)  # Output: {"name": "Alice", "country": "USA"}

5. Check for Keys
You can check if a key exists in the dictionary using the in keyword.
print("name" in my_dict)  # Output: True

6. Iterate Over a Dictionary
You can loop through keys, values, or key-value pairs.
# Loop through keys
for key in my_dict:
    print(key)

# Loop through values
for value in my_dict.values():
    print(value)

# Loop through key-value pairs
for key, value in my_dict.items():
    print(key, value)

7. Get All Keys, Values, or Items
You can retrieve all keys, values, or key-value pairs as lists (in Python 3, they are view objects).
keys = my_dict.keys()      # Get all keys
values = my_dict.values()  # Get all values
items = my_dict.items()    # Get all key-value pairs

8. Merge Dictionaries
You can merge two dictionaries using the update() method or the | operator (Python 3.9+).
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # Merge dict2 into dict1
print(dict1)  # Output: {"a": 1, "b": 3, "c": 4}

# Python 3.9+
merged_dict = dict1 | dict2

9. Dictionary Comprehensions
You can create dictionaries concisely using dictionary comprehensions.
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

10. Nested Dictionaries
Dictionaries can contain other dictionaries, allowing you to create complex data structures.
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(nested_dict["person1"]["name"])  # Output: Alice

11. Find the Length
You can find the number of key-value pairs in a dictionary using the len() function.
print(len(my_dict))  # Output: 3

12. Clear a Dictionary
You can remove all key-value pairs from a dictionary using the clear() method.
my_dict.clear()
print(my_dict)  # Output: {}

13. Copy a Dictionary
You can create a shallow copy of a dictionary using the copy() method or the dict() constructor.
copied_dict = my_dict.copy()
copied_dict = dict(my_dict)

14. Default Values with setdefault()
You can set a default value for a key if it doesn't already exist.'
'my_dict.setdefault("country", "USA")
print(my_dict)  # Output: {"name": "Alice", "age": 25, "city": "New York", "country": "USA"}

15. Convert to Other Data Structures
You can convert a dictionary to other data structures like lists, tuples, or sets.
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
items_list = list(my_dict.items())

16. Filter a Dictionary
You can filter a dictionary using dictionary comprehensions.
filtered_dict = {k: v for k, v in my_dict.items() if v > 20}
print(filtered_dict)  # Output: {"age": 25}

17. Sort a Dictionary
You can sort a dictionary by keys or values.
# Sort by keys
sorted_by_keys = dict(sorted(my_dict.items()))

# Sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

18. Use as JSON-Like Data
Dictionaries are often used to represent JSON-like data structures.
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "traveling"],
    "address": {"city": "New York", "zip": "10001"}
}

19. Use collections.defaultdict
The defaultdict from the collections module provides default values for missing keys.
from collections import defaultdict
my_dict = defaultdict(int)  # Default value is 0
my_dict["count"] += 1
print(my_dict["count"])  # Output: 1

20. Use collections.Counter
The Counter class from the collections module is useful for counting occurrences of elements.
from collections import Counter
counts = Counter(["a", "b", "a", "c", "b"])
print(counts)  # Output: Counter({"a": 2, "b": 2, "c": 1})
