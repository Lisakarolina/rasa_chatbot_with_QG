
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from sqlite_eval import insert_data, insert_data_qa





class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(f"you submitted {tracker.get_slot('sus_1')}")
        insert_data(tracker.get_slot("sensical"), tracker.get_slot("informative"),
                    tracker.get_slot("compare"), tracker.get_slot("sus_1"),
                    tracker.get_slot("sus_2"), tracker.get_slot("sus_3"),
                    tracker.get_slot("sus_4"), tracker.get_slot("sus_5"),
                    tracker.get_slot("sus_6"), tracker.get_slot("sus_7"),
                    tracker.get_slot("sus_8"), tracker.get_slot("sus_9"),
                    tracker.get_slot("sus_10"))



class SaveQA(Action):
    def name(self) -> Text:
        return "save_qa"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        if len(tracker.events) >= 3:
            q = tracker.events[-3].get('text')  # this gives user question
            a = tracker.events[-1].get('text')  # gives bot answers to faq
            insert_data_qa(q, a)


# class ActionFirstMessage(Action):
#
#     def name(self) -> Text:
#         return "action_greet_user"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         msg = "Hi! I'm a bot that can answer questions to \
#         two different topics: 1. Cats and 2.   . Would your \
#         try learning something new by asking me a couple of \
#         questions? Imagine you were writing a little text about \
#         cats. What would you want to know?"
#         dispatcher.utter_message(text=msg)
#
#         return [UserUtteranceReverted()]
