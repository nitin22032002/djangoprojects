from django.http import HttpResponse
def firstResponse(request,nums=1,name="nitin"):
    print(nums,name)
    if(nums%2==0 and name=="nitin"):
        return HttpResponse("<h1>You are authenticated</h1>")
    else:
        return HttpResponse("<h1>Your Test is Over</h1>")