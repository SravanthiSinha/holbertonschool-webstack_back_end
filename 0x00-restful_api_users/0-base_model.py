#!/usr/bin/python3
"""
Test BaseModel class
"""
from models.base_model import BaseModel

base_model_1 = BaseModel()
print(base_model_1.id)
print(base_model_1.created_at)
print(base_model_1.updated_at)

base_model_2 = BaseModel()
print(base_model_2.id)
print(base_model_2.created_at)
print(base_model_2.updated_at)
