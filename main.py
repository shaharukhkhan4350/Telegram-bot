import logging
from flask import Flask, request
from telegram import  Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters, Updater, ConversationHandler
import json
import calcData1 as datacalc
import requests
username = 'gocorona'
TOKEN = '7de73fff447c450cd4010cf9ac7c2ce7a8a29e44'
#token = '1123715706:AAHJKNKQYTyD3iJDH-tWVkQUdWFyabSA4mY'
token = '893266649:AAGDVt9mq3X7v665qeX3d1pRgaHvkuF8lHU'
from datetime import datetime

now = datetime.now()
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
current_time = now.strftime("%H:%M:%S")
MSGS = {}
QUESTION = 0
BIO = 1
q_list = ['Do you have cough ?',	'Do you have colds ?',	'Are you having Diarrhea ?',	'Do you have sore throat?',	'Are you experiencing MYALGIA or Bodyaches?',	'Do you have a headache?',	'Do you have fever (Temperature 37.8 C or 100 F and above)?',	'Are you having difficulty breathing?',	'Are you experiencing Fatigue?',	'Have you traveled recently during past 14 days?',	'Do you have a travel history to a COVID-19 INFECTED AREA?',	'Do you have direct contact or is taking care of a positive COVID-19 Patient?']
#q_list = ['क्या आपको खांसी है?','क्या आपको जुकाम है?','क्या आपको दस्त हो रहे हैं?', 'क्या आपको गले में खराश है?',' क्या आप MYALGIA या शरीर मैं दर्द का अनुभव कर रहे हैं? ', 'क्या आपको सिरदर्द है? ? ',' क्या आपको बुखार है (तापमान 37.8 C या 100 F और इससे अधिक)? ',' क्या आपको सांस लेने में कठिनाई हो रही है? ',' क्या आप थकान का अनुभव कर रहे हैं? ',' क्या आपने पिछले 14 दिनों के दौरान हाल ही में यात्रा की है? ' 'क्या आपके पास COVID-19 से प्रभावित क्षेत्र के लिए एक यात्रा इतिहास है?', 'क्या आपका सीधा संपर्क है या सकारात्मक COVID-19 रोगी की देखभाल कर रहा है?']
q_score = [1,1,1,1,1,1,1,2,2,3,3,3]
q_rank = 0
total_score = 0
print("New")
def check(update, context):
    global q_rank
    global total_score
    q_rank = 0
    total_score = 0
    reply_keyboard = [['YES', 'NO']]
    q_rank += 1
    mess_text = """Hi! My name is Professor Bot. I will hold a conversation with you.
        Send /cancel to stop talking to me.\n\n""" + q_list[q_rank-1]
    update.message.reply_text(mess_text,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return QUESTION


def questionN(update, context):
    global total_score
    global q_rank
    if(update.message.text=="YES"):
        total_score = total_score + q_score[q_rank - 1]
    reply_keyboard = [['YES', 'NO']]
    print(total_score)
    if(q_rank < len(q_list)):
        update.message.reply_text(q_list[q_rank],
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        q_rank += 1
        return QUESTION
    elif(total_score>=0 and total_score <=2):
        mess_text = "Your Covid-19 score is: " + str(total_score) +"\n May be stress related and observe"
        update.message.reply_text(mess_text, reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    elif(total_score>=3 and total_score <=5):
        mess_text = "Your Covid-19 score is: " + str(total_score) +"\n Hydrate properly and proper personal hygiene, Observe and Re-eveluate after 2 days"
        update.message.reply_text(mess_text, reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    elif(total_score>=6 and total_score <=12):
        mess_text = "Your Covid-19 score is: " + str(total_score) +"\n Seek a consultation with Doctor"
        update.message.reply_text(mess_text, reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        mess_text = "Your Covid-19 score is: " + str(total_score) +"\n Please call the state helpline number or 24X7 helpline numbers of Ministry of Health and Family Welfare, Government of India.1075 (Toll Free) | 011-23978046 https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf \n If you are from a different country please contact your respective helpline number."
        update.message.reply_text(mess_text, reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
def cancel(update, context):
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END
def bio(update, context):
    return ConversationHandler.END



# handlers
def start(update, context):
    """Send a message when the command /start is issued."""
    #my_list = datacalc.calcData.GloBal_Total(True)
    #messagetext = "Total Cases: " + str(my_list[0]) + "\n New Cases: " + str(my_list[1]) + "\n Total Deaths: " + str(my_list[2]) + "\n New Deaths: " + str(my_list[3]) + "\n Total Recovered: " + str(my_list[4]) + "\n New Recovered: "+str(my_list[5]) +"\n Total Active: " + str(my_list[6])
    #update.message.reply_text(current_time + 'Running from PythonAnywhere main.py!')
    update.message.reply_text("Hello, This is Covid-19 bot created by Data Science Nuggets. You can use this bot for Updates on Covid-19.\n Few commands >> \n /cases - to get all the cases of covid - 19\n /news  - to get all the lastest news of covid - 19 and much more\n Check the how to \n https://www.youtube.com/watch?v=2KJhwj85Qxw")

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help2!')


def echo(update, context):
    #chat_id = bot.get_updates()[-1].message.chat_id
    #if "hello" in update.message.text:
    #    update.message.reply_text("you said Hellov3")
    #else:
    #    mytext = "not working"+str(len(update.message.text))
    #    update.message.reply_text(mytext)
    """Echo the user message."""

    if (len(update.message.text)):

        command = update.message.text
        command = command.lower()
        print ('Got command: %s' % command)

        if('/start' in command):
            update.message.reply_text("Hello , This is Covid-19 chatbot created by Data Science Nuggets. You can use this bot for Updates on Covid-19.\n commands \n cases - to get all the cases of covid - 19\n deaths - to get number of deathsdue to covid - 19\n recovered - to get all the  recoverd cases of covid - 19 \n news  - to get all the lastest news of covid - 19\n top - to get an image of the top effected countries")

        if('cases' in command):
            my_list = datacalc.calcData.GloBal_Total(True)
            #messagetext = "Total Cases: " + str(my_list[0]) + "\n New Cases: " + str(my_list[1]) + "\n Total Deaths: " + str(my_list[2]) + "\n New Deaths: " + str(my_list[3]) + "\n Total Recovered: " + str(my_list[4]) + "\n New Recovered: "+str(my_list[5]) +"\n Total Active: " + str(my_list[6])
            update.message.reply_text(my_list)
            #update.message.reply_text(command)

        if ('country' in command):
            country_command  = command.split(" ")
            if (len(country_command)>=2):
                country_text = " ".join(country_command[1:])


                my_list = datacalc.calcData.country_data(True, country_text)
                if(len(country_text)<4):
                    ctry = str(country_text).upper()
                else:
                    ctry = str(country_text).capitalize()
                messagetext = "Country: " + ctry + "\n" + my_list
                #messagetext = "Country: " + str(my_list[7]) + "\n Total Cases: " + str(my_list[0]) + "\n New Cases: " + str(my_list[1]) + "\n Total Deaths: " + str(my_list[2]) + "\n New Deaths: " + str(my_list[3]) + "\n Total Recovered: " + str(my_list[4]) + "\n New Recovered: "+ str(my_list[5])+ "\n Total Active: " + str(my_list[6])
                update.message.reply_text(messagetext)

            else:
                country_text = "India"
                my_list = datacalc.calcData.country_data(True, country_text)
                list_countries = datacalc.calcData.country_list(True)
                messagetext = str(list_countries) + "\n Example: /country India \n Results: \n " + "Country: India \n" + my_list
                #messagetext = str(list_countries) + "\n Example: /country India \n Results: \n " + "Country: " + str(my_list[7]) + "\n Total Cases: " + str(my_list[0]) + "\n New Cases: " + str(my_list[1]) + "\n Total Deaths: " + str(my_list[2]) + "\n New Deaths: " + str(my_list[3]) + "\n Total Recovered: " + str(my_list[4]) + "\n New Recovered: "+ str(my_list[5])+ "\n Total Active: " + str(my_list[6])
                update.message.reply_text(messagetext)
        if ('recovered' in command):
            update.message.reply_text("Total Recovered of covid-19 Around the Globe = 95,834")

        if ('precautions' in command):
            update.message.reply_text("1. Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.\n 2. Maintain at least 1 metre distance between you and people coughing or sneezing.\n 3. Avoid touching your face.\n 4. Cover your mouth and nose when coughing or sneezing.\n 5. Stay home if you feel unwell.\n 6. Refrain from smoking and other activities that weaken the lungs.\n 7. Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people.\n For more WHO standard precautions visit https://www.who.int/csr/resources/publications/EPR_AM2_E7.pdf?ua=1")
			#bot.sendPhoto(chat_id, open("un.png", 'rb'))
			#bot.sendPhoto(chat_id, open("pre.png", 'rb'))

		#if 'symptoms' in command:
			#bot.sendMessage(chat_id, "Reported illnesses have ranged from mild symptoms to severe illness and death for confirmed coronavirus disease 2019 (COVID-19) cases.These symptoms may appear 2-14 days after exposure (based on the incubation period of MERS-CoV viruses).\n1.Fever\n2.Cough\n3.Shortness of breath\n4.Trouble breathing\n5.Persistent pain or pressure in the chest\n6.New confusion or inability to arouse\n7.Bluish lips or face")
			#bot.sendPhoto(chat_id, open("sy.png", 'rb'))


        #if 'top' in command:
            #pass
            #bot.sendPhoto(chat_id, open("covid-1.png", 'rb'))
        if ('symptoms' in command):
            update.message.reply_text("1) Common symptoms include fever tiredness, dry cough\n 2) Other Symptoms include shortness of breath, aches and pains, sore throat and very few people will report diarrhoea, nausea or a runny nose.\n For latest info from WHO symptoms https://www.who.int/health-topics/coronavirus#tab=tab_3")

        if ('covidtest' in command):
            url = "https://www.dropbox.com/s/p0bpbvoh1r92z2i/corona_automate.jpg?dl=0"
            update.message.reply_photo(url)

        if ("dont" in command):
            Dont_urls = ["https://www.dropbox.com/s/kyfbs666kx2i4i7/dont1.jpg?dl=0", "https://www.dropbox.com/s/q7pswod5pvika45/dont2.jpg?dl=0", "https://www.dropbox.com/s/svccvtsfewkyslm/dont3.jpg?dl=0"]
            for item in Dont_urls:
                update.message.reply_photo(item)
                #reply_msg = update.message.reply_to_message
                #wx_msg = MSGS.get(reply_msg)
                #wx_msg.reply_image(item)
                #update.message.photo[-1].get_file().download(


			#url = 'https://www.dropbox.com/s/pmbv9kbijmkgvhz/do1.jpg?dl=0'


        elif ('do' in command):
            Do_urls = ["https://www.dropbox.com/s/pmbv9kbijmkgvhz/do1.jpg?dl=0", "https://www.dropbox.com/s/wns67ulmzogngtp/do2.jpg?dl=0", "https://www.dropbox.com/s/psex5njfowxu2vb/do3.jpg?dl=0"]
            for item in Do_urls:
                update.message.reply_photo(item)

        if ("whotips" in command):
            Dont_urls = ["https://www.dropbox.com/s/kyn0bjwql7hdcdz/mask-1.jpg?dl=0", "https://www.dropbox.com/s/b9lj2wl3bep9y0e/mask-2.jpg?dl=0", "https://www.dropbox.com/s/ordf9on5x9mk316/mask-3.jpg?dl=0","https://www.dropbox.com/s/65in7c4tlnvfjqb/mask-4.jpg?dl=0","https://www.dropbox.com/s/19n2vi4erpqq3uw/masks-5.png?dl=0","https://www.dropbox.com/s/6fmxjhkyz4919v2/masks-6.png?dl=0","https://www.dropbox.com/s/aw3wcp6do73d53x/masks-7.png?dl=0"]
            for item in Dont_urls:
                update.message.reply_photo(item)

        if ('news' in command):
			# country_list =['in', 'us', 'gb']
			# button_list = [[KeyboardButton(s)] for s in country_list]
			# reply_markup = ReplyKeyboardMarkup(button_list)
			# bot.sendMessage(command, "A two-column menu", reply_markup=reply_markup)
            val1= command.split(" ")
            API_KEY = '2850ab2ec8504fe389bb02b98a601ca9'
            if len(val1) < 2:
                val1.append("in")
            params = {
				'q': 'coronavirus',
				'source': 'bbc-news',
				'sortBy': 'top',
				'language': 'en',
				#'category': 'business',
				'country': val1[1],
				#'apiKey': API_KEY,
			}

            headers = {
				'X-Api-Key': API_KEY,  # KEY in header to hide it from url
			}

            url = 'https://newsapi.org/v2/top-headlines'

            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            articles = data["articles"]
            results = [arr["title"] for arr in articles]
            result_url = [arr["url"] for arr in articles]
			# print(results)
			# print(data)
            news_head = ["Headliness Now: \n "]
            for index, item in enumerate(results):
				#<a href="www.google.com">www.google.com</a>
				#news_head.append(str(index + 1)+ ": "+"<html> <a href="+result_url[index]+">"+ item +"</a></html>"+"\n \n")
                news_head.append(str(index + 1)+ ": "+ item +"\n \n")
            head_news = " ".join(news_head)
            update.message.reply_text(head_news)




app = Flask(__name__)
def main():
    # add dispatcher
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    #bot = Bot(token)
    #dp = Dispatcher(bot, None, workers=0, use_context=True)
#    bot = Bot(token)
    print("Running")
 #   dp = Dispatcher(bot, None, workers=0, use_context=True)
    # add handlers

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('covidtest', check)],

        states={
            QUESTION: [MessageHandler(Filters.regex('^(YES|NO)$'), questionN)],
            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()
    # start webhook
    bot = dp.bot
    bot.delete_webhook()
    url = f"https://{username}.pythonanywhere.com/{TOKEN}"
    bot.set_webhook(url=url)
        # process updates
    @app.route('/' + TOKEN, methods=['POST'])
    def webhook():
        json_string = request.stream.read().decode('utf-8')
        update = Update.de_json(json.loads(json_string), bot)
        dp.process_update(update)
        return 'ok', 200

# make sure you've inserted your app.py name
if __name__ == "__main__":
    main()
