import sys
import random

import twitter


# users = api.GetFriends()
# print [u.name for u in users]
# Any milk? Should not a new situation for her; the man-cook had walked off the day to let the rage free Still me, till they kill me.
# http://code.google.com/p/python-twitter/


def make_chains(corpus, num):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    corpus = corpus.strip("\"")
    corpus = corpus.split()
    chains = {}

    # create first key of length num
    first_key = []
    for i in range(num):
        first_key.append(corpus[i])
    key = tuple(first_key)
    del corpus[:num] #deleted first key off of corpus

    val = corpus.pop(0) #popped off first item of corpus (after key)
    chains[key] = [val] #created first keypair
    
    while corpus:
        key = (key[1:],) + (val,)
        print key
        val = [corpus.pop(0)]
        chains[key] = [val]

    print chains






        #key[1:]+tuple(corpus.pop(0))
    


   
      


    # create second key from first key
    # pop off value each time

make_chains("this is a bear this is a fish this is a squid this is a mouse", 3)
#     return chains

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""

#     words = []
#     start = random.choice(chains.keys())

#     first_word = start[0]
#     second_word = start[1]
#     third_word = start[2]
#     fourth_word = random.choice(chains[start])

#     words.append(first_word)
#     words.append(second_word)
#     words.append(third_word)
#     words.append(fourth_word)

#     final_word = words[-1]
#     end = final_word.endswith(".") 

#     while (end == False) and (len(words) < 30):
#         new_tuple = (words[-3], words[-2], words[-1])
#         print new_tuple
#         next_word = random.choice(chains[new_tuple])
#         words.append(next_word)
#         final_word = words[-1] # this wasn't working b/c we weren't updating this
#         end = final_word.endswith(".") 

#     words[0] = words[0].capitalize()
#     return ' '.join(words)

# def tweet(input):
#     if len(input) <= 140:
#         api = twitter.Api(consumer_key='hA6K7OxR1oR8V0DvOpzg', consumer_secret='KYtgbt1o1ZAhOz0nMenHyHWwblTbIWaKlOsKTweOA', access_token_key='1551771666-XwjzKJvlMVib1diluM1bom5iRjnWmOrQkm57O3N', access_token_secret='J6uJm3EOib94KXYW7zPcxsLv0tHGB9xY8f7UJK8') 
#         status = api.PostUpdate(input)
#         return "Tweet successful!"
#     else:
#         return "The tweet was too long!"


# def main():
#     args = sys.argv

#     script, filename, num = args

#     f_open = open(filename)

#     input_text = f_open.read() # one big text string

#     chain_dict = make_chains(input_text)
    
    #random_text = make_text(chain_dict)
    #print random_text
    # print tweet(random_text)



# if __name__ == "__main__":
#     main()


# #yay! ['give', 'him,', 'as', 'it', 'were', 'beseeching', 'him', 'in', 'some', 'way', 'or', 'other', 'to', 'make', 'him', 'an', 'old', 'man,', 'not', 'susceptible', 'to', 'love.', 'Except', 'deceit', 'and', 'lying', 'were', 'opposed', 'to', 'his', 'imagination,', 'all', 'the', 'same', 'house', 'with', 'him.', 'The', 'principal', 'qualities']
# #Death collision was futuristic twisting riches But there is only one way to make him an old friend, his valet, Matvey, carrying his clothes, his boots, and a telegram


        # key = [] # build a list with items for the key tuple
        # while True:
        #     for i in range(0, num):
        #         key.append(corpus[i]) #appending to a list called key
        #     val = corpus[num + 1]
        #     key = tuple(key) #turning the list into a tuple, and still calling it key
        #     chains.setdefault(key, []).append(val)