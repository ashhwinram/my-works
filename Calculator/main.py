from kivy import Config
Config.set('graphics','multisamples','0')

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Achu_CalculatorApp(App):
    def build(self):
        self.icon='icon.png'
        def split(a):
            a.reverse()
            summ,j,flag=0,0,0
            temp=[]
            for i in a:
                if(i not in ['/','*','+','-']):
                    summ+=(int(i)*(10**j))
                    j+=1
                    flag=1
                elif(flag):
                    temp.append(summ)
                    summ,j,flag=0,0,0
                    temp.append(i)
            temp.append(summ)
            temp.reverse()
            return temp

        def answer(a,op):
            i=0
            while(i<len(a)-1):
                if(a[i]==op):
                    if(op=='/'):
                        temp=a[i-1]/a[i+1]
                    elif(op=='*'):
                        temp=a[i-1]*a[i+1]
                    elif(op=='+'):
                        temp=a[i-1]+a[i+1]
                    elif(op=='-'):
                        temp=a[i-1]-a[i+1]
                    a[i]=temp
                    a.pop(i-1)
                    a.pop(i)
                else:
                    i+=1
            return a

        def find(a):
            a=answer(a,'/')
            a=answer(a,'*')
            a=answer(a,'+')
            a=answer(a,'-')
            return a[0]

        def calc(a):
            operators=['/','*','+','-']
            numbers=['0','1','2','3','4','5','6','7','8','9']
            if(a==""):
                return ""
            a=[a[x] for x in range(len(a))]
            if(a[0] in operators or a[-1] in operators):
                return "Error"
            else:
                val=split(a)
                if(len(val)==1):
                    return val[0]
                else:
                    return(find(val))
                
        def function(instance):
            val=instance.text
            if(val=='C'):
                screen.text=""
            elif(val=='='):
                result=str(calc(screen.text))
                screen.text=result
                self.nextt=1
            else:
                if(self.nextt):
                    screen.text=""
                    self.nextt=0
                screen.text+=val

        main_layout=BoxLayout(orientation="vertical")
        screen=TextInput(multiline=False,size_hint_y=0.3
                         ,font_size=55,halign="right")
        screen.text=""
        self.nextt=0
        buttons=[['7','8','9','*'],['4','5','6','/'],
                 ['1','2','3','-'],['C','0','=','+']]
        butt=GridLayout(cols=4)
        for i in buttons:
            for j in i:
                if(j=='C'):
                    b=Button(text=j,font_size=40,color=(.7,0,0,1))
                else:
                    b=Button(text=j,font_size=40)
                b.bind(on_press=function)
                butt.add_widget(b)
        main_layout.add_widget(screen)
        main_layout.add_widget(butt)
        return main_layout
        
if __name__ == "__main__":
    Achu_CalculatorApp().run()
