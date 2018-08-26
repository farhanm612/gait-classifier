from Person import Person
from ExtractFeatures import Features
import os
import pylab as pl
from Frames import Frames
import numpy as np
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from Server import Server
import math
from gait_cycle import Gait_Cycle
class Reading_Files:

    def __init__(self):

        self.fpath = ('/Training')
        self.Pdata = list()
        self.Tdata = list()
        self.Features_obj = list()
        self.Body_Features = list()
        self.Super_Label = list()
        self.length = 0
        self.T_Features_obj = list()
        self.T_Body_Features = list()
        self.person_label_dict = dict()
        self.Super_Label = list()
        #self.clf = SVC(decision_function_shape='ovr')
        self.clf = KNeighborsClassifier(n_neighbors=5, p=1, metric='minkowski', weights='distance')
        #self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
        self.Cycle = list()

    def reading(self):

        f = 0
        for (dirname, dirs, files) in os.walk(self.fpath):
            for x in dirs:
                ppath = os.path.join(self.fpath,x)
                self.Pdata.append(Person(x,ppath))

        length = self.Pdata.__len__()
        print "Total Person Data: ", length
        for x in range(length):
            obj = Gait_Cycle(self.Pdata[x])
            obj.Calculate_cycles()
            self.Cycle.append(obj)


        for x in range(length):
            obj = Features(self.Pdata[x],self.Cycle[x])
            self.Features_obj.append(obj)
            self.Features_obj[x].Calculate_F()
        for x in range(length):
            print "Calculated Features of Cycle: ", len(self.Features_obj[x].Features_data)


        for x in range(length):
            F_length = self.Features_obj[x].Features_data.__len__()
            data = self.Features_obj[x].Features_data
            for y in range(F_length):
                a = data[y]
                self.Body_Features.append(a)

        for x in range(length):
            p_len = self.Cycle[x].person_cycle_size
            name = self.Pdata[x].name
            self.person_label_dict[name] = x
            last = p_len
            temp = list()
            temp = [x] * last
            self.Super_Label = self.Super_Label + temp


        #print "collective sum: ", len(self.Super_Label)
        #print "Fisrt Count: ", self.Super_Label.count(0)
        #self.clf.fit(self.Body_Features,self.Super_Label)
        #scores = cross_val_score(self.clf, self.Body_Features, self.Super_Label, cv=20)
        #print "Accuracy SVM", scores.mean()
        #neigh = KNeighborsClassifier(n_neighbors=3)
        #self.Normalization_Features()
        print "Feature Size: ", len(self.Body_Features)
        print "Label: ", len(self.Super_Label)
        self.clf.fit(self.Body_Features, self.Super_Label)
        scores = cross_val_score(self.clf, self.Body_Features, self.Super_Label, cv=20)
        print "Accuracy KNN", scores.mean()
        print scores

    def Run_time_Predict(self,feature):
        maxi = 0
        index = 0
        label_predicted = self.clf.predict(feature)
        label_predicted = label_predicted.tolist()
        probabilities = self.clf.predict_proba(feature)
        print "Labels predicted: ", label_predicted
        print "Probabilities: ", self.clf.predict_proba(feature)
        print "Length of Testing:", len(label_predicted)
        d2 = dict((v, k) for k, v in self.person_label_dict.iteritems())
        maxi = 0
        index = 0
        for x in range(len(label_predicted)):
            d = self.cal_maximum(probabilities[x])
            if d[0] > maxi:
                maxi = d[0]
                index = d[1]
            print "Maximum and index: ", d
        print maxi
        if maxi > 0.60:
            identified = d2[index]
        else:
            identified = "Unknown"
        print "Detected Name: ", identified

        #name = ""
        name = identified
        Faculty = "FCSE"
        notification = Server()
        notification.send_to_server(name, Faculty)

    def cal_maximum(self, probabilites):
        maxi = 0
        index = 0
        for x in range(len(probabilites)):
            if probabilites[x] > maxi:
                maxi = probabilites[x]
                index = x
        return (maxi, index)

    def Normalization_Features(self):
        length = self.Pdata.__len__()
        first = 0
        last = 0
        for x in range(length):
            p_len = self.Cycle[x].person_cycle_size
            last = last + p_len
            peson_features = self.Body_Features[first:last]
            print peson_features[0]
            feature_Set_size = len(peson_features[0])
            for x in range(feature_Set_size):
                list = [k[x] for k in peson_features]
                mini = min(list)
                for y in range(p_len):
                    list[y] = list[y] - mini
                maxi = max(list)
                for z in range(p_len):
                    list[z] = list[z]/maxi
                    list[z] = list[z] * 1000.0
                print "Max: ",max(list)
                print "Min: ",min(list)
                print list
                break
            print "Feature set Size: ", feature_Set_size
            print "Size: ", len(peson_features)
            list = [x[0] for x in peson_features]
            print"Features: " , max(list), min(list)