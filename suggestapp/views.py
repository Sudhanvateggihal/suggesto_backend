from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import feedback,new_prompt
from .serializers import feedbackSerializer,new_promptSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny 
import time
from rest_framework.response import Response
from llamaapi import LlamaAPI
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView

from django.http import StreamingHttpResponse
import json
import os



# Create your views here.

class feedbackViewSet(viewsets.ModelViewSet):
    queryset = feedback.objects.all()
    serializer_class = feedbackSerializer
    permission_classes = [IsAuthenticated]

class new_promptViewSet(viewsets.ModelViewSet):
    queryset = new_prompt.objects.all()
    serializer_class = new_promptSerializer
    permission_classes = [IsAuthenticated]



# Create your views here.
LlamaApiKey = 'LL-GDqMzqyWPz9yyGfN7XfxxmADgZVQSeFzJZpXefKtAZnTPorX0a876K47qQ0dRxxC'



class LlamaAPIView(APIView):
    permission_classes = [AllowAny]

    def stream_response_data(self, response_data):
        yield json.dumps(response_data).encode()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                model = data.get('model')
                temperature = data.get('temperature')
                prompt_input = data.get('prompt_input')

                llama = LlamaAPI(LlamaApiKey)
                start_time = time.time()  # Measure start time

                response = llama.run({
                    "model": model,
                    "messages": [{"role": "system", "content": prompt_input}],
                    "temperature": temperature
                })

                end_time = time.time()
                execution_time = end_time - start_time

                content = response.json()["choices"][0]["message"]["content"].strip()
                usage = response.json()["usage"]["prompt_tokens"]
                usage1 = response.json()["usage"]["completion_tokens"]
                usage2 = response.json()["usage"]["total_tokens"]

                response_data = {
                    "Output": content,
                    "usage": {
                        "prompt_tokens": usage,
                        "completion_tokens": usage1,
                        "total_tokens": usage2
                    },
                    "time_taken": execution_time  # Include time taken in response
                }

                # Stream the response data
                response = StreamingHttpResponse(self.stream_response_data(response_data), content_type='text/event-stream')
                response['Cache-Control'] = 'no-cache'
                return response

            except Exception as e:
                error_message = str(e)
                return Response({"error": error_message}, status=400)