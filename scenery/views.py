from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.


def main_view(request):
    period = int(request.GET.get('period', '60'))
    m_int = period
    m_delta = timedelta(minutes=period)
    now = datetime.now()
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
