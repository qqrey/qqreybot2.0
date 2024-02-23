import datetime
class idle_member:
    def __init__ (self, pname, pdate, pdiamond, pnetherite_ingot):
        self.name = pname
        self.date = pdate
        self.diamond = pdiamond
        self.netherite_ingot = pnetherite_ingot
        print('Creating_idle_member_object')

    def idle_days(self):
        temp = []
        member_idle_day = datetime.datetime.now()
        temp.append(self.date)
        temp.append(member_idle_day)
        self.date = temp
        return self.date

    def calculate(self):   #计算部分才会给新资料
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: ' %(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print("Getter Method")
        return self.name

    #@position.setter
    #def position(self, value):
    #    if value == 'Manager' or value == 'Basic':
    #        self._position = value
    #    else:
    #        print('Position is invalid. No changes made.')


runtime_date = datetime.datetime.now()
officeStaff1 = idle_member('Yvonne', runtime_date, 0, 0)  #这里都应该继承旧资料
#print(str(officeStaff1))
#print(officeStaff1.idle_days())