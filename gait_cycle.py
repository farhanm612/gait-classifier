import math
import pylab as pl
import numpy as np
from Joints import Coord
from scipy.signal import argrelextrema
from peakdetect import peakdet
class Gait_Cycle:

    def __init__(self,person):
        self.Person = person
        self.Pcycles = list()
        self.person_cycle_size = 0

    def Calculate_cycles(self):
        Dankle = list()
        PersonFrames = self.Person.Fdata
        for x in xrange(len(PersonFrames)):
            each = PersonFrames[x].CompleteFrame
            distance = self.Horizontal_distance(each, 16, 17)
            Dankle.append(distance)
        x = xrange(0,Dankle.__len__(),1)
        #print max(Dankle)
        Norm = self.Moving_Average(Dankle)
        maximum,minimum = peakdet(Norm,0.2)
        if len(maximum) < 3:
            print "Not Enough Frames"
        else:
            cycle_frames = maximum[:,0]
            self.Calculate_Half_Cycle(cycle_frames)
            #if self.Person.name == "Testing" and len(cycle_frames) > 0:
                #pl.plot(x,Norm,'r')
                #pl.plot(maximum[:,0],maximum[:,1],'go')
                #pl.show()

    def distance_Feature(self,frame,x,y):
        P1  = frame[x].getXYZ()
        P2 = frame[y].getXYZ()
        value = math.sqrt(self.square(P1[0] - P2[0]) + self.square(P1[1] - P2[1]) + self.square(P1[2] - P2[2]))
        return value

    def Horizontal_distance(self,frame,x,y):
        P1 = frame[x].getXYZ()
        P2 = frame[y].getXYZ()
        value = math.fabs(P1[0]-P2[0])
        return value

    def square(self,x):
        return math.pow(x,2)

    def Moving_Average(self,Dankle):
        array = Dankle[:]
        array_len = array.__len__()
        for x in xrange(array_len):
            if(x > 1 and x < (array_len - 2)):
                array[x] = (array[x-2] + array[x-1] + array[x] + array[x+1] + array[x+2])/5

        return array

    def Calculate_Half_Cycle(self,Cycle_num):
        length = len(Cycle_num)
        if length > 0:
            for x in xrange(0,length - 1,2):
                if (x+2) < length:
                    self.Pcycles.append((Cycle_num[x], Cycle_num[x+2]))
            self.person_cycle_size = len(self.Pcycles)
            print "Length: ", len(self.Pcycles)


