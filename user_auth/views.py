from django.views import View
from django.http import JsonResponse
from signup.models import Signup
import json

class User_auth (View):
    def post (self, request):
        data = json.loads(request.body)
        try:
            answer = Signup.objects.filter(user_csrf=data["user_csrf"])[0]
            answerdic = {}
            answerdic["user_id"] = answer.user_id
            answerdic["user_name"] = answer.user_name
            answerdic["user_profile"] = answer.user_profile
            return JsonResponse( {"data": f"{answerdic}", "message": "User Info Loading Success"}, safe=False, status=200)
        except IndexError:
            return JsonResponse({"message": "Need Signup"}, safe=False, status=200)