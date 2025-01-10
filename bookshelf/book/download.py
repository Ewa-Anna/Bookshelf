import pandas as pd
from django.http import HttpResponse

from .models import Book


def download(request, file_type):
    data = Book.objects.all().values()
    df = pd.DataFrame(data)

    if file_type == "csv":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="data.csv"'
        df.to_csv(path_or_buf=response, index=False)
    elif file_type == "xlsx":
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="data.xlsx"'
        df.to_excel(response, index=False)

    return response
