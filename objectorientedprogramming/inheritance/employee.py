

class Employee:

    def __init__(self,name,id,department):

        self.name = name

        self.id = id

        self.department = department

    def disaply(self):

        print(self.id , self.name , self.department)

class Developer(Employee):

    def __init__(self, name, id, department,language,frame_work):

        super().__init__(name, id, department)

        self.langugae = language

        self.frame_work = frame_work

    def display_developer(self):

        print(self.langugae,self.frame_work)


developer_instance = Developer("vipin",101,"developer","python","django")

developer_instance.disaply()

developer_instance.display_developer()

        