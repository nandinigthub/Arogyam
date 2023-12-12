from django.shortcuts import render
from django.http import HttpResponse
from symptomdata.models import Symptom
from django.http import HttpResponse
from .sl import DecisionTree
from symptomdata.models import d_dis
import datetime as dt
from disease.new import symptoms as disease_symptoms , predict_disease


from django.template import loader

def new(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def form(request):
    symptoms = disease_symptoms
    return render(request, 'form.html', {'symptoms': symptoms})

def result(request):
    if request.method == 'POST':
        
        symptom1 = request.POST.get('symptom1')
        symptom2 = request.POST.get('symptom2')
        symptom3 = request.POST.get('symptom3')
        symptom4 = request.POST.get('symptom4')
        symptom5 = request.POST.get('symptom5')

    sy_list = [symptom1,symptom2,symptom3,symptom4,symptom5]
    predicted_disease = predict_disease(sy_list)
    
    return  render(request, 'result.html',{'result':predicted_disease})


def bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi = round(weight / (height * height), 2)
        return render(request, 'bmi.html', {'bmi': bmi})
    else:
        return render(request,'bmi.html')  


def period_calculator(request):
     
    if request.method == 'POST':
        cycle_length = int(request.POST.get('cycle_length'))

        # Calculate estimated period start date
        period_start_date = (dt.date.today() + dt.timedelta(days=cycle_length)).strftime("%B %d, %Y")

        # Calculate most probable ovulation days
        ovulation_day_1 = (dt.date.today() + dt.timedelta(days=(cycle_length - 14))).strftime("%B %d, %Y")
        ovulation_day_2 = (dt.date.today() + dt.timedelta(days=(cycle_length - 15))).strftime("%B %d, %Y")

        # Pass results to template
        return render(request, 'period_calculator.html', {'period_start_date': period_start_date, 'ovulation_day_1': ovulation_day_1, 'ovulation_day_2': ovulation_day_2})

    # If request method is GET, render the form
    else:
        return render(request, 'period_calculator.html')






 


def cal_calculate(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])*2.205
        height = float(request.POST['height'])*0.3937
        age = int(request.POST['age'])
        gender = request.POST['gender']
        activity_level = int(request.POST['activity_level'])

        if gender == "M":
            bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
        else:
            bmr = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

        if activity_level == 1:
            multiplier = 1.2
        elif activity_level == 2:
            multiplier = 1.375
        elif activity_level == 3:
            multiplier = 1.55
        elif activity_level == 4:
            multiplier = 1.725
        else:
            multiplier = 1.9

        tdee = bmr * multiplier
        return render(request, 'calory.html', {'tdee': int(tdee)})

    else:
        return render(request, 'calory.html')


def widal(request):
    if request.method == 'POST':
        # Get input values from form data
        o_antigen_titer = float(request.POST.get('o_antigen_titer'))
        h_antigen_titer = float(request.POST.get('h_antigen_titer'))

        # Define reference ranges for Widal test
        O_antigen_range = [80, float('inf')]
        H_antigen_range = [160, float('inf')]

        # Check if input values are within reference ranges
        if o_antigen_titer >= O_antigen_range[0] and o_antigen_titer <= O_antigen_range[1] and h_antigen_titer >= H_antigen_range[0] and h_antigen_titer <= H_antigen_range[1]:
            result = "Your Widal test report is in the normal range."
        else:
            result = "Your Widal test report is outside the normal range. Please consult a healthcare professional for further evaluation."

        # Render the result in the template
        return render(request, 'widal_test_report_reader.html', {'result': result})

    # Render the form initially
    return render(request, 'widal_test_report_reader.html')        

def sugar(request):
    if request.method == 'POST':
        fasting = request.POST['fasting']
        pp = request.POST['pp']
        
        # Check if input values are within reference ranges
        fasting_min = 70
        fasting_max = 100
        pp_min = 70
        pp_max = 140
        
        if float(fasting) >= fasting_min and float(fasting) <= fasting_max and float(pp) >= pp_min and float(pp) <= pp_max:
            interpretation = "Your sugar test report is in good condition."
        else:
            interpretation = "Your sugar test report is in bad condition. Please consult a healthcare professional for further evaluation."
        
        return render(request, 'sugar_report.html', {'result': interpretation})
    
    return render(request, 'sugar_report.html')

def pregnancy_cal(request):
    if request.method == 'POST':
        last_period_date_str = request.POST['last_period_date']
        last_period_date = dt.datetime.strptime(last_period_date_str, '%Y-%m-%d').date()
        
        due_date = last_period_date + dt.timedelta(days=280)
        return render(request, 'pregnancy_calculator.html', {'due_date': due_date})
    return render(request, 'pregnancy_calculator.html')


def anxiety_screening(request):
    if request.method == 'POST':
        # Get the answers to the questions
        q1 = int(request.POST.get('q1', '0'))
        q2 = int(request.POST.get('q2', '0'))
        q3 = int(request.POST.get('q3', '0'))
        q4 = int(request.POST.get('q4', '0'))
        q5 = int(request.POST.get('q5', '0'))

        # Calculate the total score
        total_score = q1 + q2 + q3 + q4 + q5

        # Determine the level of anxiety based on the total score
        if total_score <= 5:
            anxiety_level = "Minimal anxiety"
        elif total_score <= 10:
            anxiety_level = "Mild anxiety"
        elif total_score <= 15:
            anxiety_level = "Moderate anxiety"
        elif total_score <= 20:
            anxiety_level = "Severe anxiety"
        else:
            anxiety_level = "Extreme anxiety"

        return render(request, 'anxiety_result.html', {'total_score': total_score, 'anxiety_level': anxiety_level})

    return render(request, 'anxiety_result.html')


def medical(request):
    return render(request,'medical_form.html')