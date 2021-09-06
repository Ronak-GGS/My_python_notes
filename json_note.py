"""
    this is the practice of json module
    dumps: python dictionary ko json object ma convert karta hai.
    dump: python dictionary ya json object ko ek file mai save karta hai.
    loads: json object ko python dictionary ma convert karta hai.
    load: json object ko ek file sa python dictionary ma convert karta hai.
"""
# importing json
import json

# creating python dictionary.
python_dictionary = {"name": "Ronak", "Place": "Kharkhoda", "Age": 21, "hobbies": ["chess", "Programming"],
                     "Male": True, "bad habit": None}

print(python_dictionary)

# Converting python dictionary to json object using dumps function.
json_object = json.dumps(python_dictionary, indent=4)
print(json_object)

# Saving python object into a file using dump function.
with open("my_file.json", 'w') as file:
    json.dump(python_dictionary, file, indent=12)

# Converting json object to python dictionary from a file.
with open("my_file.json", 'r') as file1:
    a = json.load(file1)
    print(a)

# Converting json object to python dictionary using loads function.
python_dictionary1 = json.loads(json_object)
print(python_dictionary1)

"""__________________________________________ADVANCE USAGE OF JSON MODULE__________________________________________"""

