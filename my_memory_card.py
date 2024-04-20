from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QMessageBox,QRadioButton,QHBoxLayout,QGroupBox,QPushButton,QButtonGroup
from random import shuffle, randint

class Qeustion():
    def __init__(self, qestion,right_answer,wrong1,wrong2,wrong3):
        self.qestion = qestion
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
qestion_list = []
qestion_list.append(Qeustion('Какой язык международый?','английский','французский','итальянский','русский'))
qestion_list.append(Qeustion('У какого животного самая длинная шея в мире?','жираф','слон','носорог','леопард'))
qestion_list.append(Qeustion('Какой континент самый большой?','Евразия','Африка','Австралия','Южная Америка'))
qestion_list.append(Qeustion('Где аходится Биг Бен?','Лондон','Париж','Москва','Нью-Ёрк'))
qestion_list.append(Qeustion('Какое животное самое быстрое в мире?','гепард','леопард','слон','пума'))
qestion_list.append(Qeustion('Где находится река Мисисипи?','Америка','Россия','Австралия','Англия'))
qestion_list.append(Qeustion('Как дела?','хорошо','плохо','отлично','ужасно'))
qestion_list.append(Qeustion('Какой транспорт самый удобный?','машина','троллейбус','автобус','газель'))
qestion_list.append(Qeustion('Какое животное имеет чёрно-белые полоски?','зебра','крокодил','бегемот','тушканчик'))
qestion_list.append(Qeustion('Какое самое большое морское животное','косатка','черепаха','пингвин','белая акула'))
app = QApplication([]) 
main_win = QWidget()
qestion = QLabel('Какой национальности не существует')
ok = QPushButton('ответить')
der = QGroupBox('Варианты ответов')
main_win.resize(400,200)
main_win.setWindowTitle('memo card')

b = QRadioButton('Энцы')
b1 = QRadioButton('Смурфы')
b2 = QRadioButton('Чульянцы')
b3 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(b)
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line1.addWidget(b)
line1.addWidget(b1)
line2.addWidget(b2)
line2.addWidget(b3)
line.addLayout(line1)
line.addLayout(line2)
der.setLayout(line)
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Прав ты или нет')
correct = QLabel('Ответ будет здесь')
lauout_line2 = QVBoxLayout()
lauout_line2.addWidget(result, alignment=(Qt.AlignLeft|Qt.AlignTop))
lauout_line2.addWidget(correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(lauout_line2)

line4 = QVBoxLayout()
line4.addWidget(qestion, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
line4.addWidget(der)
line4.addWidget(AnsGroupBox)
AnsGroupBox.hide()
line4.addWidget(ok,stretch=2)
main_win.setLayout(line4)

def show_result():
    der.hide()
    AnsGroupBox.show()
    ok.setText('продолжить')
def show_qestion():
    AnsGroupBox.hide()
    der.show()
    ok.setText('ответить')
    RadioGroup.setExclusive(False)
    b.setChecked(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    RadioGroup.setExclusive(True)
answer = [b,b1,b2,b3]
def ask(q: Qeustion):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    qestion.setText(q.qestion)
    correct.setText(q.right_answer)
    show_qestion()
def show_correct(res):
    result.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show_correct('верно')
        main_win.score +=1
        print('Сатистика \n Всего вопросов -',main_win.total,'\n Количество правильных ответов -', main_win.score)
        print('Рейтинг:',main_win.score/main_win.total*100,'%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('неверно')
            print('Рейтинг:',main_win.score/main_win.total*100,'%')
def next_qeuston():
    main_win.total += 1
    print('Сатистика \n Всего вопросов -',main_win.total,'\n Количество правильных ответов -', main_win.score)
    cur_question = randint(0, len(qestion_list) - 1)
    q = qestion_list[cur_question]
    ask(q)
def click_ok(): 
    if ok.text() == 'ответить':
        check_answer()
    else:
        next_qeuston()
q = Qeustion('какое время года?','осень','зима','лето','весна')
main_win.total = 0
main_win.score = 0
ok.clicked.connect(click_ok)
next_qeuston()
main_win.show()
app.exec_()