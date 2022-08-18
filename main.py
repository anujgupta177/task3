class Employee:
    
    def __init__(self):
        self.empList = ['John','Ron','Rosh','Jimmy']
        self.empDict = {}
    

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.mgrList = ['Bill','Tom','Greg','Josh']
        self.mgrDict = {}
    
    
    #assign project to employee    
    def assignProject(self, empName, projectName):
        if empName not in self.empDict:
            if empName in self.empList:
                self.empDict[empName] = projectName
                print("Project, "+projectName+" is assigned to Employee "+empName)
                print(self.empDict)
            else:
                print(empName + " is not an Employee")
        elif self.empDict[empName]:
            print(empName," has project ", self.empDict[empName]) 
        
        
class Admin(Manager):
    
    #add employee under manager
    def assignEmp(self, mgrName, empName):
        if mgrName not in self.mgrDict:
            if mgrName in self.mgrList:
                self.mgrDict[mgrName] = empName
                print("Employee, "+empName+" is assigned to manager "+mgrName)
                print(self.mgrDict)
            else:
                print(mgrName + " is not manager") 
        elif self.mgrDict[mgrName]:
            print(mgrName," has employee ", self.mgrDict[mgrName])
            
    
    def addMgr(self,mgrName):
        self.mgrList.append(mgrName)
        print(self.mgrList)
        
    def addEmp(self,empName):
        self.empList.append(empName)
        print("Employee list: ", self.empList)
    

assignEmpVar = Admin()
assignEmpVar.assignEmp("Tom","John")
assignEmpVar.assignEmp("Bill","Jimmy")

assignPrjVar = Manager()
assignPrjVar.assignProject("Ron","Prj1")

assignEmpVar.addEmp("Rajesh")
