import kivy
kivy.require('1.10.1')
from reconhecedor_LBPH import rec
from sqlConnector import login
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

class Widgets(FloatLayout):

    info = StringProperty()

    def login(self,usuario, senha):
        id = login(usuario,senha)
        if id != None:
            id = ','.join([str(i) for i in id])
            info = ("id "+id+" logado com sucesso" )
            print("id "+id+" logado com sucesso ")
            rec()
        else:
            info = "login ou senha incorretos"
            print("login ou senha incorretos")
            
           
    #pass
    #def __init__(self, **kwargs):
        #super(LoginScreen, self).__init__(**kwargs)
       # self.cols = 2
       # self.add_widget(Label(text="User name"))
       # self.username = TextInput(multiline=False)
       # self.add_widget(self.username)
       # self.add_widget(Label(text='password'))
       # self.password = TextInput(password=True, multiline=False)
       # self.add_widget(self.password)

class TelaPrincipal(App):
    def build(self):
        return Widgets()


if __name__ == '__main__':
    TelaPrincipal().run()