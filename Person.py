import os
from Frames import Frames

class Person:

    def __init__(self,person,path=''):
        self.Fdata = []
        self.size = 0
        self.PersonPath = path
        self.name = person
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        if path!= '':
            self.extractfile()

    def extractfile(self):
        ppath = self.PersonPath
        #print self.name
        for (dirname, dir, files) in os.walk(ppath):
            for filename in files:
                self.readdata(filename,ppath)
        print self.Fdata.__len__()

    def readdata(self,filename,ppath):
        first = 1;
        last = 21;
        filename = os.path.join(ppath, filename)
        d_p = open(filename)
        data = d_p.readlines()
        line = data[0]
        #print line
        self.size += data.__len__()
        number = data.__len__()/20

        for x in range(number):
            frame = data[first:last]
            self.Fdata.append(Frames(frame,line))
            first = last
            last += 20


    def Run_time_data(self,data):
        first = 1;
        last = 21;
        self.size = data.__len__()/20
        number = self.size
        line = data[0]
        print line
        for x in range(number):
            frame = data[first:last]
            self.Fdata.append(Frames(frame,line))
            first = last
            last += 20