class TestCovid:

    suspected=0
    trials=0
    results=[]
    errorCounter=3
    questions=['Fever or chills','Cough','Fatigue','Shortness of breath or difficulty breathing']

    def __init__(self,trials):
        self.trials=trials
        self.loopTrials()
    

    def accountSuspect(self,testResult):
        if testResult==1:
            self.suspected=self.suspected+1

    
    def checkPatientsResponse(self,message):
        while self.errorCounter>0:
            try:
                self.CheckSuspects(message)
                break
            except Exception as e:
                print(str(e)+' - You have {} more attempts'.format(self.errorCounter))
                self.errorCounter=self.errorCounter-1
        
    
    def CheckSuspects(self, message):
        test=input(message)
        test=test.strip()
        assert test in ['0','1'], "Test response can only be 0 or 1"
        test=int(test)
        self.accountSuspect(test)

    
    def consolidateReport(self,trial):
        if self.suspected==len(self.questions):
            resultPacient="Suspected with Covid 19"
        else:
            resultPacient="NOT Suspected"
        
        self.results.append(dict(name="Pacient "+str(trial),result=str(resultPacient)))


    def printReport(self):
        print(self.results)

    
    def loopTrials(self):
        for trial in range(self.trials):
            self.suspected=0
            print('----------------------- '+'Testing User '+str(trial)+' -----------------------')
            for question in self.questions:
                textMessage='Do you have '+str(question)+ '? \n Type 1 for YES or 0 for NO \n Your Response:'
                self.checkPatientsResponse(textMessage)
            self.consolidateReport(trial)
        self.printReport()
