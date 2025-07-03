from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckBalance(Action):
    def name(self):
        return "action_check_balance"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="To check your balance, please log in to your online banking portal or use our mobile app.")
        return []