from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
import webbrowser
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog


KV = '''
MDScreenManager:
    HScreen:
    MScreen:
    TScreen:
    NScreen:
    AScreen:
    AdminScreen:
    LoggedAScreen:
    
   
    
    
<AdminScreen>:
    name:'admin'
    BoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title:'Maa Aanjana Patel Samaj'
            md_bg_color: (1, 0.45, 0, 1)
            specific_text_color: (0, 0, 0, 1)
        MDIconButton:
            icon:'arrow-left'
            on_press: root.manager.current ='account'
        MDLabel:
            text:'Welcome to admin portal'
            halign:'center'
            pos_hint:{"center_x": 2.25,"center_y": 4.8}


        MDCard:
            orientation:'vertical'
            padding:'20dp'
            spacing:'20dp'
            size_hint:(None, None)
            size: "300dp", "400dp"
            pos_hint:{"center_x": 0.5}

            MDLabel:
                text:"Admin Login"
                halign:'center'
                font_style:'H6'

            MDTextField:
                id: username
                hint_text:"Username"
                icon_right:'account'
                mode:'rectangle'

                
            MDTextField:
                id: password
                hint_text:"password"
                icon_right:'lock'
                mode:'rectangle'

            MDRaisedButton:
                text:'Manage MAPSA'
                halign:'center'
                pos_hint:{"center_x":0.5}
                on_release:
                    app.validate_login(username.text,password.text)
                    
       

<LoggedAScreen>:
    name:'loggedadmin'
    BoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title:'Maa Aanjana Patel Samaj'
            md_bg_color: (1, 0.45, 0, 1)
            specific_text_color: (0, 0, 0, 1)
        MDIconButton:
            icon:'arrow-left'
            on_press: root.manager.current ='admin'
        MDLabel:
            text:'Welcome to admin portal'
            halign:'center'
            pos_hint:{"center_x": 2.25,"center_y": 4.8}

<MScreen>:
    name: 'more'
    MDTopAppBar:
        title:"Maa Aanjana Patel Samaj"
        elivation:4                 
        pos_hint:{"top":1}   
        md_bg_color: (1, 0.45, 0, 1)
        specific_text_color: (0, 0, 0, 1)

        MDIconButton:
            icon:'arrow-left'
            on_press: root.manager.current ='home'
       
    MDLabel:
        FloatLayout:  # Use FloatLayout for flexible positioning
            MDLabel:
                text: "Donate For Development"
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 6.6}
                size_hint: None, None
                size: "250dp", "60dp" 
                md_bg_color: (0, 1, 0, 1)
                
            Image:
                source: 'assets/13.jpg'
                pos_hint: {'center_x': 2.25, 'center_y':4.2}  
                size_hint: None, None  
                size: "300dp", "300dp"  
            
    
            
            
    
        
            
<HScreen>:
    name: 'home'
    MDTopAppBar:
        title:"Maa Aanjana Patel Samaj"
        elivation:4                 
        pos_hint:{"top":1}   
        md_bg_color: (1, 0.45, 0, 1)
        specific_text_color: (0, 0, 0, 1)
        
       
    MDLabel:
        FloatLayout:  # Use FloatLayout for flexible positioning
            Image:
                source: 'assets/7.jpg'
                pos_hint: {'center_x': 2.25, 'center_y':5.9 }  
                size_hint: None, None  
                size: "300dp", "300dp"  
            MDLabel:
                text: "Registration For Pratibha Samman Samaroh 2025."
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 4.3}
                size_hint: None, None
                size: "300dp", "80dp" 
                md_bg_color: (0, 1, 0, 0.55)
                
           
            
            MDRaisedButton:
                text: "CLick Here"
                md_bg_color:(0,0,1,1)
                pos_hint: {'center_x': 2.25,'center_y': 3.5}
                on_press: app.open_link('https://docs.google.com/forms/d/e/1FAIpQLSe0-3EtFeagV4EFVEZtMiAca-EKhOoiamVrf9QdD-u64IyOUA/viewform?usp=send_form')

            MDLabel:
                text: "Give your suggestion for development of our society ."
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 2.7}
                size_hint: None, None
                size: "300dp", "80dp" 
                md_bg_color: (0, 1, 0, 0.55)
                
           
            
            MDRaisedButton:
                text: "Give my suggestion"
                md_bg_color:(0,0,1,1)
                pos_hint: {'center_x': 2.25,'center_y': 1.9}
                on_press: app.open_link('https://docs.google.com/forms/d/e/1FAIpQLSfK46kXBfK2E3eEPQOJIPBRQcqz06ENnJEynaqqJAJEslpemQ/viewform')

            MDIconButton:
                icon:'arrow-right'
                md_bg_color:(1,0,0,0.7)
                pos_hint: {'center_x': 2.25,'center_y': 1.2}
                on_press: root.manager.current='more'

           
                
            MDLabel:
                text:'                                                                                                                                                   '
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 0.28}

                size_hint: None, None
                size: "400dp", "80dp" 
                md_bg_color: (1, 0.45, 0, 1)

            

    MDIconButton:
        icon: 'home'
        pos_hint: {'center_x': 0.1, 'center_y': 0.06}
        on_press: root.manager.current = 'home'
        
    MDIconButton:
        icon: 'baseball'
        pos_hint: {'center_x': 0.36, 'center_y': 0.06}
        on_press: root.manager.current = 'tournament'
    MDIconButton:
        icon: 'bell'
        pos_hint: {'center_x': 0.61, 'center_y': 0.06}
        on_press: root.manager.current = 'notifications'
    MDIconButton:
        icon: 'account-circle'
        pos_hint: {'center_x': 0.88, 'center_y': 0.06}
        on_press: root.manager.current = 'account'

   

        
   

<TScreen>:
    name: 'tournament'

    MDLabel:
        FloatLayout:  # Use FloatLayout for flexible positioning
            Image:
                source: 'assets/9.jpg'
                pos_hint: {'center_x': 2.25, 'center_y':5.8 }  
                size_hint: None, None  
                size: "200dp", "200dp" 

            MDLabel:
                text: " Tournament are organized at Major Dhyanchand Ground Nawalshyam Mod, Kanba."
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y':4 }
                size_hint: None, None
                size: "300dp", "80dp" 
                md_bg_color: (1, 0, 1, 0.55) 

            MDLabel:
                text:'                                                                                                                                                   '
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 0.28}

                size_hint: None, None
                size: "400dp", "80dp" 
                md_bg_color: (1, 0.45, 0, 1)

    MDTopAppBar:
        title:"Maa Aanjana Patel Samaj"
        elivation:4                 
        pos_hint:{"top":1}   
        md_bg_color: (1, 0.45, 0, 1)
        specific_text_color: (0, 0, 0, 1)
    MDIconButton:
        icon: 'home'
        pos_hint: {'center_x': 0.1, 'center_y': 0.06}
        on_press: root.manager.current = 'home'
        
    MDIconButton:
        icon: 'baseball'
        pos_hint: {'center_x': 0.36, 'center_y': 0.06}
        on_press: root.manager.current = 'tournament'
    MDIconButton:
        icon: 'bell'
        pos_hint: {'center_x': 0.61, 'center_y': 0.06}
        on_press: root.manager.current = 'notifications'
    MDIconButton:
        icon: 'account-circle'
        pos_hint: {'center_x': 0.88, 'center_y': 0.06}
        on_press: root.manager.current = 'account'

   



<NScreen>:
    name: 'notifications'
    MDLabel:
        FloatLayout:  # Use FloatLayout for flexible positioning
            Image:
                source: 'assets/11.jpg'
                pos_hint: {'center_x': 2.25, 'center_y':6.3}  
                size_hint: None, None  
                size: "200dp", "200dp"

            MDLabel:
                text: "1.Temple of our  Kuldevi Maa Aanjana in our Samaj is located in Dhuvaliya village,Dungarpur since 2022."
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 5}
                size_hint: None, None
                size: "300dp", "80dp" 
                md_bg_color: (1, 1, 0, 0.55)

            MDLabel:
                text: "2. Pratibha Samman Samaroh will be held on 12-January-2025, Sunday at Deval.You are cordially invited."
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 3.7}
                size_hint: None, None
                size: "300dp", "80dp" 
                md_bg_color: (1, 1, 0, 0.55)

            MDLabel:
                text:'                                                                                                                                                   '
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 0.28}

                size_hint: None, None
                size: "400dp", "80dp" 
                md_bg_color: (1, 0.45, 0, 1)

    MDTopAppBar:
        title:"Maa Aanjana Patel Samaj"
        elivation:4                 
        pos_hint:{"top":1}   
        md_bg_color: (1, 0.45, 0, 1)
        specific_text_color: (0, 0, 0, 1)
    MDIconButton:
        icon: 'home'
        pos_hint: {'center_x': 0.1, 'center_y': 0.06}
        on_press: root.manager.current = 'home'
        
    MDIconButton:
        icon: 'baseball'
        pos_hint: {'center_x': 0.36, 'center_y': 0.06}
        on_press: root.manager.current = 'tournament'
    MDIconButton:
        icon: 'bell'
        pos_hint: {'center_x': 0.61, 'center_y': 0.06}
        on_press: root.manager.current = 'notifications'
    MDIconButton:
        icon: 'account-circle'
        pos_hint: {'center_x': 0.88, 'center_y': 0.06}
        on_press: root.manager.current = 'account'

   



<AScreen>:
    name: 'account'
    MDLabel:
        FloatLayout:  # Use FloatLayout for flexible positioning
            Image:
                source: 'assets/10.jpg'
                pos_hint: {'center_x': 2.25, 'center_y':6.3}  
                size_hint: None, None  
                size: "200dp", "200dp"

            Image:
                source: 'assets/14.jpg'
                pos_hint: {'center_x': 2.25, 'center_y':4}  
                size_hint: None, None  
                size: "300dp", "200dp"
            
            MDRaisedButton:
                text:'Admin Portal'
                md_bg_color:(1,0,0,1)
                pos_hint:{"center_x":2.25,"center_y":2.3}
                on_release: root.manager.current ='admin'        
                
            MDLabel:
                text:'                                                                                                                                                   '
                halign: 'center'
                pos_hint: {'center_x': 2.25, 'center_y': 0.28}

                size_hint: None, None
                size: "400dp", "80dp" 
                md_bg_color: (1, 0.45, 0, 1)
    MDTopAppBar:
        title:"Maa Aanjana Patel Samaj"
        elivation:4                 
        pos_hint:{"top":1}   
        md_bg_color: (1, 0.45, 0, 1)
        specific_text_color: (0, 0, 0, 1)
    MDIconButton:
        icon: 'home'
        pos_hint: {'center_x': 0.1, 'center_y': 0.06}
        on_press: root.manager.current = 'home'
        
    MDIconButton:
        icon: 'baseball'
        pos_hint: {'center_x': 0.36, 'center_y': 0.06}
        on_press: root.manager.current = 'tournament'
    MDIconButton:
        icon: 'bell'
        pos_hint: {'center_x': 0.61, 'center_y': 0.06}
        on_press: root.manager.current = 'notifications'
    MDIconButton:
        icon: 'account-circle'
        pos_hint: {'center_x': 0.88, 'center_y': 0.06}
        on_press: root.manager.current = 'account'

   

    
'''

