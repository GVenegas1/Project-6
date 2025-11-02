# project-6

Write a function called **word_length_std_dev** that takes as a parameter a string and returns the **sample standard deviation** of the lengths of the words in that string. You may assume that the text contains only words separated by spaces, with no punctuation or other symbols.

A lower standard deviation indicates that values are more tightly clustered around the mean. A higher standard deviation indicates that values are more spread out. The formula for the sample standard deviation looks like this:

$\Huge s=\sqrt{\frac{\sum\limits_{i=1}^N (x_{i} - \mu)^2}{N-1}}$

Where:
- $N$ is how many values are in the list (the population)
- $i$ counts from 1 to $N$
- $x_{i}$ is the $i^{th}$ value in the list
- $μ$ is the mean (average) of the values in the list
- $Σ$ gives the sum of the expression to its right for each value of $i$
- $s$ is the sample standard deviation

In case you need a review of summation notation, here's a simple example:

$\Large \sum\limits_{i=1}^N x_{i}$

This expression would just add up all of the values in the list: $x_1 + x_2 + ... + x_N$

You can take the square root by using an exponent of 0.5. For example, the result of 9 ** 0.5 is 3.0.

Here's a simple example of how your class and function could be used:
```
text = 'There is wisdom in turning as often as possible from the familiar to the unfamiliar it keeps the mind nimble it kills prejudice and it fosters humor'
answer = word_length_std_dev(text)
```

The file must be named: word_length_std_dev.py
