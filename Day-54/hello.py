# from flask import Flask

# app = Flask(__name__)

# @app.route("/") #using decorator function here "@"
# def hello():
#     return "Hello, Flask!"

# @app.route("/Bye")
# def bye():
#     return "Bye"


# if __name__ == "__main__":
#     app.run()
# #---------------------


##decorator function
import time
# current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 



def speed_calc_decorator(function):
    def execute_time_check():
        current_time = time.time()
        function()
        after_run_time = time.time()
        print(f"{function.__name__} run speed: {after_run_time-current_time}")
    return execute_time_check
      
@speed_calc_decorator
def fast_function():
    
    for i in range(1000000):
        i * i

        
@speed_calc_decorator
def slow_function():
    
    for i in range(10000000):
        i * i
        
        
fast_function()
slow_function()