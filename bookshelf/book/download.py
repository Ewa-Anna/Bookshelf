from io import BytesIO
import pandas as pd
from django.http import HttpResponse

from .models import Book


def download(request, file_type):
    data = Book.objects.all().values(
        "id", "title", "author", "description", "updated", "created"
    )
    df = pd.DataFrame(data)

    if file_type == "csv":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="data.csv"'
        df.to_csv(
            path_or_buf=response, index=False, lineterminator="\n", encoding="utf-8"
        )

    elif file_type == "xlsx":
        df_copy = df.copy()
        for col in df_copy.select_dtypes(include=["datetimetz"]).columns:
            df_copy[col] = df_copy[col].dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")

        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_copy.to_excel(writer, index=False, sheet_name="Sheet1")

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="data.xlsx"'
        response.write(output.getvalue())

    else:
        return HttpResponse("Unsupported file type.", status=400)

    return response
