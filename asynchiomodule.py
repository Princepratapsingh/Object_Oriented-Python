import asyncio

# async def fn():
# 	print('This is ')
# 	await asyncio.sleep(1)
# 	print('asynchronous programming')
# 	await asyncio.sleep(1)
# 	print('and not multi-threading')

# asyncio.run(fn())
# import asyncio
# In the program below, we’re using await fn2() after the first print statement. It simply means to wait until the other function is done executing. So, first, it’s gonna print “one”, then the control shifts to the second function, and “two” and “three” are printed after which the control shifts back to the first function (because fn() has done its work) and then “four” and “five” are printed.



# async def fn():
	
# 	print("one")
# 	await asyncio.sleep(1)
# 	await fn2()
# 	print('four')
# 	await asyncio.sleep(1)
# 	print('five')
# 	await asyncio.sleep(1)

# async def fn2():
# 	await asyncio.sleep(1)
# 	print("two")
# 	await asyncio.sleep(1)
# 	print("three")
# asyncio.run(fn())

# import asyncio
async def fn():
	task=asyncio.create_task(fn2())
	print("one")
	#await asyncio.sleep(1)
	#await fn2()
	print('four')
	await asyncio.sleep(1)
	print('five')
	await asyncio.sleep(1)

async def fn2():
	#await asyncio.sleep(1)
	print("two")
	await asyncio.sleep(1)
	print("three")
	
asyncio.run(fn())
# Now if you want the program to be actually asynchronous, In the actual order of execution we’ll need to make tasks in order to accomplish this. This means that the other function will begin to run anytime if there is any free time using asyncio.create_task(fn2())
