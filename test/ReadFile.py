
class QuestionsHelper:
    def __init__(self,fileName):
        self.fileName = fileName

    def getQuestions(self):
        # Return questions as list of strings
        f = open(self.fileName,"r")
        for x in f:
            print(x)