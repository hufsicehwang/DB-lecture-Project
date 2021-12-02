from django.shortcuts import render
def review(request):
    if request.method =="GET":
        return render(request,'review.html')