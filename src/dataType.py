class humanData:
    def __init__(self, x, y, idx):
		self.x = x
		self.y = y
		self.id = idx
		self.updated = False
		self.missing = False
		self.isSuspect = False
		self.itemList = []

	def update_position(self, nx, ny):
		self.x = nx
		self.y = ny


class itemData:
    def __init__(self, x, y, idx):
		self.x = x
		self.y = y
		self.id = idx
		self.updated = False
		self.missing = False
		self.alarm_flag = False
		
	def update_position(self, nx, ny):
		self.x = nx
		self.y = ny
