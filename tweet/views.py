from django.views import View
from django.http import JsonResponse
from tweet.models import Tweet
import json 


class Tweetview(View): 

    def get(self, request):
        data = list(Tweet.objects.values())
        return JsonResponse({"data": f"{data}", "message": "Tweet Loading Success"}, safe=False, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            tweet = Tweet(user_id=data["user_id"], user_content=data["user_content"])
            tweet.save()
            getpk = Tweet.objects.filter(user_id=data["user_id"]).last().pk
            return JsonResponse({"content_id": f"{getpk}", "message": "Tweet Success"}, safe=False, status=200)
        except KeyError:
            return JsonResponse({"message": "Tweet Failed"}, safe=False, status=200)



