from keys import *
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

'''
MODULE Containing the chatbot class that will be used to connect directly to IBM Watson Assistant
'''

class chatbot(object):

    def __init__(self):

        try:
            self.authenticator = IAMAuthenticator(Watson_Assist_Key)
            self.assistant = AssistantV2(version='2018-09-20', authenticator=self.authenticator)
            self.assistant.set_service_url(Watson_Assist_URL)

        except:
            pass
    

    #Create a session - takes session class, converts to JSON str, then converts to Dict
    def create(self):

        try:

            self.session = self.assistant.create_session(Watson_Assist_ID).get_result()
            self.session_json = json.dumps(self.session, indent=2)
            self.session_dict = json.loads(self.session_json)
            self.session_id = self.session_dict['session_id']

        except:
            pass

    #Deletes a session
    def delete(self):

        try:
            self.assistant.delete_session(Watson_Assist_ID, self.session_id).get_result() 

        except:
            pass

    #Returns a Message to Watson Assistant to be displayed
    def get_message(self):
        pass