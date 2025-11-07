

def advanced_slice():

    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    # a. Extract the letters 'hij'.
    # b. Extract every second letter starting from 'a' to 'm'.
    # c. Reverse the entire string using slicing.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print (alphabet[7:10])

    print (alphabet[0:13:2])

    print (alphabet[::-1])
    

    # c. Reverse the entire string using slicing.
    print(alphabet[13::-1])
