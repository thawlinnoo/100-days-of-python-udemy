# from flask import Flask

# app = Flask(__name__)


# def make_bold(function):
#     def decorator():
#         result = function()
#         return f"<b>{result}</b>"
#     return decorator

# def make_emphasis(function):
#     def decorator():
#         result = function()
#         return f"<em>{result}</em>"
#     return decorator

# def make_underline(function):
#     def decorator():
#         result = function()
#         return f"<u>{result}</u>"
#     return decorator





# @app.route("/") #using decorator function here "@"
# def hello():
#     return "<h1 style='text-align: center'>Hello, Flask!</h1>" \
#     "<p>This is paragraph</p>" \
#     "<img src='https://media.tenor.com/M5Mq4GCqikAAAAAM/wagging-wagging-tail.gif'>"

# @app.route("/Bye")
# @make_bold
# @make_emphasis
# @make_underline
# def bye():
#     return "Bye"

# @app.route("/greet/<name>/<int:age>")
# def greet(name, age):
#     return f"Hello {name}. you are {age} years old"


# if __name__ == "__main__":
#     app.run(debug=True)



#---------------------------

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
        

# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"Your name is {user.name}")

# new_user = User("thaw")
# new_user.is_logged_in = True
# create_blog_post(new_user)

#--------------------


# def hello():
#     print("Hello")


# def test():
#     return hello

# result = test()
# result()
# print(result)


# def hello():
#     print("Hello")


# def test():
#     return hello()

# result = test()
# print(result)

def logging_decorator(function):

    def wrapper(*args):

        print(f"You called {function.__name__}{args}")

        result = function(*args)

        print(f"It returned: {result}")

        return result

    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

x = a_function(1,2,3)
print(x)