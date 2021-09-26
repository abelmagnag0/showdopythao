import json

f = open('teste2.json',)
data = json.load(f)
print(data)

f.close()


# NA LINHA 136 COMEÇA A ULTIMA PERGUNTA
#  {
#       "category": "naopenseiaindanisso",
#       "question": " O que o código abaixo irá reproduzir",
#       "additional": "",
#       "correct_answer": "3",
#       "incorrect_answers": [
#         "1",
#         "7",
#         "15"
#       ]
#     }