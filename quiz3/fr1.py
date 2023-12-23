class TA(object):
    def __init__(self, name, n):
        self.name = name
        self.courseNumber = n
        self.status = "Alive"
        # self.statusNum = 0
        # self.statusList = ["Alive", "Croacking", "Croaked", "At Pizza Romano"]
    
    def getCourse(self):
        s = str(self.courseNum)
        return s[:2] + '-' + s[2:]
    
    def teachRecitation(self):
        if self.status == "Alive":
            self.status = "Croacking"
        elif self.status == "Crocacking":
            self.status = "Croacked"
        else:
            self.status = "At Pizza Romano"

    # def teachRecitation(self):
    #     self.statusNum += 1
    #     self.statusNum = min(self.statusNum, len(self.statusList)-1)
    #     self.status = self.statusList[self.statusNum]

    def __repr__(self):
        return f'{self.name} is a TA for {self.getCourse()}'
    
    def __eq__(self, other):
        return self.courseNum == other.courseNum

    def defect(self, newCourseNum):
        self.courseNum = newCourseNum