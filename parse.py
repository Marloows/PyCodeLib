import sys

def parse_argv(argv):
	"""
		Parse argv
		Returns args, kwargs, path
		Similar to python arg, kwarg structure
		The return value path is path of the __main__ 
	"""
	path = argv[0]
	
	args, kwargs = list(), dict()

	index = 0

	for x in argv[1:]:
		if x.startswith('-'):
			break
		args.append(x)
		index += 1
	else:
		# args should be a tuple
		return (*args,), kwargs, path	# No kwargs

	args = *args,

	kwargs[(tmp := argv[(index := index + 1)].strip('-'))] = list()

	for x in argv[index:]:
		if not x.startswith('-'):
			kwargs[tmp].append(x)
		else:
			# Clean up kwargs[tmp]
			if (ln := len(kwargs[tmp])) > 1:
				kwargs[tmp] = *kwargs[tmp],
			elif ln == 1:
				kwargs[tmp] = kwargs[tmp][-1]
			else:
				kwargs[tmp] = True
		
			kwargs[(tmp := x.strip('-'))] = list()

	if (ln := len(kwargs[tmp])) > 1:
		kwargs[tmp] = *kwargs[tmp],
	elif ln == 1:
		kwargs[tmp] = kwargs[tmp][-1]
	else:
		kwargs[tmp] = True

	return args, kwargs, path

def main():
	pass

if __name__ == '__main__':
	main()

