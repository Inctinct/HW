class SuperStr(str):

    def __init__(self,strin):
        self.strin=strin
    def is_repeatance(self,s):
        if type(s) !=str:
            return False
        if self.strin=='':
            return False
        return s * (len(self.strin)//len(s)) == self.strin
    def is_palindrom(self):
        if self.strin == '':
            return True
        return self.strin.lower()==self.strin[::-1].lower()

strin=input('Set a string')
s=input('Set a s: ')
stroka=SuperStr(strin)
print(stroka.is_repeatance(s))
print(stroka.is_palindrom())