from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


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
