#!/usr/bin/python3
"""This moduloe defines BaseModel Class"""
from datetime import datetime
import uuid

class BaseModel():
	"""This is the basemodel definition"""
	def __init__(self, *args, **kwargs):
		if not kwargs:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
		else:
			for k, v in kwargs.items():
				if k != "__class__":
					if k in ['created_at', 'updated_at']:
						format_date = "%Y-%m-%dT%H:%M:%S.%f"
						setattr(self, k, datetime.strptime(v, format_date))
					else:
						setattr(self, k, v)
		
	def __str__(self):
		return ("[{}] {} {}".format(type(self).__name__, self.id, self.__dict__))

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		new_dict = self.__dict__.copy()
		new_dict['__class__'] = type(self).__name__
		for k, v in new_dict.items():
			if k in ['created_at', 'updated_at']:
				new_dict[k] = v.isoformat()
		return new_dict
