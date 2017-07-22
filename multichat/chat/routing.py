from channels import route
from .consumers import ws_connect, ws_receive, ws_disconnect, chat_join, chat_leave, chat_send

from channels import include

# There's no path matching on these routes; we just rely on the matching
# from the top-level routing. We could path match here if we wanted.
websocket_routing = [
    # Called when WebSockets connects
    route("websocket.connect", ws_connect),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_receive),

    # Called when WebSockets disconnects
    route("websocket.disconnect", ws_disconnect),
]

# You can have as many lists here as you like, and choose any name.
# Just refer to the individual names in the include() function.
custom_routing = [
    # Handling different chat commands (websocket.receive is decoded and put
    # onto this channel) - routed on the "command" attribute of the decoded
    # message.
    route("chat.receive", chat_join, command="^join$"),
    route("chat.receive", chat_leave, command="^leave$"),
    route("chat.receive", chat_send, command="^send$"),
]

channel_routing = [
    # Include sub-routing from an app.
    include("chat.routing.websocket_routing", path=r"^/chat/stream"),

    # Custom handler for message sending (see Room.send_message).
    # Can't go in the include above as it's not got a 'path' attribute to match on.
    include("chat.routing.custom_routing"),

    # A default "http.request" route is always inserted by Django at the end of the routing list
    # that routes all unmatched HTTP requests to the Django view system. If you want lower-level
    # HTTP handling - e.g. long-polling - you can do it here and route by path, and let the rest
    # fall through to normal views.
]