Window.size = (352, 632)

class Shiv(MDApp):
    def build(self):
        self.dialog = None
        bldr = Builder.load_string(KV)
        return bldr
    def open_link(self, url):
        # Opens the provided URL in the default browser
        webbrowser.open(url)

    def validate_login(self,username,password):
        admin_username = "1"
        admin_password= "1"

        if username== admin_username and password== admin_password:
            self.show_dialog("Login Successful!", "Welcome to the MAPSA'S Admin Dashboard", success= True)
           
        else:
            self.show_dialog("Login Failed", "Invalid Username or Password. Please Try Again.", success= False)
            

    def show_dialog(self, title, text, success):
        if not self.dialog:
            self.dialog = MDDialog(
                title= 'mapsa', 
                text='login',
                buttons=[
                    MDRaisedButton(text="ok", on_release=lambda x: self.close_dialog(success))

                ],
            )
        
        self.dialog.title = title   
        self.dialog.text = text
        self.dialog.success = success
        self.dialog.open()

    def close_dialog(self, success):
        self.dialog.dismiss()
        self.dialog = None
        if success :
            self.root.current = 'loggedadmin'
        else:
            self.root.current = 'admin'

class AdminScreen(Screen):
    pass

class LoggedAScreen(Screen):
    pass

class HScreen(Screen):
    pass

class MScreen(Screen):
    pass

class TScreen(Screen):
    pass

class NScreen(Screen):
    pass

class AScreen(Screen):
    pass

Shiv().run()
