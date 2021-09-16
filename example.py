from ArgumentProcesser import ArgumentProcesser

def handler_fn(update, context, args):
    print(args)

def main():
	# fake vars for testing
	command = '/hello @pippo false'
	update = 1
	context = 2

	# list of options
	options = [
		("", [], handler_fn),
		("user bool", [], handler_fn),
		("int", [], handler_fn)
	]

	# effective code call
	ap = ArgumentProcesser(command, update, context)
	valid_command = ap.try_matches_execute(options)

	if not valid_command:
		print("Invalid command!")

main()
