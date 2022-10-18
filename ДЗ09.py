
class Themes:
    def __init__(self,topics):
        self.topics=topics

    def add_theme(self,value):
        return self.topics.append(value)

    def shift_one(self):
        return self.topics.insert(0, self.topics.pop())

    def reverse_order(self):
        return self.topics[::-1]

    def get_themes(self):
        return self.topics
    def get_first(self):
        return self.topics[0]




class Triangle:
    def __init__(self,a=5,b=6):
        self.a=a #Катеты
        self.b=b # Гипотенуза

    def change(self,side,procent): #side-задаем сторону, procent - задаем проценты если >0 увел, <0 умен
        if side == 'a':
            if procent >0:
                return self.a + self.a * procent/100
            else:
                return self.a - self.a * procent/100
        if side == 'b':
            if procent >0:
                return self.a + self.a * procent/100
            else:
                return self.a - self.a * procent/100

    def radius(self):
        return self.b / 2

    def perim(self):
        return self.a * 2 + self.b

    def corners(self): # немного не понял, у нас дано ток два числа, получается одно это катеты, второе гипотенуза
        return 'Corners = 90, 45, 45' # отсюда следует что, если катеты равны, то и углы при них равны




class BeeElephant:
    def __init__(self,bee,elephant):
        self.bee=bee
        self.elephant=elephant

    def fly(self):
        if self.bee == self.elephant or self.bee > self.elephant:
            return True
        return False
    def trumpet(self):
        if self.elephant == self.bee or self.elephant > self.bee:
            return "tu-tu-doo-doo!"
        return "wzzzzz"
    def eat(self,meal,value):
        if value <=0 or value >=100:
            return "Error"
        if meal == 'nectar':
            if value > self.elephant:
                self.bee += self.elephant
                self.elephant = 0
            else:
                self.bee += value
                self.elephant -= value
        if meal == 'grass':
            if value > self.bee:
                self.elephant += self.bee
                self.bee = 0
            else:
                self.elephant += value
                self.bee -= value

    def get_parts(self):
        return self.bee,self.elephant



class Cat:
    I=0
    count1=0
    count2=0
    def __init__(self,name,):
        self.name=name


    def to_answer(self):
       if Cat.I == 0 or Cat.I % 2 == 0:
           Cat.I+=1
           Cat.count1+=1
           return 'moore-moore'
       if Cat.I % 2 !=0:
           Cat.count2+=1
           Cat.I+=1
           return 'meow-meow'

    def number_yes(self):
        return Cat.count1
    def number_no(self):
        return Cat.count2


from random import randint
class TArray:
    def __init__(self,count,arr):
        self.count=count
        self.arr=arr
    def in_output(self):
        self.arr=[randint(1,10)for i in range(self.count)]
        return self.arr

    def max_min(self):
        return f'Max = {max(self.arr)}, min = {min(self.arr)}'
    def sort_arr(self):
        self.arr.sort()
        return self.arr
    def sum_arr(self):
        summa=0
        for i in self.arr:
            summa+=i
        return summa
    def add_arr(self,elem):
        self.arr.append(elem)
        return self.arr

    def multip(self,number):
        for i in range(len(self.arr)):
            self.arr[i]=self.arr[i]*number
        return self.arr



