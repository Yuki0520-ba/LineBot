from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
import os

from .kansai_reply import api_reply

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK',status=200)


# メッセージ返答
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    #Webhook settingsでのエラー回避
    if event.reply_token == "00000000000000000000000000000000":
        return

    res=api_reply(event.message.text,'太郎')
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=res))
                               