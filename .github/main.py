from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.utils import platform

# Принудительно включаем горизонтальный режим для Android
if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    
    ActivityInfo = autoclass('android.content.pm.ActivityInfo')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    currentActivity = PythonActivity.mActivity
    currentActivity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE)

class ZetarsApp(App):
    def build(self):
        # Делаем фон экрана черным
        Window.clearcolor = (0, 0, 0, 1)
        
        # Создаем вертикальный контейнер
        layout = BoxLayout(orientation='vertical')
        
        # 1. Создаем красивую надпись сверху
        label = Label(
            text="Зетарс",
            font_size='48sp',
            bold=True,
            color=(0.95, 0.77, 0.06, 1),
            # Ограничиваем высоту надписи, чтобы она не растягивалась на весь экран
            size_hint_y=None,
            height='150dp'  # Высота блока с текстом
        )
        
        # 2. Создаем пустой невидимый элемент-"распорку"
        # Он займет все оставшееся снизу место и вытолкнет надпись наверх
        spacer = Widget()
        
        # Добавляем элементы в контейнер (сверху вниз)
        layout.add_widget(label)
        layout.add_widget(spacer)
        
        return layout

if __name__ == '__main__':
    ZetarsApp().run()
