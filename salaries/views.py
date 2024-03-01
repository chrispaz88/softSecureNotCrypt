from django.shortcuts import render, redirect
from .forms import SalaryForm
from .models import Salary



# Create your views here.
def index(request):

    salaries = Salary.objects.all().values('id', 'name', 'area', 'value')
    return render(request, 'index.html',
                  {'salaries': salaries})

def add_salary(request):

    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            # Extrae la información del formulario
            name = form.cleaned_data['name']
            area = form.cleaned_data['area']
            value = form.cleaned_data['value']


            Salary.objects.create(name=name, area=area, value=value )

            return redirect('index')  # Redirige a la misma página
    else:
        form = SalaryForm()
    return render(request, 'add_salary.html', {'form': form})


def edit_salary(request, salary_id):
    salary = Salary.objects.get(id=salary_id)
    # Inicializa el formulario con los datos del salario
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            # Extrae la información del formulario
            name = form.cleaned_data['name']
            area = form.cleaned_data['area']
            value = form.cleaned_data['value']


            salary.name = name
            salary.area = area
            salary.value = value
            salary.save()
            return redirect('index')
    else:

        initial_data = {
            'id': salary.id,
            'name': salary.name,
            'area': salary.area,
            'value': salary.value
        }
        form = SalaryForm(initial=initial_data)
    return render(request, 'edit_salary.html', {'form': form, 'salary_id': salary_id})


def delete_salary(request, salary_id):
    salary_data = Salary.objects.get(id=salary_id)

    if request.method == 'POST':
        # Elimina el salario de la base de datos
        salary_data.delete()

        return redirect('index')

    return render(request, 'delete_confirm.html', {
        'salary_id': salary_id,
        'salary_data': salary_data
    })


def sum_salaries(request):
    # Obtiene todos los salarios
    salaries = Salary.objects.all()

    # Inicializa el total de salarios por área
    total_salaries_by_area = {}

    # Suma los salarios por área
    for salary in salaries:
        if salary.area in total_salaries_by_area:
            total_salaries_by_area[salary.area] += salary.value
        else:
            total_salaries_by_area[salary.area] = salary.value

    return render(request, 'total_salaries.html', {
        'total_salaries_by_area': total_salaries_by_area
    })


