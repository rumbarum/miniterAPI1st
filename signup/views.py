from django.views import View
from .models import Signup
from django.http import JsonResponse
import json 

class Signupview(View):

    #로그인 정보 확인시
    def get(self, request):
        data = list(Signup.objects.values())
        return JsonResponse(data, safe=False, status=200)

    #사인업시

    def post(self, request):
        data = json.loads(request.body)
        try:
            Signup.objects.filter(user_id=data["user_id"])[0]
            return JsonResponse({"message": "Id is Already Exist"}, safe=False, status=200)
        except IndexError:
            sign = Signup(user_id=data["user_id"], user_name=data["user_name"], user_password=data["user_password"],
                          user_profile=data["user_profile"], user_csrf=data["user_csrf"])
            sign.save()
            return JsonResponse({"message": "Sign Up Success"}, safe=False, status=200)

