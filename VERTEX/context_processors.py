
from datetime import date

today_date = date.today()

def data(request):
    context = {
        'today':today_date,
    }
    return(context)