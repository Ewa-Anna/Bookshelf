import pandas as pd

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Book


def upload(request):
    if request.method == "POST" and request.FILES["file"]:
        file = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)

        try:
            if filename.endswith(".csv"):
                data = pd.read_csv(file_path)
            elif filename.endswith(".xlsx"):
                data = pd.read_excel(file_path)

            for _, row in data.iterrows():
                Book.objects.create(
                    title=row["title"],
                    author=row["author"],
                    description=row["description"],
                )
            return redirect("book_list")
        except Exception as e:
            return render(request, "upload.html", {"error": str(e)})

    return render(request, "upload.html")
