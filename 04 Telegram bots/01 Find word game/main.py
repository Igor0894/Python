import telebot
import time
import datetime
import csv
from telebot import types
import multiprocessing
from multiprocessing import *
import threading
import schedule
import random
import wikipedia

def load_token():
    global token
    f = open('token.txt')
    try:
        token = f.readlines()[0]
    finally:
        f.close()

load_token()
bot = telebot.TeleBot(token)
chats_id = []
games = []

def load_existing_chats_id():
    global chats_id
    f = open('chats.txt')
    try:
        for chat_id in f.readlines():
            if int(chat_id) not in chats_id:
                chats_id.append(int(chat_id))
    finally:
        f.close()

def write_new_chat_id(chat_id):
    global bot, chats_id
    f = open('chats.txt', 'a')
    try:
        if chat_id not in chats_id:
            f.write(str(chat_id) + '\n')
            chats_id.append(int(chat_id))
            bot.send_message(chat_id, 'Вы добавлены в игру как новый пользователь.', reply_markup=types.ReplyKeyboardRemove())
    finally:
        f.close()

def start_schedule_process():#Запуск Process
    global chats_id, bot
    p1 = threading.Thread(target=start_schedule, args=())
    p1.start()

def delete_game(chat_id):
    global games
    for i in range(len(games)):
        if games[i].chat_id == chat_id:
            games.pop(i)
            break

class Game():
    def __init__(self, chat_id, need_ask_ready):
        self.need_ask_ready = need_ask_ready
        self.chat_id = chat_id
        self.ask = 'Готовы играть?'
        self.variables = ['Готов','Не сейчас']
        self.reply_wait = False
        self.playing = False
        self.player_word = '*****'
        self.new_symb_on_right_pos = False
        self.new_symb_on_else_pos = False
        self.symb_on_else_pos = []
        self.symb_on_right_pos = []
        self.count_find_symbols = 0
        self.tries = 0
        self.hint = ''
        self.last_answer_time = datetime.datetime.now()

    def generate_word(self):
        f = open('./words.txt', encoding='utf8', errors='ignore')
        try:
            words = f.readlines()
            line = random.randint(0, len(words))
            self.word = words[line]
            self.word = self.word[0:5]
        finally:
            f.close()

    def find_hint(self):
        wikipedia.set_lang("ru")
        try:
            self.hint = ""
            big_hint = wikipedia.summary(self.word)
            #print(big_hint)
            start_hint = False
            end_hint = False
            for i in big_hint:
                if start_hint and not end_hint:
                    self.hint += i
                if i == '—':
                    start_hint = True
                if i == '.' and start_hint:
                    end_hint = True
        except:
            self.hint = 'Не удалось загрузить подсказку.'
            self.generate_word()
            self.find_hint()

    def start_game(self):
        self.generate_word()
        self.find_hint()
        #bot.send_message(self.chat_id, 'Начнём игру! Слово состоит из 5 букв. Слово: ' + self.word + ' Подсказка: ' + self.hint)
        bot.send_message(self.chat_id, 'Начнём игру! Слово состоит из 5 букв.' + ' Подсказка: ' + self.hint, reply_markup=types.ReplyKeyboardRemove())
        self.playing = True
        self.reply_wait = True

    def asking(self):
        if self.need_ask_ready:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in self.variables:
                item1 = types.KeyboardButton(i)
                markup.add(item1)
            bot.send_message(self.chat_id, self.ask, reply_markup=markup)
            self.reply_wait = True
        else:
            self.start_game()

    def verification_word(self, word):
        self.new_symbols_on_right_pos = False
        self.new_symb_on_else_pos = False
        for i in range(len(word)):
            if word[i] == self.word[i] and self.player_word[i] == '*':
                self.player_word = self.player_word[0:i] + word[i] + self.player_word[i+1:len(self.player_word)]
                self.symb_on_right_pos.append(word[i])
                self.new_symb_on_right_pos = True
                self.count_find_symbols += 1
                if len(self.symb_on_else_pos) != 0:
                    j = 0
                    while j < len(self.symb_on_else_pos):
                        if self.symb_on_else_pos[j] == word[i]: #list index out of range
                            need_else = False
                            for s in range(len(self.player_word)):
                                if self.player_word[s] == '*' and self.word[s] == word[i]:
                                    need_else = True
                            if not need_else:
                                self.symb_on_else_pos.pop(j)
                        j += 1
            else:
                for j in range(len(self.word)):
                    if self.word[j] == word[i] and word[i] not in self.symb_on_else_pos and word[i] not in self.symb_on_right_pos:
                        self.symb_on_else_pos.append(word[i])
                        self.new_symb_on_else_pos = True

    def replying(self, message):
        if message.text in self.variables and not self.playing:
            if self.ask == 'Готовы играть?':
                if message.text == 'Готов':
                    self.start_game()
                else:
                    bot.send_message(self.chat_id, 'До встречи!', reply_markup=types.ReplyKeyboardRemove())
                    delete_game(self.chat_id)
        elif self.playing:
            self.tries += 1
            '''print('Разница во времени = ' + str(datetime.datetime.now() - self.last_answer_time))
            print(datetime.time(minute=10))'''
            self.last_answer_time = datetime.datetime.now()
            if len(message.text) != 5:
                bot.send_message(self.chat_id, 'Ошибка! Слово должно состоять из 5 строчных букв.', reply_markup=types.ReplyKeyboardRemove())
                self.reply_wait = True
            else:
                word_from_gamer = message.text.lower()
                self.verification_word(word_from_gamer)
                ecran_pl_wrd = self.player_word.replace('*', '\*')
                answer = ''
                new_symb_on_else_pos_str = ','.join(self.symb_on_else_pos)
                if self.new_symb_on_else_pos and self.count_find_symbols < 5:
                    if self.new_symb_on_right_pos:
                        answer = 'Найдены буквы на своих местах: *[' + ecran_pl_wrd + ']* , так же ещё найдены присутствующие в слове буквы: *' + new_symb_on_else_pos_str + '*'
                    elif self.player_word == '*****':
                        answer = 'Найдены присутствующие в слове буквы: *' + new_symb_on_else_pos_str + '*'
                    else:
                        answer = 'Найдены присутствующие в слове буквы: *' + new_symb_on_else_pos_str + '* ,отгаданная часть слова: *[' + ecran_pl_wrd + ']*'
                elif self.count_find_symbols < 5:
                    if self.new_symb_on_right_pos and len(self.symb_on_else_pos) != 0:
                        answer = 'Найдены буквы на своих местах: *[' + ecran_pl_wrd + ']* , так же в слове присутствуют буквы: *' + new_symb_on_else_pos_str + '*'
                    elif self.new_symb_on_right_pos and len(self.symb_on_else_pos) == 0:
                        answer = 'Найдены буквы на своих местах: *[' + ecran_pl_wrd +']*'
                    elif self.player_word == '*****' and len(self.symb_on_else_pos) == 0:
                        answer = 'Не угадано ни одной буквы, пробуйте ещё\!'
                    elif self.player_word == '*****' and len(self.symb_on_else_pos) != 0:
                        answer = 'Не угадано ни одной новой буквы. В слове присутствуют буквы: *' + new_symb_on_else_pos_str + '*'
                    elif self.player_word != '*****' and len(self.symb_on_else_pos) == 0:
                        answer = 'Не угадано ни одной новой буквы. Отгаданная часть слова: *[' + self.player_word + ']*'
                    elif self.player_word != '*****' and len(self.symb_on_else_pos) != 0:
                        answer = 'Не угадано ни одной новой буквы. Отгаданная часть слова: *[' + self.player_word + ']* , так же в слове присутствуют буквы: *' + new_symb_on_else_pos_str + '*'
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    '''for i in ['/Новая_игра']:
                        item1 = types.KeyboardButton(i)
                        markup.add(item1)'''
                    answer = 'Поздравляю! Вы угадали слово! С ' + str(self.tries) + ' попытки.'
                    self.playing = False
                    #bot.send_message(self.chat_id, answer, reply_markup=markup)
                    bot.send_message(self.chat_id, answer, reply_markup=types.ReplyKeyboardRemove())
                    delete_game(self.chat_id)
                    return
                if self.playing:
                    answer = answer.replace(".","\.")
                    bot.send_message(self.chat_id, answer, parse_mode='MarkdownV2', reply_markup=types.ReplyKeyboardRemove())
                    self.reply_wait = True


