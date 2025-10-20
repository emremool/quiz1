full_name = "Emre Mol"
first_name = full_name[0:4]
last_name = full_name[5:]
full_name_length = len(full_name)
first_name_length = len(first_name)
last_name_length = len(last_name)
bSum = full_name_length == first_name_length + last_name_length + 1
print(bSum)
