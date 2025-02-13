
from telegram import Bot



class librairie():
    session = 'line2'
    api_id = 25837876
    api_hash = '51bb06dbd238cdf2f5b085cd53a9d44f'
    phone_number = '+32477724509'
    bot_token = '7181142934:AAGxxLdS7hZ4LpwUdh-chNPcxko86I0_u_Q'
    user_ids = ['5836026820']  # Les ID des utilisateurs à ajouter

    bot = Bot(token=bot_token)

    def __init__(self):
        pass

    def getAPI(self):
        return self.api_id
    def getPhoneNumber(self):
        return self.phone_number
    def getBotToken(self):
        return self.bot_token
    def getUserIds(self):
        return self.user_ids
    def getBot(self):
        return self.bot
    def getHash(self):
        return self.api_hash
    def getSession(session=None):
        return session


