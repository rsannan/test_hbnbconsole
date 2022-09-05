#!/usr/bin/python3
"""This module defines file storage class"""
import json


class FileStorage():
	__file_path = ""
	__objects = {}

	def all(self):
		"""returns __objects attribute"""
		return self.__objects
	
	def new(self, obj):
		"""sets obj on __objects"""
		self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj.to_dict()
	
	def save(self):
		"""serializes __objects to JSON file"""
		with open(self.__file_path, mode="w", encoding="utf-8") as myfile:
			for k in self.__objects:
				json.dump(self.__objects.get(k), myfile)
	def reload(self):
		"""deserializes __objects in a json file"""
		try:
			with open(self.__file_path, mode="r", encoding="utf-8") as myfile:
				self.__objects = json.load(myfile)
			for k, v in json_file.items():
				self.__objects[k] = BaseModel()
		except FileNotFoundError:
			pass
