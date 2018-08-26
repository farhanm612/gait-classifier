import Joints
class Frames:

        def __init__(self, s,line):
            self.A = 0;
            self.B = 0;
            self.C = 0;
            self.D = 0;
            self.FloorData(line)
            self.Head = Joints.Coord(self._get_joint(s[0]))
            self.Shoulder_Center = Joints.Coord(self._get_joint(s[1]))
            self.Shoulder_Right = Joints.Coord(self._get_joint(s[2]))
            self.Shoulder_left = Joints.Coord(self._get_joint(s[3]))
            self.Elbow_Right = Joints.Coord(self._get_joint(s[4]))
            self.Elbow_Left = Joints.Coord(self._get_joint(s[5]))
            self.Wrist_Right = Joints.Coord(self._get_joint(s[6]))
            self.Wrist_Left = Joints.Coord(self._get_joint(s[7]))
            self.Hand_Right = Joints.Coord(self._get_joint(s[8]))
            self.Hand_Left = Joints.Coord(self._get_joint(s[9]))
            self.Spine = Joints.Coord(self._get_joint(s[10]))
            self.Hip_centr = Joints.Coord(self._get_joint(s[11]))
            self.Hip_Right = Joints.Coord(self._get_joint(s[12]))
            self.Hip_Left = Joints.Coord(self._get_joint(s[13]))
            self.Knee_Right = Joints.Coord(self._get_joint(s[14]))
            self.Knee_Left = Joints.Coord(self._get_joint(s[15]))
            self.Ankle_Right = Joints.Coord(self._get_joint(s[16]))
            self.Ankle_Left = Joints.Coord(self._get_joint(s[17]))
            self.Foot_Right = Joints.Coord(self._get_joint(s[18]))
            self.Foot_Left = Joints.Coord(self._get_joint(s[19]))

            self.CompleteFrame = [self.Head, self.Shoulder_Center, self.Shoulder_Right, self.Shoulder_left,
                                  self.Elbow_Right, self.Elbow_Left, self.Wrist_Right, self.Wrist_Left,
                                  self.Hand_Right, self.Hand_Left, self.Spine, self.Hip_centr, self.Hip_Right,
                                  self.Hip_Left, self.Knee_Right, self.Knee_Left, self.Ankle_Right, self.Ankle_Left,
                                  self.Foot_Right, self.Foot_Left,self.A,self.B,self.C,self.D]
        def _get_joint(self, Str):
            Str = Str.rstrip()
            y = Str.split(';')
            a = float(y[1].translate(None))
            b = float(y[2].translate(None))
            c = float(y[3].translate(None))
            return (a, b, c)

        def oneframe(self):
            return self.CompleteFrame

        def FloorData(self,Str):
            Str = Str.rstrip()
            y = Str.split(';')
            self.A = float(y[1].translate(None))
            self.B = float(y[2].translate(None))
            self.C = float(y[3].translate(None))
            self.D = float(y[4].translate(None))
