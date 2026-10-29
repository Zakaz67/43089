prompt = "\nвыбери начинку для пиццы:"
prompt += "\nEnter 'quit' to end the program. "
print(prompt)
message = ""
while message != quit:
    message = input("начинка для пиццы:")
    print("начинка добавлеан")
    if message == "quit":
        break
