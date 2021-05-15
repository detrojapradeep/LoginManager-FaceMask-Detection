screen_helper = """
ScreenManager:
    id: scr_mngr
    LoginScreen:
    MainScreen:
    ScanScreen:
    AttendanceScreen:
    AboutScreen:
    ProfileScreen:

<LoginScreen>
    id: screen1
    name: 'login'
    username: username
    password: password
    spinner: spinner
    MDToolbar:
        md_bg_color: 0, 0, 1, 1
        title: "Login Screen"
        pos_hint:{"top": 1}
        elevation: 11
    Image:
        id: imageView
        pos_hint: {'center_x':0.5,'center_y':0.75}
        size_hint_x: None
        width: 200
        source: 'LogX.png'
        
    MDTextField:
        id:username
        hint_text: "Enter Username"
        helper_text: "Or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "login"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.55}
        size_hint_x: None
        width: 300
        
    MDTextField:
        id: password
        hint_text: "Password"
        helper_text: "Or click on forgot Password"
        helper_text_mode: "on_focus"
        password: True
        icon_right: "onepassword"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.45}
        size_hint_x: None
        width: 300
    
    MDSpinner:
        id:spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: False
        
    MDRectangleFlatButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        user_font_size: "64sp"
        on_press: app.validation()

<AttendanceScreen>
    name : 'attendance'
    #table: table
    MDToolbar:
        md_bg_color: 0, 0, 1, 1
        id: toolbar
        title: "Attendance Logs"

<AboutScreen>
    name : 'about'
    MDLabel:
        text: 'Our Goal is to make the World a of employers a tension free and contactless by QR Code attendance login. With this no one will be able to have a cheat day and will also live a prosporous life without the infection of Covid19 attack. As this machine checks the mask of the person and then only he/she can move forward with the attendance.'
        pos_hint: {"center_x": 0.5, "center_y": 0.60}
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDIconButton:
        icon: "keyboard-backspace"
        pos_hint: {"center_x": .1, "center_y": .95}
        on_release: app.back()
    
<ProfileScreen>
    name : 'profile'
    MDToolbar:
        md_bg_color: 0, 0, 0.95, 1
        id: toolbar
        title: "Profile"
    MDLabel: 
        text: 'PROFILE'
        pos_hint: {"center_x": 0.5, "center_y": 0.90}
        halign: 'center'
        # size_hint: 1,1
        #font_style='H3'
        theme_text_color: "Custom"
        text_color: 1, 1, 0.65, 1
    MDLabel: 
        text: 'Name: '
        pos_hint: {"center_x": 0.1, "center_y": 0.80}
        halign: 'center'
        # size_hint: 1,1
        #font_style='Button'
        theme_text_color: "Custom"
        text_color: 247/255, 169/255, 115/255, 1
    MDLabel: 
        text: 'Employee ID: '
        pos_hint: {"center_x": 0.1, "center_y": 0.70}
        #halign: 'center'
        # size_hint: 1,1
        #font_style='Button'
        theme_text_color: "Custom"
        text_color: 247/255, 169/255, 115/255, 1
    
    # MDLabel: 
    #     text: app.namee
    #     pos_hint: {"center_x": 0.3, "center_y": 0.80}
    #     #halign: 'center'
    #     # size_hint: 1,1
    #     #font_style='Button'
    #     theme_text_color: "Custom"
    #     text_color: 247/255, 156/255, 145/255, 1
    
    MDIconButton:
        icon: "keyboard-backspace"
        pos_hint: {"center_x": .1, "center_y": .95}
        on_release: app.back()
            
<MainScreen>
    id: screen2
    name : 'main'
    MDToolbar:
        md_bg_color: 0, 0, 1, 1
        id: toolbar
        title: "LogX Manager"
    MDIconButton:
        icon: "qr.png"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        user_font_size:'70sp'
        on_release: app.scanner()
    MDLabel: 
        text: 'Scan QR Code'
        pos_hint: {"center_x": 0.5, "center_y": 0.60}
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDIconButton:
        icon: "attendance.png"
        pos_hint: {"center_x": .5, "center_y": .45}
        user_font_size:'70sp'
        #on_release: root.manager.current = 'attendance'
        on_release: app.table()
    MDLabel: 
        text: 'Attendance Log'
        pos_hint: {"center_x": 0.5, "center_y": 0.30}
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDFloatingActionButtonSpeedDial:
        data: app.data
        callback: app.callback
        root_button_anim: True
        hint_animation: True
        rotation_root_button: True
        

<ScanScreen>
    name : 'scan'
    qrlabel: qrlabel
    zbarcamm: zbarcamm
    MDToolbar:
        md_bg_color: 0, 0, 1, 1
        id: toolbar
        title: "LogX Scanner"
    MDLabel: 
        text: 'Scan QR Code'
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1        
    ZBarCam:
        id: zbarcamm
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: [1, 3]
    MDLabel:
        id: qrlabel
        #size_hint: None, None
        size: self.texture_size[0], 10
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        halign: "center"
        text: ', '.join([str(symbol.data) for symbol in zbarcamm.symbols])
        opacity: 0
        on_text: app.calc(self.text)
        
    MDFlatButton:
        text: "Back"
        pos_hint: {"center_x": .1, "center_y": .95}
        on_release: app.back()

"""