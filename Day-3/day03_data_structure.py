#Take yesterday's "print numbers > 10" loop and rewrite it as a one-line list comprehension.
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
arr2=[x for x in arr if x>10]
print(arr2)
#Build a list of squares for even numbers 1–20 using a comprehension with a condition.
arr=[x**2 for x in range(1,21) if x%2==0]
print(arr)
#Convert a list of words into a dict mapping each word to its length, using a dict comprehension.
words=["apple","banana","orange"]
dict={word:len(word) for word in words}
print(dict)
#Write a function that divides two numbers but catches division by zero and returns a friendly message.
def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Friendly message: You can't divide by zero!")
print(divide(2,0))

#Write code that tries to convert a list of strings to integers, skipping any that fail (e.g., ["1", "2", "abc", "4"]).
list=["1", "2", "abc", "4"]
list2=[int(i) for i in list if i.isdigit()]
print(list2)
#Mini-challenge: rewrite your word-counting function from Day 1/2 using a dict comprehension or a cleaner approach, and wrap it in try/except so it handles non-string input gracefully
def word_count(words):
    try:
        return {word:words.count(word) for word in words.split()}
    except TypeError:
        print("Error: Input must be a list of strings")
        return {}
print(word_count("hi how are you you"))