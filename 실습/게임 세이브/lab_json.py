import json

numbers = [1, 2, 3, 4]
numbers_string = json.dumps(numbers)
print(numbers_string)

value_string = '{"x": 10, "y": 20, "size": 4.5}'
value = json.loads(value_string)
print(value)