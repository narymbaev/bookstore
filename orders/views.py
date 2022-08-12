from locale import currency
from pydoc import describe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Permission
from django.conf import settings
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        permission = Permission.objects.get(codename='special_status')
        user = request.user
        user.user_permissions.add(permission)
        charge = stripe.Charge.create(
            amount=4500,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')
