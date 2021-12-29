"""
Created on Feb 26, 2021

@author: laurentmichel
"""
import unittest
import os

from astropy.io.votable import parse


data_path = os.path.dirname(os.path.realpath(__file__))
vpath = os.path.join(data_path, "test.7.xml")
votable = parse(vpath)
for resource in votable.resources:
    for resource_meta in resource.resources:
        print(resource_meta.type)
        print(resource_meta.mapping_block)
