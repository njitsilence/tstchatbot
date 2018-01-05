import json
import watson_developer_cloud

def callWatsonConversation(input):
    conversation = watson_developer_cloud.ConversationV1(
        username='61f4632f-8f8c-4292-b9b8-95382d8ef3d8',
        password='D14UJNo02KCP',
        version='2017-05-26'
    )

    response = conversation.message(
        workspace_id='1c9b588c-8b0e-4ae3-a7e1-83588a30ae81',
        message_input={
            'text': input
        }
    )
    return str((response["output"]["text"][0]))

