# # This is a comment

# name = "David"
# last = 'Desilvey'
# age = 29
# weight = 183
# happy = True  # false
# something = []

# print("Hello World")
# print(age+1)
# print(name*3)
# # print(name+1)
# print(name+last)
# print(name+" "+last)
# print(f"{name} {last}")


# def say_hello():
#     print("Hi!!")
#     print("This is inside the function")

# say_hello()


# n = int(input('How many times do you want to repeat the message'))

# for i in range(n):
#     print(f"Hello world!. {i} " )

elements = ["a", "b", "c", "a"]

print(elements[0])

#range(4) ---->[0,1,2,3]
print("Slower form")
for i in range(4):
    print(elements[i])

print("Cooler form")
for e in elements:
    print(e)


    me = {
        "first": "David",
        "last": "Desilvey",
        "age": "29"
    }

    print( me["first"] )