from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *
from .PBX_Base import *

class PBX_Base_Phase(PBX_Base):
    
    def __init__(self, lookup_func, dictionary, project):
        self.name = 'PBX_BASE_PHASE';
        
    def performPhase(self):
        print 'implement me!';