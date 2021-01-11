# -*- coding: utf-8 -*-

from TM1py.Objects.TM1Object import TM1Object
from TM1py.Objects.Deployment import Deployment

class TM1Project(TM1Object):
    """ Abtraction of TM1Project
    """

    def _init_(self, deployments : List[Deployment]):
        self.deployments = deployments