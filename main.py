from telebot import types, TeleBot
################$#
from pytube import YouTube
def audio(text):
    global sifat
    global aname
    yt=YouTube(text)
    aname = yt.title
    if yt.streams.filter(only_audio=True, abr="160kbps"):      
        yt.streams.filter(only_audio=True,abr="160kbps").first().download(filename='saudio')
        sifat="160kbps"
    elif yt.streams.filter(only_audio=True,abr="128kbps"):
        yt.streams.filter(only_audio=True,abr="128kbps").first().download(filename='saudio')
        sifat="128kbps"
    else:
        yt.streams.filter(only_audio=True).first().download(filename='saudio')
def video(text):
    global sifatv
    yt=YouTube(text)
    if yt.streams.filter(progressive=True, res='1080p'):      
        yt.streams.filter(progressive=True, res='1080p').first().download(filename='svideo')
        sifatv='1080p'
    elif yt.streams.filter(progressive=True,res="720p"):
        yt.streams.filter(progressive=True,res="720p").first().download(filename='svideo')
        sifatv='720p'
    elif yt.streams.filter(progressive=True,res="480p"):
        yt.streams.filter(progressive=True,res="480p").first().download(filename='svideo')
        sifatv="480p"
    elif yt.streams.filter(progressive=True,res="360p"):
        yt.streams.filter(progressive=True,res="360p").first().download(filename='svideo')
        sifatv="360p"
    else:
        yt.streams.filter(progressive=True).first().download(filename='svideo')
        sifatv="144p"
########$##$$$$#$
from botdata import qoshish, amal
bot= TeleBot('1699547688:AAHjXPWPT1_u8l1SzI2F23Smj96B1l32BlA')
@bot.message_handler(commands=['start'])
def start(message):
    if amal(int(message.from_user.id)):
        bot.send_message(message.from_user.id, f'<b>Yana bir bor xush kelibsiz {message.from_user.first_name}\nMenga Link Yuboring...</b>',parse_mode='html')
    else:
        qoshish(message.from_user.id, message.from_user.user_name, message.from_user.first_name, message.from_user.last_name)
        bot.send_message(message.from_user.id, f'<b>Xush kelibsiz {message.from_user.first_name}* \nMenga Link Yuboring...</b>',parse_mode='html') 
@bot.message_handler(content_types=['text'])
def text(message):
    global sifat
    global sifatv
    try:
        video(message.text)
        audio(message.text)
        markp = types.InlineKeyboardMarkup()
        markp.add(types.InlineKeyboardButton('📽Video',callback_data='video'))
        markp.add(types.InlineKeyboardButton('🎧Audio',callback_data='audio'))
        bot.send_message(message.from_user.id , message.text,reply_markup=(markp))
    except:
        bot.send_message(message.from_user.id, '<b>Link</b> Xato Yuborilgan \nIltimos Qayta Urinib Ko\'ring',parse_mode='html')
@bot.callback_query_handler(func=lambda call: True)
def  test_callback(call):
    global sifat
    global sifatv
    if call.data=='video':
        try:
            vid = open('svideo.mp4','rb')
            bot.send_video(call.from_user.id,vid, caption=f'*{aname}*\nSifati: *{sifatv}*\n[TigerTube](t.me/TigerTube_bot)' , parse_mode='Markdown')
        except:
            bot.send_message(call.from_user.id,'Kontent o`lchami 50mb oshib ketdi.')
    if call.data=='audio':
        try:
            aud = open('saudio.webm','rb')
            bot.send_audio(call.from_user.id, aud, caption=f'*{aname}*\nSifati: *{sifat}*\n[TigerTube](t.me/TigerTube_bot)' , parse_mode='Markdown')
        except:
            bot.send_message(call.from_user.id,'Kontent o`lchami 50mb oshib ketdi.')
bot.polling(none_stop=(True))



