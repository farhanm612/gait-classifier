from Person import Person
from Frames import Frames
from Joints import Coord
from gait_cycle import Gait_Cycle
import scipy.stats
import numpy as np
import math

class Features:

    def __init__(self,person,cycle):
        self.Features_data = []
        self.Person = person
        self.Cycle = cycle
        self.thigh_R = 0
        self.thigh_L = 0
        self.thigh = 0
        self.calf_R = 0
        self.calf_L = 0
        self.calf = 0
        self.leg_L = 0
        self.leg_R = 0
        self.leg = 0
        self.upper_Arm_L = 0
        self.upper_Arm_R = 0
        self.lower_Arm_R = 0
        self.lower_Arm_L = 0
        self.Arm_L = 0
        self.Arm_R = 0
        self.Arm = 0
        self.Neck = 0
        self.shoulder_L = 0
        self.shoulder_R = 0
        self.hip_R = 0
        self.hip_L = 0
        self.hip = 0
        self.upper_spine = 0
        self.lower_spine = 0
        self.spine = 0
        self.hand_R = 0
        self.hand_L = 0
        self.foot_L = 0
        self.foot_R = 0
        self.Body_Height = 0
        self.elbow_distance = 0
        self.hand_distance = 0
        self.knee_distance = 0
        self.foot_distance = 0
        self.head_height = 0
    def Calculate_F(self):
        List_of_Frames = self.Person.Fdata
        Person_Cycles = self.Cycle.Pcycles
        list_size = len(Person_Cycles)
        for x in range(list_size):
            cycle_frames_count = Person_Cycles[x]
            first = int(cycle_frames_count[0])
            last = int(cycle_frames_count[1]) + 1
            cycle_frames = List_of_Frames[first:last]
            cycle_features = list()
            for y in range(len(cycle_frames)):
                    each = cycle_frames[y].CompleteFrame
                    #print each
                    self.thigh_R = self.Vertical_dist(each, 12, 14)
                    self.thigh_L = self.Vertical_dist(each, 13, 15)
                    self.thigh = (self.thigh_R + self.thigh_L)/2

                    self.calf_R = self.distance_Feature(each, 14, 16)
                    self.calf_L = self.distance_Feature(each, 15, 17)
                    self.calf = (self.calf_R + self.calf_L)/2

                    self.leg_L = self.thigh_L + self.calf_L
                    self.leg_R = self.thigh_R + self.calf_R
                    self.leg = (self.leg_L + self.leg_R)/2

                    self.upper_Arm_R = self.distance_Feature(each, 2, 4)
                    self.upper_Arm_L = self.distance_Feature(each, 3, 5)
                    self.lower_Arm_R = self.distance_Feature(each, 4, 6)
                    self.lower_Arm_L = self.distance_Feature(each, 5, 7)
                    self.Arm_R = self.upper_Arm_R + self.lower_Arm_R
                    self.Arm_L = self.upper_Arm_L + self.lower_Arm_L
                    self.Arm = (self.Arm_L + self.Arm_R)/2

                    self.Neck = self.distance_Feature(each, 0, 1)
                    self.shoulder_R = self.distance_Feature(each, 1, 2)
                    self.shoulder_L = self.distance_Feature(each, 1, 3)

                    self.hip_R = self.distance_Feature(each, 11, 12)
                    self.hip_L = self.distance_Feature(each, 11, 13)
                    self.hip = (self.hip_R + self.hip_L)/2

                    self.upper_spine = self.Vertical_dist(each, 1, 10)
                    self.lower_spine = self.Vertical_dist(each, 10, 11)
                    self.spine = self.lower_spine + self.upper_spine

                    self.hand_R = self.distance_Feature(each, 6, 8)
                    self.hand_L = self.distance_Feature(each, 7, 9)
                    self.foot_R = self.distance_Feature(each, 16, 18)
                    self.foot_L = self.distance_Feature(each, 17, 19)

                    self.elbow_distance = self.Horizontal_Distance(each, 4, 5)

                    self.hand_distance = self.Horizontal_Distance(each, 6, 7)
                    self.knee_distance = self.Horizontal_Distance(each, 14, 15)

                    self.foot_distance = self.distance_Feature(each, 18,19)
                    self.Body_Height = self.Body_Height_C(each)

                    self.V_height = self.Vertical_Feature(each, 0)
                    try:
                        right = self.Vertical_Feature(each, 2)
                        left = self.Vertical_Feature(each, 3)
                        self.V_Should = (right+left)/2
                        right = self.Vertical_Feature(each, 6)
                        left = self.Vertical_Feature(each, 7)
                        self.V_Wrist = (right+left)/2
                        right = self.Vertical_Feature(each, 16)
                        left = self.Vertical_Feature(each, 17)
                        self.V_Ankle = (right+left)/2
                        right = self.Vertical_Feature(each, 4)
                        left = self.Vertical_Feature(each, 5)
                        self.V_Elbow = (right + left) / 2
                        right = self.Vertical_Feature(each, 14)
                        left = self.Vertical_Feature(each, 15)
                        self.V_knee = (right + left) / 2
                        #right = self.Vertical_Feature(each, 8)
                        left = self.Vertical_Feature(each, 9)
                        self.V_hand = left
                    except:
                        print "Floor Plane Equation not Found"
                        exit()
                    angles_right = self.Calculate_Angle(each,12,14,16)
                    angles_left = self.Calculate_Angle(each,12,14,16)
                    self.Angle_R_hip_knee = angles_right[0]
                    self.Angle_R_knee_ankle = angles_right[1]
                    self.Angle_L_hip_knee = angles_left[0]
                    self.Angle_L_knee_ankle = angles_left[1]
                    #print angles
                    #self.Angle_hip_knee =
                    #Temp = self.getFeatures()
                    self.ankle_distance = self.Horizontal_Distance(each,16,17)
                    Temp = self.getVetical()
                    cycle_features.append(Temp)
                    #print cycle_features.__len__()
                    #print Temp.__len__()
            #print "Length: ", len(cycle_features)
            #print cycle_features[0]
            #print cycle_features[1]
            #print sum(x[13] for x in cycle_features)/len(cycle_features)
            #self.Cycle_Average(cycle_features)
            #print "New Length of Cycle frames: ", len(cycle_frames)
            length = len(cycle_frames)
            self.Cycle_Calculation(cycle_features,length)
            #Temp = Calculate_Avg(Temp)
            #self.Features_data.append(Temp)
        print "ENDED PERSON CYCLES"

    def Print_Size(self):

        return self.Person.Fdata.__len__()

    def Vertical_Feature(self, frame, p):
         try:
             A = frame[20]
             B = frame[21]
             D = frame[23]
             x = 0
             if A == 0:
                 A = -0.0231876
             if B == 0:
                 B = 0.9997158
             if D == 0:
                 D = 1.067132
             y = frame[p].Y
             num = math.fabs((A*x) + (B*y) + D)
             denum = math.sqrt(A*A + B*B)
             dist = num/denum
         except:
             print "Error: Floor Plane Equation Not detected"
             exit()
         else:
            return dist

    def Vertical_dist(self, frame, x, y):
        P1 = frame[x].getXYZ()
        P2 = frame[y].getXYZ()
        value = math.fabs(P1[1] - P2[1])
        return value

    def Calculate_Angle(self,frame,h,k,a):
        d_hip_knee = self.distance_Feature(frame,h,k)
        d_knee_ankle = self.distance_Feature(frame,k,a)
        d_hip_ankle = self.distance_Feature(frame,h,a)
        num = ((d_hip_ankle * d_hip_ankle) + (d_hip_knee * d_hip_knee)) - (d_knee_ankle * d_knee_ankle)
        denum = 2 * (d_hip_ankle) * (d_hip_knee)
        try:
            if denum > 0:
                value = num/denum
            else:
                value = 0
        except:
            print "Error division by zero unable to find Angle"
            exit()
        else:
            angle_hip_knee = math.acos(value)
            num = ((d_hip_ankle * d_hip_ankle) + (d_knee_ankle * d_knee_ankle)) - (d_hip_knee * d_hip_knee)
            denum = 2 * (d_hip_ankle) * (d_knee_ankle)
            value = num / denum
            angle_knee_ankle = math.acos(value)
            return [angle_hip_knee, angle_knee_ankle]

    def distance_Feature(self,frame,x,y):
        P1  = frame[x].getXYZ()
        P2 = frame[y].getXYZ()
        value = math.sqrt(self.square(P1[0] - P2[0]) + self.square(P1[1] - P2[1]) + self.square(P1[2] - P2[2]))
       # print value
        return value

    def Horizontal_Distance(self, frame, x, y):
        P1 = frame[x].getXYZ()
        P2 = frame[y].getXYZ()
        value = math.fabs(P1[0] - P2[0])
        return value

    def Cycle_Calculation(self, cycle_f,length):
        list = [x[0] for x in cycle_f]
        height_mean = np.mean(np.array(list))
        height_std = np.std(np.array(list))

        list = [x[1] for x in cycle_f]
        shoulder_mean = np.mean(np.array(list))
        shoulder_std = np.std(np.array(list))

        list = [x[2] for x in cycle_f]
        wrist_mean = np.mean(np.array(list))
        wrist_std = np.std(np.array(list))

        list = [x[3] for x in cycle_f]
        ankle_mean = np.mean(np.array(list))
        ankle_std = np.std(np.array(list))

        list = [x[4] for x in cycle_f]
        elbow_mean = np.mean(np.array(list))
        elbow_std = np.std(np.array(list))

        list = [x[5] for x in cycle_f]
        hand_mean = np.mean(np.array(list))
        hand_std = np.std(np.array(list))

        list = [x[6] for x in cycle_f]
        h_mean = np.mean(np.array(list))
        h_std = np.std(np.array(list))

        list = [x[7] for x in cycle_f]
        d_knee_mean = np.mean(np.array(list))
        d_knee_std = np.std(np.array(list))

        list = [x[8] for x in cycle_f]
        V_Elbow_mean = np.mean(np.array(list))
        V_Elbow_std = np.std(np.array(list))

        list = [x[9] for x in cycle_f]
        V_knee_mean = np.mean(np.array(list))
        V_knee_std = np.std(np.array(list))

        list = [x[10] for x in cycle_f]
        l_spine_mean = np.mean(np.array(list))
        l_spine_std = np.std(np.array(list))
        list = [x[11] for x in cycle_f]
        l_thigh_mean = np.mean(np.array(list))
        l_thigh_std = np.std(np.array(list))
        list = [x[12] for x in cycle_f]

        right_hip_knee_mean = np.mean(np.array(list))
        right_hip_knee_std = np.std(np.array(list))
        list = [x[13] for x in cycle_f]
        right_knee_ankle_mean = np.mean(np.array(list))
        right_knee_ankle_std = np.std(np.array(list))
        list = [x[14] for x in cycle_f]
        left_hip_knee_mean = np.mean(np.array(list))
        left_hip_knee_std = np.std(np.array(list))
        list = [x[15] for x in cycle_f]
        left_knee_ankle_mean = np.mean(np.array(list))
        left_knee_ankle_std = np.std(np.array(list))
        list = [x[16] for x in cycle_f]
        step_length = max(list)
        stride_length = step_length * 2
        time = float(length) / 20.0
        speed = stride_length/time
        list = [x[17] for x in cycle_f]
        V_hand_mean = np.mean(np.array(list))
        V_hand_std = np.std(np.array(list))
        list = [x[18] for x in cycle_f]
        l_calf_mean = np.mean(np.array(list))
        l_calf_std = np.std(np.array(list))
        list = [x[19] for x in cycle_f]
        l_upper_Arm_mean = np.mean(np.array(list))
        l_upper_Arm_std = np.std(np.array(list))

        list = [x[20] for x in cycle_f]
        r_upper_Arm_mean = np.mean(np.array(list))
        r_upper_Arm_std = np.std(np.array(list))

        array = np.array([shoulder_mean, shoulder_std, wrist_mean, wrist_std, ankle_mean,
                          ankle_std, hand_mean, hand_std, h_mean, h_std, d_knee_mean, d_knee_std,
                          V_Elbow_mean, V_Elbow_std, V_knee_mean, V_knee_std, l_spine_mean, l_spine_std, l_thigh_mean,
                          l_thigh_std, step_length, l_calf_mean, l_calf_std, height_mean, height_std, l_upper_Arm_mean, l_upper_Arm_std,
                          elbow_mean, elbow_std, r_upper_Arm_std, r_upper_Arm_mean])
        self.Features_data.append(array)


    def Cycle_Average(self,cycle_f):
        size = len(cycle_f)
        self.Neck = sum(x[0] for x in cycle_f) / size
        self.Arm = sum(x[1] for x in cycle_f) / size
        self.elbow_distance = sum(x[2] for x in cycle_f) / size
        self.knee_distance = sum(x[3] for x in cycle_f) / size
        self.hand_distance = sum(x[4] for x in cycle_f) / size
        self.foot_distance = sum(x[5] for x in cycle_f) / size
        self.thigh = sum(x[6] for x in cycle_f) / size
        self.calf = sum(x[7] for x in cycle_f) / size
        self.hip = sum(x[8] for x in cycle_f) / size
        self.upper_spine = sum(x[9] for x in cycle_f) / size
        self.lower_spine = sum(x[10] for x in cycle_f) / size
        self.spine = sum(x[11] for x in cycle_f) / size
        self.leg = sum(x[12] for x in cycle_f) / size
        self.Body_Height = sum(x[13] for x in cycle_f) / size
        self.Features_data.append(self.getNPArray())


    def Body_Height_C(self,frame):
        fr = frame[18].getXYZ()
        ft = frame[19].getXYZ()
        head = frame[0].getXYZ()
        lower = ((fr[0] + ft[0])/2, (fr[1] + ft[1])/2, (fr[2] + ft[2])/2)
        value = math.sqrt(self.square(head[0] - lower[0]) + self.square(head[1] - lower[1]) + self.square(head[2] - lower[2]))
        return value

    def square(self,x):
        return math.pow(x,2)

    def getFeatures(self):
        return [self.Neck, self.Arm, self.elbow_distance, self.knee_distance, self.hand_distance,
                self.foot_distance, self.thigh, self.calf, self.hip, self.upper_spine, self.lower_spine,
                self.spine, self.leg, self.Body_Height]
    def getVetical(self):
        return [self.V_height, self.V_Should, self.V_Wrist, self.V_Ankle, self.elbow_distance,
                self.hand_distance, self.Body_Height, self.knee_distance, self.V_Elbow, self.V_knee, self.spine, self.thigh,
                self.Angle_R_hip_knee, self.Angle_R_knee_ankle, self.Angle_L_hip_knee, self.Angle_L_knee_ankle,
                self.ankle_distance, self.V_hand, self.calf, self.upper_Arm_L, self.upper_Arm_R]

    def getNPArray(self):
        return np.array([self.Neck, self.Arm, self.elbow_distance, self.knee_distance, self.hand_distance,
                self.foot_distance, self.thigh, self.calf, self.upper_spine, self.lower_spine,
                self.spine, self.leg, self.Body_Height])

