import time
 
begin = time.time()

words = ['apple', 'banana', 'pineapple', 'tomato', 'chicken']

print("Array of words = ",words)

searchword = "apple"
for i in range(len(words)):
    if searchword == words[i]:
        print("Word found at index = ", i)

print("The first word in the array is: ", words[0])
print("The last word in the array is: ", words[-1])
end = time.time()

print(f"Total runtime of the program is {end - begin}")