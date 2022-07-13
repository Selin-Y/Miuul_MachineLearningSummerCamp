##########
# Exercise - Interview Question
# We want to write a string-changing function as follows.
# Let's make the string expressions uppercase in even indexes, lowercase in odd indexes.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""
    # traverse the indexes of the entered string.
    for string_index in range(len(string)):
        # capitalize if index is even.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # lowercase if index is odd.
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")

