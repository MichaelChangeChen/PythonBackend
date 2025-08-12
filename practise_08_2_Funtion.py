def callOne(a, *b):
	print(f'a=> {a}, b=> {b}')

def callTwo(a, **b):
	print(f'a=> {a}, b=> {b}')

callOne(1, 2, 3, 4, 5, 6)
callTwo(a=1, b=2, c=3, d=4)
