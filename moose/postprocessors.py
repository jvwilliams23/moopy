#!/usr/env/python3

from enum import IntEnum, auto

class PostProcessorTypes(IntEnum):
    NodalExtremeValue = auto()
    ElementExtremeValue = auto()    
    ElementAverageValue = auto()  
    PressureDrop = auto()

class PostProcessor():
    def __init__(self, name = "", **kwargs):
        self.name = name

        # set the kwargs into names        
        for arg in kwargs.keys():
            self.__setattr__(arg, kwargs[arg])

    def __str__(self):
        string =  f'[{self.name}]\n'
        string += f'type={self.type.name}\n'
        
        objects = ["name", "type"]
        
        for key in self.__dict__.keys():
            if key not in objects:
                data = self.__dict__[key]
                if isinstance(data,list):
                    if hasattr(data[0], '__dict__'):
                        data = [x.name for x in data]
                    else:
                        data = [str(x) for x in data]
                    data = ' '.join(data)
                if hasattr(data, '__dict__'):
                    data = data.name
                string += f'{key}="{data}"\n'

        string += '[]\n'
        return string

class NodalExtremeValue(PostProcessor):
    def __init__(self, name = "", **kwargs):
        super().__init__(name,**kwargs)
        self.type = PostProcessorTypes.NodalExtremeValue

class ElementExtremeValue(NodalExtremeValue):
    def __init__(self, name = "", **kwargs):
        super().__init__(name,**kwargs)
        self.type = PostProcessorTypes.ElementExtremeValue

class ElementAverageValue(PostProcessor):
    def __init__(self, name = "", variable = None, block = "", **kwargs):
        super().__init__(name,**kwargs)
        self.type = PostProcessorTypes.ElementAverageValue

class PressureDrop(PostProcessor):
    def __init__(self, upstream_boundary, downstream_boundary, boundary, name = "", pressure = "p", **kwargs):
        # super().__init__(upstream_boundary, downstream_boundary, boundary,name, pressure, **kwargs)
        super().__init__(name,**kwargs)
        self.upstream_boundary = upstream_boundary
        self.downstream_boundary = downstream_boundary
        self.boundary = boundary
        self.pressure = pressure
        self.type = PostProcessorTypes.PressureDrop

class PostProcessors():
    def __init__(self):
        self.name = "Postprocessors"
        self.post_processors = {}

    def __str__(self):
        string =  f'[{self.name}]\n'
        for key in self.post_processors.keys():
            string += self.post_processors[key].__str__()
        string += '[]\n'
        return string