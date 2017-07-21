from channels import route, include

def message_handler(message):
    print(message['text'])

channel_routing = [
        route("websocket.receive", message_handler)
]
