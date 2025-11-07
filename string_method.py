def string_meth():
        
    # Problem Set 3: String Methods
    # Upper & Lower:
    # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
    hi="MAY THE FORCE BE WITH YOU."
    print(hi.lower())

    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    # a. Convert the list into a single string.
    # b. Now, split the string at every occurrence of the letter 'a'.
    motto = ["Make", "haste", "slowly."]

    comb= " ".join(motto)
    print(comb)
    fr=comb.split('a')
    print(fr)
    # Replacing Words:
    # Modify the sentence: "Life is what happens when you are busy making other plans."
    sentence= "Life is what happens when you are busy making other plans."
    # a. Replace "busy" with "distracted".

    # b. Replace "plans" with "mistakes".
