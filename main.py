#pip install nltk numpy tensorflow

from chatbot import ChatBot
import os
import random

# Importar windows-curses se estiver no Windows
try:
    import curses
except ImportError:
    import windows_curses as curses

myChatBot = ChatBot()

#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

def start_snake_game():
    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    food = [sh // 2, sw // 2]
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    key = curses.KEY_RIGHT
    score = 0

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, sh] or \
                snake[0][1] in [0, sw] or \
                snake[0] in snake[1:]:
            curses.endwin()
            return score

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 1),
                    random.randint(1, sw - 1)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(int(tail[0]), int(tail[1]), ' ')

        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

print("Bem vindo ao Chatbot")

while True:
    pergunta = input("\ncomo posso te ajudar?")
    if pergunta.lower() == "easter egg":
        score = start_snake_game()
        print(f"Você conseguiu {score} pontos! Parabéns por achar o easter egg, posso te ajudar com algo a mais?")
    else:
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")

        while (intencao[0]['intent'] != "despedida"):
            pergunta = input("posso lhe ajudar com algo a mais?")
            if pergunta.lower() == "easter egg":
                score = start_snake_game()
                print(f"Você conseguiu {score} pontos! Parabéns por achar o easter egg, posso te ajudar com algo a mais?")
            else:
                resposta, intencao = myChatBot.chatbot_response(pergunta)
                print(resposta + "   [" + intencao[0]['intent'] + "]")

    if intencao[0]['intent'] == "despedida":
        break

print("Foi um prazer atendê-lo")