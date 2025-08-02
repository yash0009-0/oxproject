from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen , ScreenManager


turn = [0]
state_w = [-1,0]
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
reset_sound = SoundLoader.load('sound/reset.ogg')
ox_sound = SoundLoader.load('sound/ox.ogg')
class RoundButton(Button):
    rgba = ListProperty([0.827, 0.843, 0.812, 1])
    color = ListProperty([0.937, 0.161, 0.161, 1])
    def animate_color(self, new_color):
        anim = Animation(rgba=new_color, duration=0.07)
        anim.start(self)

class First(Screen):
    state = [4,4,4,4,4,4,4,4,4]
    def sound_ox(self):
        if ox_sound:
            ox_sound.play()
    def sound_reset(self):
        if self.state != [4,4,4,4,4,4,4,4,4]:
            if reset_sound:
                reset_sound.play()
            self.reset_game()
    def reset_game(self):
        self.ids.b_1.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_2.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_3.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_4.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_5.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_6.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_7.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_8.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_9.animate_color([0.827, 0.843, 0.812, 1])
        self.ids.b_1.text = ""
        self.ids.b_2.text = ""
        self.ids.b_3.text = ""
        self.ids.b_4.text = ""
        self.ids.b_5.text = ""
        self.ids.b_6.text = ""
        self.ids.b_7.text = ""
        self.ids.b_8.text = ""
        self.ids.b_9.text = ""
        self.state = [4,4,4,4,4,4,4,4,4]
    def check_win(self):
        for win in wins:
            if self.state[win[0]] + self.state[win[1]] + self.state[win[2]] == 3:
                self.ids.b_1.rgba = [0,0,0,0]
                self.ids.b_2.rgba = [0,0,0,0]
                self.ids.b_3.rgba = [0,0,0,0]
                self.ids.b_4.rgba = [0,0,0,0]
                self.ids.b_5.rgba = [0,0,0,0]
                self.ids.b_6.rgba = [0,0,0,0]
                self.ids.b_7.rgba = [0,0,0,0]
                self.ids.b_8.rgba = [0,0,0,0]
                self.ids.b_9.rgba = [0,0,0,0]
                self.manager.current = "second"
                state_w[0] = 1
                state_w[1] = 1
                self.reset_game()
            if self.state[win[0]] + self.state[win[1]] + self.state[win[2]] == 0:
                self.ids.b_1.rgba = [0,0,0,0]
                self.ids.b_2.rgba = [0,0,0,0]
                self.ids.b_3.rgba = [0,0,0,0]
                self.ids.b_4.rgba = [0,0,0,0]
                self.ids.b_5.rgba = [0,0,0,0]
                self.ids.b_6.rgba = [0,0,0,0]
                self.ids.b_7.rgba = [0,0,0,0]
                self.ids.b_8.rgba = [0,0,0,0]
                self.ids.b_9.rgba = [0,0,0,0]
                self.manager.current = "second"
                state_w[0] = 0
                state_w[1] = 1
                self.reset_game()
    def on_press(self,a):
        if self.state[a] == 4:
            if turn[0] == 0:
                if ox_sound:
                    ox_sound.play()
                self.state[a] = 0
                self.but_col()
                self.but_text()
                turn[0] = 1
                self.check_turn()
                self.check_win()
                print(self.state)
            else:
                if ox_sound:
                    ox_sound.play()
                self.state[a] = 1
                self.but_col()
                self.but_text()
                turn[0] = 0
                self.check_turn()
                self.check_win()
                print(self.state)

    def but_text(self):
        if self.state[0] != 4:
            if self.state[0] == 0:
                self.ids.b_1.text = "O"
            elif self.state[0] == 1:
                self.ids.b_1.text = "X"
        if self.state[1] != 4:
            if self.state[1] == 0:
                self.ids.b_2.text = "O"
            elif self.state[1] == 1:
                self.ids.b_2.text = "X"
        if self.state[2] != 4:
            if self.state[2] == 0:
                self.ids.b_3.text = "O"
            elif self.state[2] == 1:
                self.ids.b_3.text = "X"
        if self.state[3] != 4:
            if self.state[3] == 0:
                self.ids.b_4.text = "O"
            elif self.state[3] == 1:
                self.ids.b_4.text = "X"
        if self.state[4] != 4:
            if self.state[4] == 0:
                self.ids.b_5.text = "O"
            elif self.state[4] == 1:
                self.ids.b_5.text = "X"
        if self.state[5] != 4:
            if self.state[5] == 0:
                self.ids.b_6.text = "O"
            elif self.state[5] == 1:
                self.ids.b_6.text = "X"
        if self.state[6] != 4:
            if self.state[6] == 0:
                self.ids.b_7.text = "O"
            elif self.state[6] == 1:
                self.ids.b_7.text = "X"
        if self.state[7] != 4:
            if self.state[7] == 0:
                self.ids.b_8.text = "O"
            elif self.state[7] == 1:
                self.ids.b_8.text = "X"
        if self.state[8] != 4:
            if self.state[8] == 0:
                self.ids.b_9.text = "O"
            elif self.state[8] == 1:
                self.ids.b_9.text = "X"
        
        
        
    def but_col(self):
        if self.state[0] != 4:
            self.ids.b_1.animate_color([0, 0, 0, 1])
        if self.state[1] != 4:
            self.ids.b_2.animate_color([0, 0, 0, 1])
        if self.state[2] != 4:
            self.ids.b_3.animate_color([0, 0, 0, 1])
        if self.state[3] != 4:
            self.ids.b_4.animate_color([0, 0, 0, 1])
        if self.state[4] != 4:
            self.ids.b_5.animate_color([0, 0, 0, 1])
        if self.state[5] != 4:
            self.ids.b_6.animate_color([0, 0, 0, 1])
        if self.state[6] != 4:
            self.ids.b_7.animate_color([0, 0, 0, 1])
        if self.state[7] != 4:
            self.ids.b_8.animate_color([0, 0, 0, 1])
        if self.state[8] != 4:
            self.ids.b_9.animate_color([0, 0, 0, 1])

    def check_turn(self):
        if turn[0] == 0:
            self.ids.turn_text.text = "[color=EF2929]O[/color] [color=D3D7CF]turn[/color]"
        else:
            self.ids.turn_text.text = "[color=EF2929]X[/color] [color=D3D7CF]turn[/color]"

class Second(Screen):
    def on_enter(self):
        if "b__" in self.ids:
            if state_w[0] == 1:
                self.ids.b__.text = "[color=EF2929]X[/color] [color=D3D7CF]win ![/color]"
                print("X wins")
            elif state_w[0] == 0:
                self.ids.b__.text = "[color=EF2929]O[/color] [color=D3D7CF]win ![/color]"
                print("O wins")
            else:
                self.ids.b__.text = "[color=EF2929]Draw[/color]"
                print("Draw")
        else:
            print("b__ not found in ids!")
            

        
        
class Window(ScreenManager):
    pass
class ox(App):
    def build(self):
        return Window()

ox().run()
