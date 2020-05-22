# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:35:58 2020

@author: eltronicsvilla
"""


#If you want to calculate the number of weights and biases in each layer without instantiating the model,
# you can simply load the raw file and iterate over the resulting collections.OrderedDict like so:
import torch

tensor_dict = torch.load('model.dat', map_location='cpu') # OrderedDict
tensor_list = list(tensor_dict.items())
for layer_tensor_name, tensor in tensor_list:
    print('Layer {}: {} elements'.format(layer_tensor_name, torch.numel(tensor)))
