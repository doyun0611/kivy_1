# kivy 라이브러리에서 App 클래스를 import
from kivy.app import App
# kivy 라이브러리에서 BoxLayout 클래스를 import
from kivy.uix.boxlayout import BoxLayout
# kivy 라이브러리에서 Label 클래스를 import
from kivy.uix.label import Label
# kivy 라이브러리에서 TextInput 클래스를 import
from kivy.uix.textinput import TextInput
# kivy 라이브러리에서 ScrollView 클래스를 import
from kivy.uix.scrollview import ScrollView
# kivy 라이브러리에서 GridLayout 클래스를 import
from kivy.uix.gridlayout import GridLayout
# kivy 라이브러리에서 Button 클래스를 import
from kivy.uix.button import Button
import openai


# ChatApp 클래스를 선언하고 App 클래스를 상속받음
openai.organization = "org-nQ24a9MWYBCNdK1Qu8cRl2jr"
openai.api_key = "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"

fontname = 'NanumGothic.ttf'

text_input = TextInput(size_hint_y=0.2,font_name= fontname)

class ChatApp(App):
    # build 함수를 override
   
    def build(self):
        # BoxLayout을 생성하고 orientation 속성을 'vertical'로 설정
        layout = BoxLayout(orientation='vertical')
        # ScrollView를 생성하고 size_hint_y 속성을 0.9로 설정
        scroll_view = ScrollView(size_hint_y=0.9)
        # GridLayout을 생성하고 cols 속성을 1로 설정
        grid_layout = GridLayout(cols=1, size_hint_y=None)
        # grid_layout의 높이를 최소화
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # scroll_view에 grid_layout을 추가
        scroll_view.add_widget(grid_layout)
        # layout에 scroll_view를 추가
        layout.add_widget(scroll_view)
        # TextInput을 생성하고 size_hint_y 속성을 0.1로 설정
        # layout에 text_input을 추가

        # Button을 생성하고 text 속성을 'Send'로 설정
        button = Button(text='Send', size_hint=(None, None), size=(60, 60))
        # text_input과 button을 담을 BoxLayout을 생성하고 orientation 속성을 'horizontal'로 설정
        input_layout = BoxLayout(orientation='horizontal')
        # input_layout에 text_input과 button을 추가
        input_layout.add_widget(text_input)
        input_layout.add_widget(button)
        # layout에 input_layout을 추가
        layout.add_widget(input_layout)
        # button에 on_press 이벤트를 추가하여 text_input의 내용을 label로 추가하는 함수를 실행
        button.bind(on_press=lambda x: self.add_label(
            grid_layout, text_input.text))
        # return layout
        return layout

    # add_label 함수를 정의하여 grid_layout에 label을 추가하는 함수
    def add_label(self, grid_layout, text):
        answer = text_input.text
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="%s\nA:"%answer,
                    temperature=0,
                    max_tokens=4000,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    stop=["\n"])
        # label을 생성하고 text_input의 내용으로 설정
        label = Label(text="Me: %s"%text,font_name= fontname, size_hint_y=None, height=40)
        label_1 = Label(text="AI: %s"%response.choices[0].text.strip(),font_name= fontname, size_hint_y=None, height=40)
        # grid_layout에 label을 추가
        grid_layout.add_widget(label)
        grid_layout.add_widget(label_1)
        # text_input의 내용을 지움
        text_input.text = ''
        


# ChatApp을 실행
if __name__ == '__main__':
    ChatApp().run()