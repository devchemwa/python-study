# data structure used to store data in key-value pairs:
#  the key and value are separated with :
#  enclosed with {}
#  keys are case-sensitive
#  creating a dictionary:
person = {'name' : "Rick Sanchez", 'age' : 20, 'location' : "Somewhere", 'place of work' : "Karen, Big Square"}
details = {'name' : "Rick", 'class' : "4N", 'ADM':676, 'addr' : {'code' : 20020, 'street' : "kimathi"}, 'subjects' : ["eng","kisw","comp"],}

# add town to addr
details['addr']['town'] = "Ongata Rongai"
print(details)

# add chemistry to subjects
details['subjects'].append("Chemistry")
print(details)

# dictionary methods:
# => .keys() - returns the keys of the dictionary:
print(details.keys())
# => .values() - returns the values of the dictionary: 
print(details.values())
# => .items() - returns all key-value pairs: 
print(details.items())
# => .clear()

# => .copy()

# => .update() - updates the dictionary with elements from another dictionary:
