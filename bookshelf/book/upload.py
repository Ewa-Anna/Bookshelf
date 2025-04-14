import pandas as pd

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Book

def upload(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        mode = request.POST.get("mode")

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)

        try:
            if filename.endswith(".csv"):
                data = pd.read_csv(file_path)
            elif filename.endswith(".xlsx"):
                data = pd.read_excel(file_path)
            else:
                return render(request, "book/upload.html", {"error": "Unsupported file format."})

            required_columns = {"title", "author", "description"}
            if not required_columns.issubset(data.columns):
                return render(request, "book/upload.html", {"error": "Missing required columns."})

            if mode == "overwrite":
                Book.objects.all().delete()

            for _, row in data.iterrows():
                Book.objects.create(
                    title=row["title"],
                    author=row["author"],
                    description=row["description"],
                )

            return redirect("book:book_list")

        except Exception as e:
            return render(request, "book/upload.html", {"error": f"Upload failed: {str(e)}"})

    return render(request, "book/upload.html")
