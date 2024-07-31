def text_function():
    print("i'm creating a function")


# calling function
text_function()


# function with parameters
def writing_text(text):
    print(text)


# calling function
writing_text("this is laptop")


# funstion with if elif else
def school_calculator(age):
    if age >= 5 and age <= 18:
        print("you are in school")
    elif age >= 19 and age <= 65:
        print("you are in college")
    else:
        print("you are not in school or college")


# calling function
school_calculator(4)
school_calculator(15)
school_calculator(88)


# future age function
def future_age(current_age, years):
    future_age = current_age + years
    print(future_age)
    # return future_age


# calling function
future_age(25, 20)
