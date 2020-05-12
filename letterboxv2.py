# SOFTWARE TO PLAY NYT'S LetterBoxed game

def make_dict(): # create dictionary of all vocab words
    wordlist = [line.strip().lower() for line in open('words.txt')]
    return wordlist

def help_load(A,B,C,D,dict): # helper to create neighbors dictionary
    others = B+C+D
    for word1 in A:
        curr = []
        for word2 in others:
            curr.append(word2)
        dict[word1] = curr
    return dict

def load_dict (N,E,S,W):
    neighbors = {}
    neighbors = help_load(N,E,S,W,neighbors)
    neighbors = help_load(E,N,S,W,neighbors)
    neighbors = help_load(S,N,E,W,neighbors)
    neighbors = help_load(W,N,E,S,neighbors)

    return neighbors # load all reachable letters dictionary

def clean_list (wordlist, neighbors): # clean for valid words for letterboxed
    clean_words = []
    for word in wordlist:
        add = True
        for i in range(len(word)): # go through all word characters
            if word[i] not in neighbors: # if not letter on board
                add = False
            elif i != len(word) - 1 and word[i+1] not in neighbors[word[i]]: # letter is valid, but next is not a valid neighbor
                add = False
        if add:
            clean_words.append(word)
    return clean_words

def execute(N,E,S,W): # print all pairs of valid words

    neighbors = load_dict(N,E,S,W)
    wordlist = clean_list(make_dict(),neighbors)

    wordlist.sort(key = lambda s: len(s),reverse=True) # sort decreasing - longest first


    start_index1 = 0

    while start_index1 < len(wordlist): # for each word1, find other valid words

        word1 = wordlist[start_index1]

        letterset1 = set() # unique letters in first word
        for char in word1:
            letterset1.add(char)


        for j in range(len(wordlist)): # find second words

            word2 = wordlist[j]

            letterset2 = set()
            for char in word2:
                letterset2.add(char)

            letterset = letterset1|letterset2 # combine

            for char in word2:
                all_in = True
                for char in neighbors:
                    if char not in letterset:
                        all_in = False # make sure every letter exists
            if all_in and (word1[-1] == word2[0]):
                print(word1,word2)

        start_index1 += 1

# example board
N = ['y','n','d']
E = ['r','c','p']
S = ['u','o','l']
W = ['j','i','a']

N = [e.lower() for e in N]
E = [e.lower() for e in E]
S = [e.lower() for e in S]
W = [e.lower() for e in W]

execute(N,E,S,W)
