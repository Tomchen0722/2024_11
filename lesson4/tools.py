PI=3.1415926  #常數要用大寫


class Person:
    '''
    我是Person
    '''
    def __init__(self,name:str,age:int):#self可以省略
        self.name = name #name,age (attribute)
        self.age = age #name,age (attribute)
    
    #實體方法(instance method)
    def echo(self):
        print(f'我的姓名是:{self.name}')
        print(f'我的年齡是:{self.age}')
class Student(Person):#（子類別) Student繼承->Person繼承->object 
    '''
    我是Student
    '''
    
    def __init__(self,name:str,age:int,score:int):
            super().__init__(name=name,age=age) #super引用父類別
            self.__score = score #保護score 用__

    @property #只能讀不能做修改
    def score(self)->int:
         return self.__score
    
    def echo(self):
        super().echo()#super引用父類別
        #print(f'我的姓名是:{self.name}')
        #print(f'我的年齡是:{self.age}')
        print(f'我的score是:{self.score}')   
def get_status(bmi:float)->str:
    '''
    docstring
    Parameter:
        bmi:bmi值可以整數或浮點數
    Return:str
        會傳出5個狀態
        - 正常範圍
    
    '''
    if bmi >= 35 :
        bmi_str = '重度肥胖'
    elif bmi >= 30 :
        bmi_str = '中度肥胖'
    elif bmi >= 27 :
        bmi_str = '輕度肥胖'
    elif bmi >= 24 :
        bmi_str = '過重'
    elif bmi >= 18.5 :
        bmi_str = '正常範圍'
    else :
        bmi_str = '過輕' 
    return bmi_str
    
def BMI_math(height_cm:float, weight_kg:float)->tuple[float,str]:
    height_m = round(height_cm/100, 2)
    bmi_kg_m2 = round(weight_kg/(height_m**2), 2)
    bmi_str = get_status(bmi_kg_m2)
    return bmi_kg_m2, bmi_str