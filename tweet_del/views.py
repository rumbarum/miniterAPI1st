from django.views import View
from django.http import JsonResponse
from tweet.models import Tweet
import json

class Tweet_del (View) :

    def post (self, request) :
        data = json.loads(request.body)

        transferedData2 = data["content_id"]
        try:
            tweet = Tweet.objects.get(id=transferedData2)
            if tweet.user_id == data["user_id"]:
                tweet.delete()
                return JsonResponse({"message": "Delete Success"}, safe=False, status=200)
            else:
                return JsonResponse({"message": "Error"}, safe=False, status=200)
        except:
            return JsonResponse({"message": "No Authorization"}, safe=False, status=200)
