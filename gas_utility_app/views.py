from django.shortcuts import render, redirect
from .models import ServiceRequest, Customer

# Create your views here.
def submit_request(request):
    if request.method == 'POST':
        request_type = request.POST['request_type']
        details = request.POST['details']
        attachment = request.FILES.get('attachment')
        customer = Customer.objects.get(email=request.user.email) # Assuming the user is authenticated

        service_request = ServiceRequest.objects.create(request_type=request_type, details=details, attachment=attachment)
        customer.service_requests.add(service_request)
        return redirect('request_tracking')
    return render(request, 'submit_request.html')
def request_tracking(request):
    customer = Customer.objects.get(email=request.user.email)
    service_requests = customer.service_requests.all()
    return render(request, 'request_tracking.html', {'service_requests': service_requests})
