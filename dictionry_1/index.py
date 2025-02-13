my_dictionary = (input("Enter the dictionary (name: age):"))
oldest_person = max(my_dictionary, key=my_dictionary.get)
print("The oldest person is: ",oldest_person)