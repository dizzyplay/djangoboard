from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.


def main_view(request):
    one_minute = timedelta(minutes=1)
    now = datetime.now()
    testlist = []

    for i in range(9):
        now -= one_minute
        testlist.append(now.strftime("%Y-%m-%d_%H%M"))

    return render(request, './scenery/main.html', {
        'test': testlist,
    })
