
import random

class Resource:
    def __init__(self, name, resource_type, cost):
        self.name = name
        self.resource_type = resource_type
        self.cost = cost
        

class Resource_Type:
    def __init__(self, name):
        self.name = name
