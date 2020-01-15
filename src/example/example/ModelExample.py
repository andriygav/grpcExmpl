# -*- coding: utf-8 -*-
class ModelExample(object):
    def __init__(self, config):
        pass
    
    def extract(self, a=0, b=1, types='sum'):
    	if types=='sum':
    		return a+b
    	if types=='prod':
    		return a*b
    	return 0

    def __call__(self, a=0, b=1, types='sum'):
    	return self.extract(a, b, types)
