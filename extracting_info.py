def extracting_inf(): 
    
    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    person= "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(person.find("John F. Kennedy"))
    print(person[83:])
    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    info="Python is fun. Fun is good. Good is subjective."
    # a. Extract the word 'subjective' without knowing its exact position.
    print(info.find("subjective"))

    # b. Extract every third word.
    every_third_word = info.split()[0::3]
    every_third_worb= info.split()[-1::-3]
    print(every_third_word)
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    print(every_third_worb)