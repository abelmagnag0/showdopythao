from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
import json
import pandas as pd
import random
# esse daqui é o de colocar tempo, dps da uma olahda
from threading import Timer

api = open('db.json',)
data = json.load(api)
df = pd.DataFrame(data["results"])


def preload_data(idx):
    question = df["question"][idx]
    correct = df["correct_answer"][idx]
    wrong = df["incorrect_answers"][idx]

    formatting = [
        ("#039;", "'"),
        ("&'", "'"),
        ("&quot;", '"'),
        ("&lt;", "less than SYMBOL"),
        ("&gt;", "greater than SYMBOL")
    ]

    for tuple in formatting:
        question = question.replace(tuple[0], tuple[1])
        correct = correct.replace(tuple[0], tuple[1])

    for tuple in formatting:
        wrong = [char.replace(tuple[0], tuple[1]) for char in wrong]

    parameters["question"].append(question)
    parameters["correct"].append(correct)

    all_answers = wrong + [correct]
    random.shuffle(all_answers)

    parameters["answer1"].append(all_answers[0])
    parameters["answer2"].append(all_answers[1])
    parameters["answer3"].append(all_answers[2])
    parameters["answer4"].append(all_answers[3])
    print(parameters["correct"][-1])


parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "correct": [],
    "score": [],
    "index": []
}

# variavel global com os widgets que mudam dinamicamente
widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "message": [],
    "message2": [],
    "ajuda1": [],
    "ajuda2": []
}

contador_score = 0

# start grid
grid = QGridLayout()


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def clear_parameters():
    for parm in parameters:
        if parameters[parm] != []:
            for i in range(0, len(parameters[parm])):
                parameters[parm].pop()

    parameters["index"].append(random.randint(0, 25))
    parameters["score"].append(0)

    global contador_score
    contador_score = 0


def show_frame1():
    clear_widgets()
    frame1()


def start_game():
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    frame2()


def create_buttons(answer, l_margin, r_margin):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border: 4px solid '#008878';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        "color: #FCFAEC;" +
        "font-family: 'shanti';" +
        "font-size: 12px;" +
        "white-space: no-wrap;"
        "border-radius: 15px;" +
        "padding: 8px 0;" +
        "background: '#008878';" +
        "margin-top: 20px}" +
        "*:hover{color: #1E1C0C;" +
        "font-weight: bold;}"
    )
    button.clicked.connect(lambda x: is_correct(button))
    return button


def format_score():
    global contador_score

    if contador_score == 0:
        new_score = '500'
    elif contador_score == 1:
        new_score = '1k'
    elif contador_score == 2:
        new_score = '2.5k'
    elif contador_score == 3:
        new_score = '5k'
    elif contador_score == 4:
        new_score = '25k'
    elif contador_score == 5:
        new_score = '100k'
    elif contador_score == 6:
        new_score = '250k'
    elif contador_score == 7:
        new_score = '500k'
    elif contador_score == 8:
        new_score = '1M'

    
    contador_score += 1

    return new_score


def is_correct(btn):

    if btn.text() == parameters["correct"][-1]:
        new_score = format_score()
        parameters["score"].pop()
        parameters["score"].append(new_score)

        parameters["index"].pop()
        parameters["index"].append(random.randint(0, 25))

        preload_data(parameters["index"][-1])

        widgets["score"][-1].setText(parameters["score"][-1])
        widgets["question"][0].setText(parameters["question"][-1])
        widgets["answer1"][0].setText(parameters["answer1"][-1])
        widgets["answer2"][0].setText(parameters["answer2"][-1])
        widgets["answer3"][0].setText(parameters["answer3"][-1])
        widgets["answer4"][0].setText(parameters["answer4"][-1])

        if contador_score > 8:
            clear_widgets()
            frame3()
    else:
        clear_widgets()
        frame4()


def frame1():
    clear_widgets()

    # display logo
    image = QPixmap("assets/logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 100px;"
    )
    widgets["logo"].append(logo)

    # button widget
    button = QPushButton("PLAY ►")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{background: #006B5F;" +
        "border-radius: 20px;" +
        "font-size: 35px;" +
        "font-weight: bold;"
        "color: #f6f6f6;" +
        "padding: 25px 0;" +
        "margin: 50px 200px;}" +
        "*:hover{font-size: 33px}"
    )

    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

# def start_countdown():
#     t = Timer(number_of_seconds, timeout)
#     t.start()
#     clear_widgets()
#     frame4()

