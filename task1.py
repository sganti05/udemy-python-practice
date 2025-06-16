'''
"Task - 1 : You are given a list of integers where each number appears twice, except for one unique number that appears only once. 
Example : 
Input: [4, 1, 2, 1, 2]  
Output: 4  
"
'''

list = [4, 1, 2, 1, 2]
# Goal: Output the one unique number that appears only once
# Idea behind solution: Utilisation of XOR property, which is an ideal solution as any number XOR'd with itself returns 0, and any number XOR'd with zero remains as itself

def uniqueNum(list):
    result = 0  # start off with zero 
    for item in list: # iterate through the numbers in the list
        result ^= item # ^ is the XOR operator, and so result is updated during every iteration and in the end the unique number is outputted
    return result # final result returned


# Function test
print(uniqueNum(list))