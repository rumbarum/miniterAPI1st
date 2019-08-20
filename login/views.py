from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse
from signup.models import Signup
import json

class Loginview(View):

    # def get(self, request):
    #     data = Login.objects.last().iddd
    #     return JsonResponse({"Result":data}, safe=False, status=200)

    def post(self, request):
        data = json.loads(request.body)
        try:
            answer = Signup.objects.filter(user_id=data["user_id"])[0]
            if data["user_password"] == answer.user_password:
                return JsonResponse({"message": "Login Success"}, safe=False, status=200)
            else:
                return JsonResponse({"message": "Wrong Password"}, safe=False, status=200)
        except IndexError:
            return JsonResponse({"message": "Check Id"}, safe=False, status=200)