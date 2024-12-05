from django.shortcuts import render, redirect, get_object_or_404
from .models import Loan, LoanCategory, Transaction
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    loans = Loan.objects.filter(user=request.user)
    return render(request, 'loans/dashboard.html', {'loans': loans})

@login_required
def admin_dashboard(request):
    loans = Loan.objects.all()
    categories = LoanCategory.objects.all()
    return render(request, 'loans/admin_dashboard.html', {'loans': loans, 'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        LoanCategory.objects.create(name=name, description=description)
        return redirect('admin_dashboard')
    return render(request, 'loans/add_category.html')
