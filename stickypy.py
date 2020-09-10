"""
	Calling the "print" function will add the text to the clipboard
	Just importing will apply this effect
	Call stickypy.STICKY.restore() to deactivate
"""

import os, sys

import functools

import tempfile

import builtins

class Sticky:

	def __init__(self):
		self.Tfile = tempfile.NamedTemporaryFile(mode='w', encoding='UTF-16-LE', prefix='StickyPy', suffix='.txt')
		self.file = self.Tfile.file
		self.tab_file()

		self.ur_print = builtins.print
		builtins.print = self.__deco__(builtins.print)


	def tab_file(self):
		self.file.close()
		self.file = open(self.Tfile.name, 'w')


	def __deco__(self, func):

		@functools.wraps(func)
		def wrapper(*args, **kwargs):

			func(*args, **kwargs, end='', file=self.file)

			self.file.close()

			with open(self.Tfile.name) as f:
				func(f.read())

			os.system(f"CLIP < {self.Tfile.name}")

			self.tab_file()

		return wrapper


	def restore(self):
		builtins.print = self.ur_print


	def __del__(self):
		self.restore()
		self.file.close()
		os.unlink(self.Tfile.name)


print('\n\tStickyPy is imported\n')

STICKY = Sticky()

