from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def destination_list(request):
    destinations = Destination.objects.filter(is_deleted=False)
    return render(request, 'destination_list.html', {'destinations': destinations})

@login_required(login_url='signin')
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'destination_detail.html', {'destination': destination})

@login_required(login_url='signin')
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination created successfully.')
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'destination_form.html', {'form': form})

@login_required(login_url='signin')
def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    form = DestinationForm(request.POST or None, request.FILES or None, instance=destination)
    if form.is_valid():
        form.save()
        messages.success(request, 'Destination updated successfully.')
        return redirect('destination_detail', pk=pk)
    return render(request, 'destination_form.html', {'form': form})

@login_required(login_url='signin')
def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.is_deleted = True
        destination.save()
        messages.warning(request, 'Destination deleted successfully.')
        return redirect('destination_list')
    return render(request, 'destination_confirm_delete.html', {'object': destination})

@login_required(login_url='signin')
def destination_history(request):
    deleted_destinations = Destination.objects.filter(is_deleted=True)
    return render(request, 'destination_history.html', {'deleted_destinations': deleted_destinations})

@login_required(login_url='signin')
def destination_restore(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.is_deleted = False
        destination.save()
        messages.success(request, 'Destination restored successfully.')
        return redirect('destination_list')
    return render(request, 'destination_restore_confirm.html', {'object': destination})
