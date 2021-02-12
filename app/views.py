from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login
from app.forms import ContactForm, UserRegisterForm, NewTaskForm
from app.models import Task, Profile
from django.contrib.auth.decorators import login_required

from app.my_query_models import tasks_finished


def sign_up(request):
    context = {
        'form': UserRegisterForm(),
        'icon_message': 'success',
        'title_message': 'Great'
    }

    if request.method == 'POST':
        data_form = UserRegisterForm(data=request.POST)
        if data_form.is_valid():
            data_form.save()

            # loguear automaticamente con datos del formulario
            user = authenticate(
                username=data_form.cleaned_data['username'],
                password=data_form.cleaned_data['password1']
            )
            login(request, user)

            # redireccionar al home luego de un mensaje
            messages.success(
                request, "you have registered successfully!"
            )
            return redirect(to='home')

        context['form'] = data_form

    return render(request, 'registration/sign_up.html', context)


def home(request):

    return render(request, 'home.html')


@login_required(login_url='/login/')
def task_management(request):
    '''
    Vista donde se vizualizaran los trabajadores que tiene el lider logueado
    '''

    if not request.user.leader:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    work_area = request.user.work_area
    employees = tasks_finished(Task, Profile, work_area)

    context = {
        'form': NewTaskForm(),
        'employees':  employees,
        'work_area': work_area,
        'icon_message': 'success',
        'title_message': 'Great'
    }

    if request.method == 'POST':
        data_form = NewTaskForm(data=request.POST)
        if data_form.is_valid():
            data_form = data_form.save(commit=False)
            data_form.sender = Profile.objects.get(id=request.user.id)
            data_form.save()
            messages.success(
                request, 'Task created successfully.'
            )

            return redirect(to='task_management')
        else:
            messages.success(
                request, 'An error occurred while trying to submit the form.'
            )

            context = {
                'form': data_form,
                'icon_message': 'error',
                'title_message': 'Error'
            }

    return render(request, 'task_management.html', context)


@login_required(login_url='/login/')
def task_completed(request, id):
    finish_task = get_object_or_404(Task, id=id)
    finish_task.done = True
    finish_task.save()
    return redirect(to='task_management')


@login_required(login_url='/login/')
def task_delete(request, id):
    delete_task = get_object_or_404(Task, id=id)
    delete_task.delete()
    return redirect(to='task_management')


@login_required(login_url='/login/')
def my_tasks(request):
    '''
    Vista donde se vizualizaran las tareas pendientes por realizar
    '''
    username = request.user.username

    tasks_pending = Task.objects.filter(
        receiver__username=username, done=False
    )

    context = {
        'tasks_pending': tasks_pending
    }

    return render(request, 'my_tasks.html', context)


def contact(request):
    context = {
        'form': ContactForm()
    }

    if request.method == 'POST':
        data_form = ContactForm(data=request.POST)
        if data_form.is_valid():
            data_form.save()
            messages.success(
                request, 'Contacto guardado exitosamente.'
            )
        else:
            context['form'] = data_form

    return render(request, 'contacto.html', context)
