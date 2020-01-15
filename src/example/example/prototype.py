# -*- coding: utf-8 -*-
import argparse
from configobj import ConfigObj
from .ModelExample import ModelExample

model = None 


def init_model(config):
    global model
    model = ModelExample(config)


def extractor(a=0, b=1, types='sum'):
    res = model(a, b, types)
    result = dict()
    result[types] = res
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('a', help='first value')
    parser.add_argument('b', help='second value')
    parser.add_argument('--config', default = None, help='path to the config file in json format')
    parser.add_argument('--type', default = 'sum', help='extion type', choices=['sum', 'prod'])
    namespace = parser.parse_args()
    argv = vars(namespace)

    if argv['config'] is not None:
        config = ConfigObj(infile=argv['config'], encoding='utf-8')
    else:
        config = None

    init_model(config)
    
    result = extractor(int(argv['a']), int(argv['b']), argv['type'])
    
    print(result)