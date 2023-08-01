from django.shortcuts import render

# Create your views here.
def loopstatements(request):
    d={"name":"ramcharan","age":35,"movies":["rrr","dhruva","rangasthalam","chirutha","magadheera"],"hobbies":["acting","dancing","football"]}
    return render(request,"loopstatements.html",context=d)

def pk(request):
    d={"name":"pawankalyan","age":50,"movies":["badri","gabbarsingh","sardargabbarsingh","bro","tholiprema","kushi"],"hobbies":["acting","powerful dancing"]}
    return render(request,"pk.html",context=d)
