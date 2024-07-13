def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")#before Execution
        fx(*args, **kwargs)
        print("Thanks for using this function")#After Execution
    return mfx
@greet
def hello():
    print("Hello WORLD")
@greet
def add(a,b):
   print(a+b)


hello()
add(1,2)

