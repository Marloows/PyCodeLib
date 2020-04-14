import os, sys, contextlib

from functools import wraps

class Stdout:

	def __init__(self,
		file_name = 'out.txt', mode = 'w',
			reveal = False, reveal_in = 'code',
				reveal_at_location = False,
					encoding ='utf-8', append = False,
				):

		self.file_name = file_name
		self.mode = 'a' if append else mode
		self.encoding = encoding
		self.URZUSTAND = sys.stdout	 # to be used when the S-Object is deleted
		self.stdout = self.open_file()
		self.file = self.stdout
		self.reveal_in = reveal_in
		self.reveal = reveal
		self.reveal_at_location = reveal_at_location
		self.file_path = os.path.abspath(file_name)


	def __enter__(self):
		self.switch()
		return self	 # enter always have return not yield
	

	def __exit__(self, *args):
		# *args = exc_type, exc_value, traceback
		self.file.flush()
		self.reset()

	def __call__(self, *args):
		
		# calling S-Object to be a decoratore
		if len(args) == 1:
			return self.__deco__(*args)
	
		# mainly calling without argument create a switch
		self.switch()

	def __deco__(self, func):
		
		@wraps(func)
		def first_wrapper(*args, **kwargs):

			with self:
				re_value = func(*args, **kwargs)

			return re_value
			
		return first_wrapper


	# switch back and forth between standard and file output each time __call__ is appears without args
	def switch(self):
		sys.stdout, self.stdout = self.stdout, sys.stdout

	def checks(self, call_r = '{} {}', call_l = '{} {}'):
		if self.reveal:
			os.system(call_r.format(self.reveal_in, self.file_path))
		
		if self.reveal_at_location:
			os.system(call_l.format('explorer ', os.getcwd()))

	def open_file(self):
		return open(self.file_name, self.mode, -1, self.encoding)

	def tab_file(self):
		with open(self.file_name) as file:
			pass
		return file
	
	def empty_file(self):
		with open(self.file_name, 'w') as file:
			file.write('')
		return file

	def reset(self):
		if sys.stdout != self.URZUSTAND:
			self.switch()

	def __del__(self):
		self.file.close()
		self.checks()
		self.reset()
		


