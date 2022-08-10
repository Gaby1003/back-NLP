from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from summarizer.summarizer import Summarizer
import json
import base64

# Create your views here.

class Api(APIView): 
     
    def convertBase64ToString(self, base64_txt):
        txt_b64_string = base64_txt.split(",")[1]
        print(txt_b64_string[0:20])
        txt_b64 = txt_b64_string.encode('utf-8')
        txt_bytes = base64.b64decode(txt_b64)
        txt_string = txt_bytes.decode('utf-8')
        return txt_string

    def get(self, request, format=None):
        print(request)
        res = {
            "message": self.summarizer.getSummary()
        }
        return Response(res)

    def post(self, request, format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        info = body['datas']
        txt = self.convertBase64ToString(info)
        summarizer = Summarizer(txt)
        resume = summarizer.process()
        print("request: ", resume)
        return Response(resume)

