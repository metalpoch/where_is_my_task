from django.utils import timezone


def proccess_list_of_employees(Profile, work_area):
    # query from models based in task complete and not complete
    if work_area:
        list_of_employees = Profile.objects.filter(
            work_area=work_area, leader=False
        )

    else:
        list_of_employees = Profile.objects.filter(leader=False)

    return list_of_employees


def time_working(admission_date=None):
    time = (timezone.now() - admission_date).days
    if time > 1:
        return f'Employed for {time} days!'
    if time == 1:
        return f'Employed for {time} day.'
    else:
        return 'Employed from today.'


def tasks_finished(Task, Profile, work_area=None):
    '''
    Función que genera dos diccionarios con el nombre de usuario como llave
    y las tareas completas (o no completas) como valor
    '''

    list_of_employees = proccess_list_of_employees(Profile, work_area)

    data_task_by_employee = Task.objects.filter(
        receiver__work_area=work_area
    )

    tasks_complete = Task.objects.filter(
        receiver__work_area=work_area, done=True
    )

    tasks_not_complete = Task.objects.filter(
        receiver__work_area=work_area, done=False
    )

    # temp dict
    employee_time_working = {}
    work_area_by_employee = {}
    tasks_not_complete_by_employee = {}
    tasks_complete_by_employee = {}
    programming_area_by_employee = {}
    fullname_by_employee = {}
    data_task_by_employee = {}

    for e in list_of_employees:

        username = e.username
        work_area = e.work_area
        programming_area = e.programming_area
        fullname = f'{e.first_name} {e.last_name}'
        admission_date = e.admission_date

        fullname_by_employee[username] = fullname
        tasks_complete_by_employee[username] = 0
        tasks_not_complete_by_employee[username] = 0
        work_area_by_employee[username] = work_area
        programming_area_by_employee[username] = programming_area
        employee_time_working[username] = time_working(admission_date)

    # sum tasks_complete in list
    for e in tasks_complete:  # get finish task, fullname and work_data
        username = e.receiver.username
        if username in tasks_complete_by_employee.keys():
            tasks_complete_by_employee[username] += 1

    # sum task_no_complete in list
    for e in tasks_not_complete:
        username = e.receiver.username
        if username in tasks_not_complete_by_employee.keys():
            tasks_not_complete_by_employee[username] += 1

        try:
            data_task_by_employee[username].items()

        except KeyError:
            data_task_by_employee[username] = {}

        finally:
            data_task_by_employee[username][e.id] = {
                'subject': e.subject,
                'message': e.message,
                'limit_date': e.limit_date
            }

    # Create dict with dict from data query
    data_employees = {
        'fullname': fullname_by_employee,
        'work_area': work_area_by_employee,
        'time_working': employee_time_working,
        'programming_area': programming_area_by_employee,
        'tasks_complete': tasks_complete_by_employee,
        'tasks_not_complete': tasks_not_complete_by_employee,
        'data_task': data_task_by_employee
    }

    # tomar list_dict_employee_data generar diccionario con todos los datos
    employees = {}
    for data_type, data_employee in data_employees.items():
        for username, content in data_employee.items():

            # if any dict field is empty (error), create it empty
            try:
                employees[username].items()

            except KeyError:
                employees[username] = {}

            finally:
                employees[username][data_type] = content

    return employees
