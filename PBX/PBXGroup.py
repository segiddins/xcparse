from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *
from .PBX_Base_Reference import *

class PBXGroup(PBX_Base_Reference):
    # name = '';
    # path = '';
    # children = [];
    
    def __init__(self, lookup_func, dictionary, project, identifier):
        self.identifier = identifier;
        self.name = None;
        self.fs_path = None;
        # has 'path' only if it has an assigned location
        self.path = None;
        if 'path' in dictionary.keys():
            self.path = Path(dictionary['path'], '');
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'children' in dictionary.keys():
            self.children = self.parseProperty('children', lookup_func, dictionary, project, True);
        if 'sourceTree' in dictionary.keys():
            self.sourceTree = dictionary['sourceTree'];
        