def frame2():
    ajuda1 = QPushButton("Universitários")
    ajuda1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    ajuda1.setFixedWidth(100)
    ajuda1.setStyleSheet(
        "*{border: 4px solid '#8fc740';" +
        "color: #FCFAEC;" +
        "font-family: 'shanti';" +
        "font-size: 12px;" +
        "white-space: no-wrap;"
        "border-radius: 15px;" +
        "background: '#8fc740';" +
        "margin-top: 20px}" +
        "*:hover{color: #1E1C0C;" +
        "font-weight: bold;}"
    )
    # button.clicked.connect(lambda x: is_correct(button))
    widgets["ajuda1"].append(ajuda1)

    ajuda2 = QPushButton("1/2")
    ajuda2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    ajuda2.setFixedWidth(100)
    ajuda2.setStyleSheet(
        "*{border: 4px solid '#8fc740';" +
        "color: #FCFAEC;" +
        "font-family: 'shanti';" +
        "font-size: 12px;" +
        "white-space: no-wrap;"
        "border-radius: 15px;" +
        "background: '#8fc740';" +
        "margin-top: 20px}" +
        "*:hover{color: #1E1C0C;" +
        "font-weight: bold;}"
    )
    ajuda2.clicked.connect(lambda x: corta_metade(ajuda2))
    widgets["ajuda2"].append(ajuda2)

    score = QLabel(str(parameters["score"][-1]))
    score.setAlignment(QtCore.Qt.AlignLeft)
    score.setStyleSheet(
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 10px 0px;" +
        "margin: 20px 0px;" 
    )
    widgets["score"].append(score)
    def corta_metade():
        return "soltaram os cobrao"
        
    question = QLabel(parameters["question"][-1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 15px;" +
        "text-align: justify;" +
        "background: #045245;" +
        "border-radius: 20px;" +
        "color: 'white';" +
        "padding: 20px 10px;"
    )
    widgets["question"].append(question)

    button1 = create_buttons(parameters["answer1"][-1], 85, 5)
    button2 = create_buttons(parameters["answer2"][-1], 5, 85)
    button3 = create_buttons(parameters["answer3"][-1], 85, 5)
    button4 = create_buttons(parameters["answer4"][-1], 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    # trocar pelo github  depois
    image = QPixmap("assets/logopequena.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin: 75px 0 30px 0;"
    )
    widgets["logo"].append(logo)

    grid.addWidget(widgets["score"][-1], 0, 0)
    grid.addWidget(widgets["ajuda1"][-1], 0, 1)
    grid.addWidget(widgets["ajuda2"][-1], 0, 2)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1, 2)

    
def frame3():
    # congratz
    message = QLabel("Parabéns! Você\né um bom programador \ne acaba de faturar: ")
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        "font-family: 'Shanti'; font-size: 25px; color: white; margin: 100px 0px;"
    )
    widgets["message"].append(message)

    # score widget
    score = QLabel(parameters["score"][-1])
    score.setStyleSheet(
        "font-size: 100px; color: #8fc740; margin: 0px 75px 0px 75px;")
    widgets["score"].append(score)

    # voltando ao trabalho
    message2 = QLabel("Ok, agore volte ao trabalho.")
    message2.setAlignment(QtCore.Qt.AlignCenter)
    message2.setStyleSheet(
        "font-family: 'Shanti'; font-size: 30px; color: white; margin-top: 0px; margin-bottom: 75px;"
    )
    widgets["message2"].append(message2)

    # button widget
    button = QPushButton('JOGAR')
    button.setStyleSheet(
        "*{background: '#006B5F'; padding: 25px 0px; border: 1px solid '#006B5F'; color: 'white'; font-family: 'Arial'; font-size 25px; border-radius: 40px; margin: 10px 300px;} *:hover{background:'#8fc740';}"
    )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(frame1)

    widgets["button"].append(button)

    # logo widget
    pixmap = QPixmap('assets/logopequena.png')
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "padding :10px; margin-top:75px; margin-bottom: 20px;"
    )
    widgets["logo"].append(logo)

    # colocando os widgets no grid
    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 5, 0, 2, 2)


def frame4():
    # sorry widget
    message = QLabel("Desculpa, resposta errada,\nvocê iria ganhar:")
    message.setAlignment(QtCore.Qt.AlignRight)
    message.setStyleSheet(
        "font-family: 'Shanti'; font-size: 35px; color: 'white'; margin: 75px 5px; padding:20px;"
    )
    widgets["message"].append(message)

    # score widget
    if(parameters["score"][-1] != 0):
        score = QLabel(parameters["score"][-1])
    else:
        score = QLabel(str(0))

    score.setStyleSheet(
        "font-size: 100px; color: white; margin: 0 75px 0px 75px;")
    widgets["score"].append(score)

    # button widget
    button = QPushButton('Quero tentar de novo')
    button.setStyleSheet(
        '''*{
            padding: 25px 0px;
            background: '#006B5F';
            color: 'white';
            font-family: 'Arial';
            font-size: 35px;
            border-radius: 40px;
            margin: 10px 200px;
        }
        *:hover{
            background: '#8fc740';
        }'''
    )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(frame1)

    widgets["button"].append(button)

    # logo widget
    pixmap = QPixmap('assets/logopequena.png')
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "padding :10px; margin-top:75px;"
    )
    widgets["logo"].append(logo)

    # place widgets on the grid
    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["score"][-1], 1, 1)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 3, 0, 1, 2)

    clear_parameters()

