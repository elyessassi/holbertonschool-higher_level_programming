#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	z = 0
	try:
		for i in range(x):
			print(my_list[i], end="")
			z = z + 1
		print("")
	except TypeError:
		return (z)
	except IndexError:
		print("")
		return (z)
	return (z)
