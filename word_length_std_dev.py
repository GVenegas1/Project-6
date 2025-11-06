# project-6

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 11/5/2025
# Description: This program finds the standard deviation of the
#length of words in a sentence.


def word_length_std_dev(text):
    """
    This function takes the string (text) and returns the standard deviation
    of the word length.

    """

    #split the text into words
    words = text.split()

    #counting how many words there are
    N = len(words)

    #if there is only one or no words, STD is 0
    if N <= 1:
        return 0
    # Makes a list with the length of each word
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))

    #finds the average (mean)word length
    total_length = sum(word_lengths)
    mean = total_length / N

    #Finds how far each length is from the mean, then sq it
    sq_diffs = []
    for length in word_lengths:
        difference = length - mean
        squared = difference ** 2
        sq_diffs.append(squared)

    #Add all the squared difference together
    sum_sq_difference  = sum(sq_diffs)

    #Divid by (N-1 and take the squared root
    std_dev = (sum_sq_difference / N) ** 0.5

    return std_dev

#Test the function
text= "elle when tp sleep early"
answer = word_length_std_dev(text)
print("The STD is ", round(answer, 2))