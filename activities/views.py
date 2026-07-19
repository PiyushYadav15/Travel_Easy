from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Activity
from .forms import ActivityForm

@login_required(login_url='signin')
def activity_list(request):
    activities = Activity.objects.filter(is_deleted=False)
    return render(request, 'activity_list.html', {'activities': activities})

@login_required(login_url='signin')
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk, is_deleted=False)
    return render(request, 'activity_detail.html', {'activity': activity})

@login_required(login_url='signin')
def activity_create(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Activity created successfully!')
            return redirect('activity_list')
    else:
        form = ActivityForm()
    return render(request, 'activity_form.html', {'form': form})

@login_required(login_url='signin')
def activity_update(request, pk):
    activity = get_object_or_404(Activity, pk=pk, is_deleted=False)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, '✏️ Activity updated successfully!')
            return redirect('activity_detail', pk=pk)
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activity_form.html', {'form': form})

@login_required(login_url='signin')
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk, is_deleted=False)
    if request.method == 'POST':
        activity.is_deleted = True
        activity.save()
        messages.warning(request, '🗑️ Activity soft deleted.')
        return redirect('activity_list')
    return render(request, 'confirm_delete.html', {'object': activity})

@login_required(login_url='signin')
def activity_history(request):
    deleted_activities = Activity.objects.filter(is_deleted=True)
    return render(request, 'activity_history.html', {'activities': deleted_activities})

@login_required(login_url='signin')
def activity_restore(request, pk):
    activity = get_object_or_404(Activity, pk=pk, is_deleted=True)
    if request.method == 'POST':
        activity.is_deleted = False
        activity.save()
        messages.success(request, '✅ Activity restored successfully!')
        return redirect('activity_list')
    return render(request, 'confirm_restore.html', {'object': activity})


