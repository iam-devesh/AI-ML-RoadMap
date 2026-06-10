# Write a function that takes a number and returns whether it's even or odd.
def check_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(4))

# Loop through a list of numbers and print only the ones greater than 10.
list=[1,23,4,5,67,12,43,15,16]
for num in list:
    if num>10:
        print(num)


# FizzBuzz: print numbers 1–50, but "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both. (Classic — every coder does this.)
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
# Write a function that takes a list and returns its max value without using max().
def max(list):
    max=0
    for i in list:
        if i>max:
            max=i
    return max
print(max(list))

# Use a while loop to keep asking for input until the user types "quit".
while(input()!="quit"):
    print("You typed :"+input())

# Mini-challenge: write a function that takes a sentence and returns a dictionary counting each word — but this time wrap yesterday's logic in a reusable function with a return

def count_words(sentence):
    frequency={}
    for words in sentence.split():
        if words in frequency:
            frequency[words]+=1
        else:
            frequency[words]=1
    return frequency
print(count_words("hello world hello world"))