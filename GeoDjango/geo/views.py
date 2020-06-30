from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data

class IndexView(View):
	def get(self, request, *args, **kwargs):
		items = []
		city = None
		while not city:
			ret = get_client_data()
			if ret:
				city = ret['city']

		query_term = request.GET.get('key',None)
		local = request.GET.get('location',None)
		location = city
		context = {
			'city':city,
			'busca': False
		}

		if local:
			location = local
		if query_term:
			items = yelp_search(keyword=query_term, location=location)
			context = {
				'items':items,
				'city':location,
				'busca':True
			}
		return render(request,'index.html', context)