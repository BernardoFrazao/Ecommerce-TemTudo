
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
	template_name = "search/view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductView, self).get_context_data(*args, **kwargs)
		#query = method_dict.get('q')
		context['query'] = self.request.GET.get('q')
		#SearchQuery.objects.create(query=query)
		return context


	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q', None)
		if query is not None:
			return Product.objects.search(query)
		return Product.objects.featured()#vai para os produtos featured quando não existe resultado da pesquisa


		#distinct para nao mostrar dois produtos iguais
		#__icontains = o campo contém isto
		#__iexact = o campo contém exatamente isto
		#não sensivel a maiusculas