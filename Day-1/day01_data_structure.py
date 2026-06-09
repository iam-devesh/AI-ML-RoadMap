## create a list of 15 numbers; slice the first 5, last 3 and every other one
list=[1,2,3,4,4,5,6,6,7,7,8,9,9,10]
print(len(list))
print(list[0:5])
print(list[-1:-4:-1])
print(list)

## Build a dictionary describing yourself (name, age, hobbies, goal). Print each value.

dict={
    "name":"devesh",
    "age":21,
    "hobbies":["cricket","reading","coding"],
    "goal":"sde"
}

for key,value in dict.items():
    print(key,":",value)

## Take a list with duplicates and use a set to remove them
print(set(list))

## Make a tuple and try to change an element — see the error, understand 
# tuple=(1,2,3,4,5)
# print(tuple)
# tuple[0]=2
# print(tuple)

words=["apple","banana","cherry","dragonfruit","orange","apple"]
frequency={}
for i in words:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)