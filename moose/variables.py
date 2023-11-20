#!/usr/env/python3

from enum import IntEnum, auto

class Order(IntEnum):
    CONSTANT = auto()
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()

class Family(IntEnum):
    LAGRANGE = auto()
    MONOMIAL = auto()
    HERMITE = auto()
    SCALAR = auto()
    HIERARCHIC = auto()
    CLOUGH = auto()
    XYZ = auto()
    SZABAB = auto()
    BERNSTEIN = auto()
    L2_LAGRANGE = auto()
    L2_HIERARCHIC = auto()
    NEDELEC_ONE = auto()
    LAGRANGE_VEC = auto()
    MONOMIAL_VEC = auto()
    RATIONAL_BERNSTEIN = auto()
    SIDE_HIERARCHIC = auto()
    
class Variable():
    def __init__(self, name = "", order = 1, family = 1, block = "", vartype=None):
        self.name = name
        self.order = Order(order)
        self.family = Family(family)
        self.block = block
        self.type = vartype

    def __str__(self):
        string = f'[{self.name}]\n'
        if self.type:
            string += f'type = {self.type}\n'
        string += f'order = {self.order.name}\n'
        string += f'family = {self.family.name}\n'
        if self.block:
            string += f'block = "{self.block}"\n'
        string += f'[]\n'
        return string

class AuxVariable(Variable):
    def __init__(self, name = "", order = 1, family = 1, block = "", vartype=None):
        super().__init__(name,order,family,block,vartype)

class Variables():
    def __init__(self):
        self.name = "Variables"
        self.variables = {}

    def add_variable(self, name, order, family, block, vartype=None):
        variable = Variable(name=name,order=order,family=family,block=block,vartype=vartype)
        if variable.name in self.variables.keys():
            print("variable name already in use")
            
        self.variables[variable.name] = variable

    def __str__(self):
        string = f'[{self.name}]\n'
        for variable in self.variables.keys():
            string += self.variables[variable].__str__()
        string += f'[]\n'
        return string

class AuxVariables(Variables):
    def __init__(self):
        super().__init__()
        self.name = "AuxVariables"    
