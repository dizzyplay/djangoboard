from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.


def main_view(request):
    period = int(request.GET.get('period', '10'))
    request_time = request.GET.get('time',None)
    if request_time is not None:
        request_time = str(request_time)
        year = int(request_time[:4])
        month = int(request_time[4:6])
        days = int(request_time[6:8])
        hour = int(request_time[8:10])
        minute = int(request_time[10:12])
        print("{}년 {}월 {}일 {}시 {}분".format(year, month, days, hour, minute))
        now = datetime(year, month, days, hour, minute)
    else:
        now = datetime.now()

    m_int = period
    m_delta = timedelta(minutes=period)
    testlist = []
    if now.minute % m_int == 0:
        for i in range(10):
            testlist.append(now.strftime("%Y-%m-%d_%H%M"))
            now -= m_delta
    else:
        get_lid_value = now.minute % m_int
        get_lid_value_delta = timedelta(minutes=get_lid_value)
        now -= get_lid_value_delta
        for i in range(10):
            testlist.append(now.strftime("%Y-%m-%d_%H%M"))
            now -= m_delta

    return render(request, './scenery/main.html', {
        'test': testlist,
    })
