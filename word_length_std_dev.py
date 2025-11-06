# project-6

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 11/5/2025
# Description: This program finds the standard deviation of the
#length of words in a sentence.

import string
def word_length_std_dev(text):
    """
    This function takes the string (text) and returns the standard deviation
    of the word length.

    """

    #split the text into words
    words = text.split()

    #Remove punctuation from each word
    clean_words = []
    for word in words:
        clean_word=word.strip(string.punctuation)
        if clean_word:
            clean_words.append(clean_word)

    #if there is only one or more words, then std is 0
    N = len(clean_words)
    if N <= 1:
        return 0.0

    #Get length of eac word
    word_lengths = [len(word) for word in clean_words]

    #calculate the mean (avg) of length
    mean = sum(word_lengths) / N

    #Finds how far each length is from the mean, then sq it
    sq_diffs = [(length - mean) ** 2 for length in word_lengths]

    #STD
    std_dev= (sum(sq_diffs) / (N - 1)) ** 0.5

    return std_dev

#Test the function
text= "There is wisdom in turning as often as possible from the familiar to the unfamiliar it keeps the mind nimble it kills prejudice and it fosters humor"
answer = word_length_std_dev(text)
print("The STD is ", round(answer, 2))