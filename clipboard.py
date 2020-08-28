"""
	Add text to clipboard, input args will be concatenated
"""

import os

import sys

import tempfile

def align(S, t = "\t"):
	return t + ("\n"+t).join(S.splitlines())

def add_to_clipboard_one_liner(S):
	# s = S.replace('"', '\"')
	os.system(f'echo | set /p="{S}"|clip')
	return True


def encoded(S):
	return str(S).encode('UTF-16-LE')

def add_to_clipboard(S):
	with tempfile.NamedTemporaryFile(delete=False, prefix='pyclip', suffix='.txt') as file:
		file.write(encoded(S))

	try:
		os.system(f"CLIP < {file.name}")
	except:
		print("Something must have gone terribly wrong!!!")
	finally:
		os.unlink(file.name)

	return True


def add_to_clipboard_verbose(S):
	print(f"\n{align(S)}\n\nAdding to clipboard...\n")
	return add_to_clipboard(S)

def parse_args(argv = sys.argv):
	return " ".join(argv[1:])


def main():
	if len(sys.argv) < 2:
		print(__doc__)
		exit()

	S = parse_args()

	return add_to_clipboard_verbose(S)

if __name__ == "__main__":
	main()

