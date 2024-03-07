class Python_Switch:
    def day(self, month):
        default = "Incoreect day"
        return getattr(self,'case_'+ str(month),lambda: default())

    def case_1(self):
        return "Jan"

    def case_2(self):
        return "Feb"
    def case_3(self):
        return "Mar"

#Switch_instance == Python_instance()

    

                       