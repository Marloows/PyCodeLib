import os

ListWrapper = "{0} = [\n{1}\n]"
TupleWrapper = "{0} = (\n{1}\n)"

VarName = 'MyVar'

DefaultExport = 'tuple'


def process_element(x):
	
	if isinstance(x, str):
		x = f'"{x}"'

	return f'{x}'

def get_iter_content(var, line_buffer, sep, sep_buffer, sep_lines, new_line_buffer):
	
	content = new_line_buffer

	sep_buffer = sep + sep_buffer

	get_line = lambda index, line: sep_buffer.join(process_element(x) for x in var[index:index+line])

	length = len(var)

	get_line_length = lambda index: line_buffer if (e := length-index) > line_buffer else e

	new_line_buffer = sep + sep_lines + new_line_buffer

	new_line_buffer = f'{new_line_buffer}' + '{}'

	get_new_line = lambda line : new_line_buffer.format(line)

	# first line

	index = 0

	line = get_line_length(index)

	line = get_line(index, line)

	index += line_buffer

	content += line

	while index < length:
		line = get_line_length(index)

		line = get_line(index, line)

		index += line_buffer

		content += get_new_line(line)
	
	return content


def export_as_tuple(var, var_name, line_buffer, sep, sep_buffer, sep_lines, new_line_buffer, **kwargs):
	
	content = get_iter_content(var, line_buffer, sep, sep_buffer, sep_lines, new_line_buffer)
	
	return TupleWrapper.format(var_name, content)


def export_as_list(var, var_name, line_buffer, sep, sep_buffer, sep_lines, new_line_buffer, **kwargs):
	
	content = get_iter_content(var, line_buffer, sep, sep_buffer, sep_lines, new_line_buffer)
	
	return ListWrapper.format(var_name, content)


AS_FUNC = {
	'list': export_as_list, 'tuple': export_as_tuple
}

class ExportList(dict):
		

	def __init__( self, var, file_name = 'varlib', ext = 'py',
	
		export_as = 'tuple', mode = 'w',	

		var_name = 'MyVar', line_buffer = 7,
	
		sep = ',', sep_buffer = ' ', encoding = 'utf-8',

		sep_lines = '\n', new_line_buffer = '\t\t', reveal_afterwards = True

	):
		self.var = self.parse_var(var)
		
		self.file_name = self.parse_file_name(file_name, ext)

		self.path = self.parse_path()

		self.mode = self.parse_mode(mode)

		self.export_func = self.parse_export_func(export_as)

		self.var_name = self.parse_var_name(var_name)

		self.line_buffer = line_buffer

		self.sep = sep

		self.sep_buffer = sep_buffer

		self.encoding = encoding

		self.sep_lines = sep_lines
		self.new_line_buffer = new_line_buffer

		self.reveal_afterwards = reveal_afterwards


	def __setattr__(self, name, value):
		self[name] = value

	def __getattr__(self, name):
		return self[name]

	# Parse Func

	def parse_var(self, var):

		if not hasattr(var, '__iter__') or isinstance(var, str):
			var = (var, )

		return var

	def parse_file_name(self, file_name, ext):
		return file_name if '.' in file_name else f"{file_name}.{ext}"

	def parse_path(self):
		return os.path.abspath(self.file_name)

	def parse_mode(self, mode):
		return mode

	def parse_export_func(self, export_as):
		if export_as not in AS_FUNC.keys():
			export_as = DefaultExport
		return AS_FUNC[export_as]

	def parse_var_name(self, var_name):
		if isinstance(var_name, str):
			pass
		elif hasattr(self.var, '__name__'):
			var_name = var.__name__
		else:
			var_name = VarName

		return var_name

	def export(self):
		content = self.export_func(**self)
		self.write(content)

	def write(self, content):
		with open(self.path, self.mode, encoding = self.encoding) as file:
			file.write(content)			

	def checks(self):
		if self.reveal_afterwards:
			os.system(f'code "{self.path}"')

	def __del__(self):
		self.export()
		self.checks()
		del self

