import sys
import string
import random
import time

#1) BruteForce (Naive) algorithm
def naive_search(text, substring):
    n = len(text)
    m = len(substring)
    i = 0
    j = 0
    
    while not(j >= m) and not(i >= n-m):
        
        j = 0
        while not(j >= m) and text[i+j] == substring[j]:
            j += 1
        
        i += 1
        
    
    if not(j >= m):
        return -1
    else:
        return i-1
    


#2) Rabin-Karp algorithm
def rabin_karp_search(text, substring):
    n = len(text)
    m = len(substring)
    
    substringSum = 0
    for i in range(m):
        substringSum += ord(substring[i])
#    i; # index for text
#    j # index for substring
#count initial (i==0) ctrlSum for text[0..m-1]
    ctrlSum = 0
    for k in range(m):
        ctrlSum += ord(text[k])
    
    
    for i in range(n-m): #i = 0 .. n-m-1
       
        if ctrlSum == substringSum:  
#            print "Ctrl sums coincide"
#           check character be character:
            j = 0
            while not(j >= m) and text[i+j] == substring[j]:
                j +=1
            
            if j >= m: #found
                return i
#
#       count ctrlSum for text[i..i+m-1]
        ctrlSum = ctrlSum - ord(text[i]) + ord(text[i+m])

    return -1


#main code
if len(sys.argv) == 4:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    iters = int(sys.argv[3])
    
else:
    print """
Usage:

    python substring_search.py [text_length] [substring_length] [num_iters]

Example:

    python substring_search.py 10000 3 100
"""
    sys.exit(-1)
    

alphabet = string.ascii_uppercase


text = ""
substring = [""] * iters

#filling the text & substring
print "Start creating text(1) and substrings(%r)..." % iters

for i in range(n):
    text += random.choice(alphabet)


for k in range(iters):
    
    for i in range(m):
        substring[k] += random.choice(alphabet)


#search substring in text
pos = [None] * iters

#1) BruteForce (Naive) algorithm
print "Start bruteforce searching..."
start = time.time()

for k in range(iters):
    pos[k] = naive_search(text, substring[k])

print "Mean BruteForce time per 1 search: %s sec \n"  % ( (time.time() - start) / iters )
print pos
print



ctrlPos = [None] * iters
#2) Rabin-Karp (control sum) algorithm
print "Start Rabin-Karp searching..."
start = time.time()


for k in range(iters):
    ctrlPos[k] = rabin_karp_search(text, substring[k])


print "Mean Rabin-Karp time per 1 search: %s sec \n"  % ( (time.time() - start) / iters )
print ctrlPos



if pos == ctrlPos:
    print "OK"
else:
    print "[!] Error: pos != ctrlPos "

