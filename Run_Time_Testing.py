from Person import Person
from ExtractFeatures import Features
from gait_cycle import Gait_Cycle

class Testing:

    def __init__(self, new):
        self.text= new
        print "Hello"
        self.line_Wise_data = list()
        self.Extract_data()
        self.Testing_Person = Person('Testing')
        self.Testing_Person.Run_time_data(self.line_Wise_data)
        self.Cycle_obj = Gait_Cycle(self.Testing_Person)
        self.Cycle_obj.Calculate_cycles()
        self.size = self.Cycle_obj.person_cycle_size
        #print "Testing Cycle Size: ", self.Cycle_obj.person_cycle_size
        self.Feature_obj = Features(self.Testing_Person,self.Cycle_obj)
        self.Feature_obj.Calculate_F()

    def Extract_data(self):
        f = 5
        l = 9
        split_list = self.text.split(';')
        temp = split_list[0:5]
        temp = ';'.join(temp)
        self.line_Wise_data.append(temp)
        length = split_list.__len__()
        length = length - 5
        length = length / 4

        for x in range(length):
            temp = split_list[f:l]
            temp = ';'.join(temp)
            self.line_Wise_data.append(temp)
            f = l
            l = l + 4

    def get_F(self):
        return self.Feature_obj.Features_data

