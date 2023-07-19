from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition

Builder.unload_file("testapp.kv")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class CreateHabitScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(CreateHabitScreen(name='create_habit'))
        return sm

if __name__ == '__main__':
    TestApp().run()