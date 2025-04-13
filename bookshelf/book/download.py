import pandas as pd
from django.http import HttpResponse

from .models import Book


def download(request, file_type):
    data = Book.objects.all().values('id', 'title', 'author', 'description', 'updated', 'created')
    df = pd.DataFrame(data)

    if file_type == "csv":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="data.csv"'
        df.to_csv(path_or_buf=response, index=False, lineterminator='\n',encoding='utf-8')

    else:
        return HttpResponse("Unsupported file type.", status=400)

    return response
