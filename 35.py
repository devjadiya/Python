# Python String center() Method
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"

x = txt.center(20)
# Parameter value --> length	Required. The length of the returned string
print(x)

x = txt.center(20, "O")
# Using the letter "O" as the padding characte
print(x)