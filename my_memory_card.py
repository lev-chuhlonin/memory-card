from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication,QWidget
,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,
QPushButton,QLabel,QButtonGroup,)
from random import shuffle,randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3


question_list = []
question_list.append(Question('Государственный язык бразилии?', 'Португальский', 'Англиский' , 'Испанский' , 'Бразилльский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'жёлтый', 'синий' , 'белый' , 'красный'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта' , 'Иглу' , 'Хата'))
question_list.append(Question('кто лучший шкебеде туалет?' , 'G-man', 'туалет учёный' , 'туалет вертолёт', 'туалет паук'))
question_list.append(Question('сколько месяцев в году?' , '12', '100' , '0', '1'))
question_list.append(Question('в каком году была основана Москва?' , '1147', '1242' , '2028', '127'))
question_list.append(Question('сколько часов в дне?' , '24', '1' , '40', '12'))
question_list.append(Question('сколько дней в неделе?' , '7', '5' , '2', '10'))
question_list.append(Question('сколько букв в германском алфавите?' , '26', '10' , '50', '23'))
question_list.append(Question('в каком году распался ссср?' , '1991', '2023' , '2000', '1424'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Мемори кард')
btn_OK=QPushButton('Ответить')
lb_question = QLabel('В коком году была основана Москва')

RadioGroupBox=QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1816')
rbtn_4 = QRadioButton('1943')

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

LAYOUT_ANS1=QHBoxLayout()
LAYOUT_ANS2=QVBoxLayout()
LAYOUT_ANS3=QVBoxLayout()
LAYOUT_ANS2.addWidget(rbtn_1)
LAYOUT_ANS2.addWidget(rbtn_2)

LAYOUT_ANS3.addWidget(rbtn_3)
LAYOUT_ANS3.addWidget(rbtn_4)

LAYOUT_ANS1.addLayout(LAYOUT_ANS2)
LAYOUT_ANS1.addLayout(LAYOUT_ANS3)

RadioGroupBox.setLayout(LAYOUT_ANS1)


AnsGroupBox=QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_corect = QLabel('Ответ будет тут?')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_corect, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)


layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch = 2)
layout_card.addLayout(layout_line2,stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_corect.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()  

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика \n -всего вопросов:' , window.total , '\n - правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг:', (window.score/window.total*100,'%'))



def next_question():
    window.total +=1
    print('Статистика \n -всего вопросов:' , window.total, '\n - правильных ответов:', window.score)
    cur_question = randint(0, len(question_list)-1)
    q=question_list[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'ответить':
        check_answer()
    else:
        next_question()





window.score = 0
window.total = 0
if window.total >= 15:
    if window.score >= 10:
        show_correct.hide()
        show_correct(QLabel,'МОЛОДЕЦ ТЫ ВЫИГРАЛ!')
    else:
        show_correct.hide()
        textgamov=(QLabel,'ГДЕ-ТО ТЫ ОТВЕТИЛ НЕ ТАК')

btn_OK.clicked.connect(click_ok)
next_question()
window.setLayout(layout_card)
window.show()   
app.exec()            