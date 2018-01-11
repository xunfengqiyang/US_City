'''''
Created on 2018.1.11

@author: Jie Tan
'''


class Tv(object):

    def __init__(self):
        self.id = None
        self.Rank = None
        self.Market = None
        self.State = None
        self.Counties = None
        self.Households = None
        self.ABC = None
        self.CBS = None
        self.Fox = None
        self.NBC=None
        self.Other=None


    def getId(self):
        return self.id

    def setId(self,value):
        self.id=value

    def getRank(self):
        return self.Rank

    def setRank(self,value):
        self.Rank=value


    def getMarket(self):
        return self.Market

    def setMarket(self , value):
        self.Market = value


    def getState(self):
        return self.State

    def setState(self , value):
        self.State = value


    def getCounties(self):
        return self.Counties

    def setCounties(self , value):
        self.Counties=value

    def getHouseholds(self):
        return self.Households

    def setHouseholds(self , value):
        self.Households = value

    def getABC(self):
        return self.ABC

    def setABC(self, value):
        self.ABC = value

    def getCBS(self):
        return self.CBS

    def setCBS(self, value):
        self.CBS = value

    def getFox(self):
        return self.Fox

    def setFox(self, value):
        self.Fox = value

    def getNBC(self):
        return self.NBC

    def setNBC(self, value):
        self.NBC=value

    def getOther(self):
        return self.Other

    def setOther(self , value):
        self.Other = value
