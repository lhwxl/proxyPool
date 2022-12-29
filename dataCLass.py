class Data:
	def __init__(self, data: list):
		self.data = list()
		if len(data) == 2 and isinstance(data[0], str) and isinstance(data[1], str):
			if isinstance(data[0], str) and isinstance(data[1], str):
				self.data.append([data[0], data[1]])
			else:
				raise ValueError("列表参数必须都是str")
		else:
			for item in data:
				if len(item) == 2 and isinstance(item[0], str) and isinstance(item[1], str):
					self.data.append([data[0], data[1]])
				else:
					raise ValueError("子列表元素个数必须是偶数并且等于2个")
	
	
	def __len__(self):
		return len(self.data)
	
	
	def __add__(self, other: "Data"):
		return Data(self.data + other.data)
	
	
	def __iadd__(self, other: "Data"):
		self.data += other.data
	

	def getData(self):
		return self.data
	