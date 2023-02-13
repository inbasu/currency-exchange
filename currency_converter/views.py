from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CurrencyForm
from .request import convert


# Create your views here.
class CurencyView(TemplateView):
    def get(self, request):
        template_name = "index.html"
        context = {"form": CurrencyForm}
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        """Post come from JS and return to JS in this url"""
        form = CurrencyForm(request.POST or None)
        context = {"result": ""}
        if form.is_valid:
            value = request.POST["value"]
            fromCur = request.POST["fromCur"]
            toCur = request.POST["toCur"]
            result = convert(value, fromCur, toCur)
            context["result"] = round(result, 2)
        return JsonResponse(context)
