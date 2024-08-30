# convert JOHn . to john:
my_name = " JOHn ."
n = my_name.lower().strip().replace(".","")
print(n)

# only display "Breed is German":
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

# only display "Clinton forces"
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

# split where there is a semi-colon:
s = "The lazy dog; ran so fast; it hit the wall"
p = s.split(";")
print(len(p))

# clean up the names to John Doe:
first_name = " Joh.n"
last_name = " Do,e"
full_name = first_name.replace(".","").strip() + " " + last_name.replace(",","").strip()
print(full_name)

# display EWC:
r = '["E","W","C"]'
s = r.replace("'","").replace("[","").replace('"','').replace('"','').replace(",","").replace("]","")
print(s)