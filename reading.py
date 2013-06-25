'''

'''
def round(inp): # takes a float as input & rounds up or down to an integer
    base = int(inp) # recasts inp as an integer
    if inp - base >= 0.5: # if input - base is greater than or equal to .5:
        return base+1 #return base plus one
    else:
        return base # otherwise return the base
    
def count_lines(string): # takes a str as input and counts the number of lines in it
    if not inp:
        return 0
    num = 1 # initalize counter variable num to 1
    for c in inp: # iterate through inp
        if c == "\n": # if an item in inp is a new line
           num  += 1  # increment the counter variable num
    return num # returns number of lines in the input string

def third_side(length_a, length_b): # for a right triangle with sides of length_a and length_b, calculate
                    # length of the third side
    c = a * a + b * b
    return Math.sqrt(c)
    

def reverser(input_list): # reverses a list
    size = len(inp)
    for i in range(len(inp)/2): # iterate across range from 0 to 1/2 the length of inp
        temp = inp[i] # store each item in a temp variable, map value to index
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp 
        
    return input_list # return reversed list
    
def count_word_frequency(): 
    inp = open("sample_input.txt") # open a text file
    ws = inp.split() # create a list of the words in the file
    h = dict() # initialize an empty dictionary
    for w in ws: # for each word in the list of words
        num = h.get(w, 0) # get the key that matches w. if it doesn't exist, 
                          #  create it with default value 0.
        num += 1 # increase the value of key w by 1.
        h[w] = num # assign the newly-incremented value back to key w. 
    
    for k, v in h.iteritems(): # iterate through each key/value pair in the dictionary
        print "%s:\t%d"%(k, v) # print each key with its value, i.e. print each word 
                                # with a count of how many times it appeared in the text file.

def swapfail(inp): # sorts a list in ascending order using bubble sort
    swapped = True
    while swapped == True:
        swapped = False # breaks the loop
        for i in range(len(inp)-1): # iterate over inp
            if inp[i] > inp[i+1]: # if a value is greater than the next value in the list
                tmp = inp[i] # store it in a temp variable
                inp[i] = inp[i+1] # swap values
                inp[i+1] = tmp # will end up with two values the same
                swapped = True # this is the worst function ever
