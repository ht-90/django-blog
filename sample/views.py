from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, FileResponse, JsonResponse

import csv
import io
from reportlab.pdfgen import canvas

body = """
<ol>
  <li>list item 1</li>
  <li>list item 2</li>
  <li>list item 3</li>
</ol>
"""

class Index(View):
    def get(self, request):  # http method
        return HttpResponse(body)

header = ["ID", "Name", "Age"]

people = [
    ("1", "A", 10),
    ("2", "B", 20),
    ("3", "C", 30),
]


class CSVView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=mycsv.csv"
  
        writer = csv.writer(response)
        writer.writerow(header)
        writer.writerows(people)
        return response


class PDFView(View):
    def get(self, request):
        buffer = io.BytesIO()
        # Create a canvas
        p = canvas.Canvas(buffer)
        # Write string in pdf cancas
        p.drawString(50, 800, "Hello PDF!")
        
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    

class PeopleAPIView(View):
    def get(self, request):
        people_ret = []
        for p in people:
            people_ret.append({
                "id": p[0],
                "name": p[1],
                "age": p[2],
            })
        data = {
            "people": people_ret,
        }
        return JsonResponse(data=data)
