def square():
    for i in range(1,21):
        yield i*i

gen=square()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)




































