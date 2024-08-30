# creating sets:
# set() => converts any data to a set:
# difference => returns elements in first set but not in second set
# intersection => returns common elements in both sets
# symmetrical_difference => returns elements in either set which are not common
# add() => adds elements to a set
# remove() => removes elements from a list
# union() => combines all elements in both sets


days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

# Remove friday and sunday from the set using methods.
days.remove("friday")
days.remove("sunday")
print(days)

# Add them back to the set
days.add("friday")
days.add("sunday")
print(days)