# create tuples
# list() => convert tuple to list
# tuple() => convert list to tuple
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])

#2. Using a function a find the length of the tuple.
print(len(days))

#3. Replace Thursday with Thur
days = list(days)
days[3] = "Thur"
days = tuple(days)
print(days)