def add_game(chat_id, need_ask_ready):
    global games
    new_game = Game(chat_id, need_ask_ready)
    games.append(new_game)
    new_game.asking()

def start_schedule():  # Запуск schedule
    schedule.every(1).day.at("08:00").do(auto_ask_to_add_game)
    #schedule.every(10).seconds.do(auto_ask_to_add_game)
    while True:  # Запуск цикла
        schedule.run_pending()
        time.sleep(1)

def auto_ask_to_add_game():
    global chats_id
    for chat_id in chats_id:
        [find, game] = find_game_running_chat(chat_id)
        if not find or ((datetime.datetime.now() - game.last_answer_time) > datetime.timedelta(minutes=10)):
            delete_game(chat_id)
            add_game(chat_id, True)

def find_game_running_chat(chat_id):
    global games
    for i in range(len(games)):
        if games[i].chat_id == chat_id:
            return [True, games[i]]
    return [False, None]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=types.ReplyKeyboardRemove())
    write_new_chat_id(message.chat.id)

@bot.message_handler(commands=['new_game'])
def start_message(message):
    [find_game, game] = find_game_running_chat(message.chat.id)
    if not find_game:
        add_game(message.chat.id, False)
    else:
        bot.send_message(message.chat.id, 'Вы не угадали слово: *' + game.word + '*', parse_mode='MarkdownV2', reply_markup=types.ReplyKeyboardRemove())
        delete_game(message.chat.id)
        add_game(message.chat.id, False)

@bot.message_handler(content_types='text')
def message_reply(message):
    [find_game, game] = find_game_running_chat(message.chat.id)
    if find_game and game.reply_wait:
        game.reply_wait = False
        game.replying(message)

if __name__ == '__main__':
    load_existing_chats_id()
    start_schedule_process()
    '''markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in ['/Подписка','/Новая_игра']:
        item1 = types.KeyboardButton(i)
        markup.add(item1)'''
    for chat_id in chats_id:
        bot.send_message(chat_id, 'Запуск бота', reply_markup=types.ReplyKeyboardRemove())
        #bot.send_message(chat_id, 'Запуск бота')
    try:
        #bot.polling(none_stop=True)
        bot.infinity_polling(timeout=10, long_polling_timeout = 5)
    except:
        print("Polling out")
        pass


