from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

# Create your views here.

from .models import MainCategory, BasicStats, BasicFood, AllFood
import pandas as pd

from .calculations import DRICalculations

import random

def home(request):

    return render(request, 'home.html')


def dri_result(request):
    
    user_data = request.session.get('user_data')

    if user_data and len(user_data) > 0:

        sex, age, pregnancy, height, weight, activity = user_data

        if pregnancy == "not-pregnant-lactating":
            pregnancy = None
        

    else:
        sex="male"
        age=20
        pregnancy=None
        height=180
        weight=70
        activity="active"




    
    calculator = DRICalculations(sex, float(age), pregnancy, int(height), int(weight), activity)

    main_info, result, vitamins, minerals = calculator.return_results()

    sex = sex.capitalize

    if activity == "sedentary":
        activity = "Sedentary"
    elif activity == "low-active":
        activity = "Low Active"
    elif activity == "active":
        activity = "Active"
    elif activity == "very-active":
        activity = "Very Active"


    context = {"sex":sex, "age":age, "pregnancy":pregnancy, "height":height, "weight":weight, "activity":activity, "main_info":main_info, "result": result, "vitamins": vitamins, "minerals": minerals}

    return render(request, 'dri_result.html', context=context)




def calculate(request):

    if request.method == "POST":
        sex = request.POST.get('sex', None)
        age = request.POST.get('age', None)
        pregnancy = request.POST.get('pregnancy', None)
        height = request.POST.get('height', None)
        weight = request.POST.get('weight', None)
        activity = request.POST.get('activity', None)
        user_data = [sex, age, pregnancy, height, weight, activity]
        print(sex, age, pregnancy, height, weight, activity)

        request.session['user_data'] = user_data

        return redirect('dri_result')

    
    return render(request, 'calculate.html')

def article(request):

    return render(request, 'article.html')


def category(request):
    data = [10, 23, 26, 12, 3, 9]
    labels = ['tim', 'tam', 'tom', 'jim', 'kim', 'rim']

    context = {'data':data, 'labels':labels}

    return render(request, 'category.html', context=context)


def allFood(request):

    # table_names = ['name', 'serving_size', 'calories','total_fat',
    #     'saturated_fat',
    #     'cholesterol',
    #     'sodium',
    #     'choline',
    #     'folate',
    #     'folic_acid',
    #     'niacin',
    #     'pantothenic_acid',
    #     'riboflavin',
    #     'thiamin',
    #     'vitamin_a',
    #     'vitamin_a_rae',
    #     'carotene_alpha',
    #     'carotene_beta',
    #     'cryptoxanthin_beta',
    #     'lutein_zeaxanthin',
    #     'lucopene',
    #     'vitamin_b12',
    #     'vitamin_b6',
    #     'vitamin_c',
    #     'vitamin_d',
    #     'vitamin_e',
    #     'tocopherol_alpha',
    #     'vitamin_k',
    #     'calcium',
    #     'copper',
    #     'irom',
    #     'magnesium',
    #     'manganese',
    #     'phosphorous',
    #     'potassium',
    #     'selenium',
    #     'zink',
    #     'protein',
    #     'alanine',
    #     'arginine',
    #     'aspartic_acid',
    #     'cystine',
    #     'glutamic_acid',
    #     'glycine',
    #     'histidine',
    #     'hydroxyproline',
    #     'isoleucine',
    #     'leucine',
    #     'lysine',
    #     'methionine',
    #     'phenylalanine',
    #     'proline',
    #     'serine',
    #     'threonine',
    #     'tryptophan',
    #     'tyrosine',
    #     'valine',
    #     'carbohydrate',
    #     'fiber',
    #     'sugars',
    #     'fructose',
    #     'galactose',
    #     'glucose',
    #     'lactose',
    #     'maltose',
    #     'sucrose',
    #     'fat',
    #     'saturated_fatty_acids',
    #     'monounsaturated_fatty_acids',
    #     'polyunsaturated_fatty_acids',
    #     'fatty_acids_total_trans',
    #     'alcohol',
    #     'ash',
    #     'caffeine',
    #     'theobromine',
    #     'water']

    # foods = AllFood.objects.all()

    # result = []
    # for item in foods:
    #     temp = []
        
    #     temp.append(item.name)
    #     temp.append(item.serving_size)
    #     temp.append(item.calories)
    #     temp.append(item.total_fat)
    #     temp.append(item.saturated_fat)
    #     temp.append(item.cholesterol)
    #     temp.append(item.sodium)
    #     temp.append(item.choline)
    #     temp.append(item.folate)
    #     temp.append(item.folic_acid)
    #     temp.append(item.niacin)
    #     temp.append(item.pantothenic_acid)
    #     temp.append(item.riboflavin)
    #     temp.append(item.thiamin)
    #     temp.append(item.vitamin_a)
    #     temp.append(item.vitamin_a_rae)
    #     temp.append(item.carotene_alpha)
    #     temp.append(item.carotene_beta)
    #     temp.append(item.cryptoxanthin_beta)
    #     temp.append(item.lutein_zeaxanthin)
    #     temp.append(item.lucopene)
    #     temp.append(item.vitamin_b12)
    #     temp.append(item.vitamin_b6)
    #     temp.append(item.vitamin_c)
    #     temp.append(item.vitamin_d)
    #     temp.append(item.vitamin_e)
    #     temp.append(item.tocopherol_alpha)
    #     temp.append(item.vitamin_k)
    #     temp.append(item.calcium)
    #     temp.append(item.copper)
    #     temp.append(item.irom)
    #     temp.append(item.magnesium)
    #     temp.append(item.manganese)
    #     temp.append(item.phosphorous)
    #     temp.append(item.potassium)
    #     temp.append(item.selenium)
    #     temp.append(item.zink)
    #     temp.append(item.protein)
    #     temp.append(item.alanine)
    #     temp.append(item.arginine)
    #     temp.append(item.aspartic_acid)
    #     temp.append(item.cystine)
    #     temp.append(item.glutamic_acid)
    #     temp.append(item.glycine)
    #     temp.append(item.histidine)
    #     temp.append(item.hydroxyproline)
    #     temp.append(item.isoleucine)
    #     temp.append(item.leucine)
    #     temp.append(item.lysine)
    #     temp.append(item.methionine)
    #     temp.append(item.phenylalanine)
    #     temp.append(item.proline)
    #     temp.append(item.serine)
    #     temp.append(item.threonine)
    #     temp.append(item.tryptophan)
    #     temp.append(item.tyrosine)
    #     temp.append(item.valine)
    #     temp.append(item.carbohydrate)
    #     temp.append(item.fiber)
    #     temp.append(item.sugars)
    #     temp.append(item.fructose)
    #     temp.append(item.galactose)
    #     temp.append(item.glucose)
    #     temp.append(item.lactose)
    #     temp.append(item.maltose)
    #     temp.append(item.sucrose)
    #     temp.append(item.fat)
    #     temp.append(item.saturated_fatty_acids)
    #     temp.append(item.monounsaturated_fatty_acids)
    #     temp.append(item.polyunsaturated_fatty_acids)
    #     temp.append(item.fatty_acids_total_trans)
    #     temp.append(item.alcohol)
    #     temp.append(item.ash)
    #     temp.append(item.caffeine)
    #     temp.append(item.theobromine)
    #     temp.append(item.water)

    #     result.append(temp)

    
    # context = {'table_names': table_names, 'data':result}


    return render(request, 'search.html')


def basicFood(request):

    table_names = ['Name', 'Measure', 'Grams', 'Calories', 'Protein', 'Fat', 'Sat.Fat', 'Fiber', 'Carbs', 'Category']

    foods = BasicFood.objects.all()

    result = []
    for item in foods:
        temp = []
        
        temp.append(item.name)
        temp.append(item.measure)
        temp.append(item.grams)
        temp.append(item.calories)
        temp.append(item.protein)
        temp.append(item.fat)
        temp.append(item.sat_fat)
        temp.append(item.fiber)
        temp.append(item.carbs)
        temp.append(item.category.name)

        result.append(temp)

    
    context = {'table_names': table_names, 'data':result}


    return render(request, 'visualization.html', context=context)



def visualization(request):

    table_names = ['Category', 'Grams', 'Calories', 'Protein', 'Fat', 'Sat.Fat', 'Fiber', 'Carbs']

    stats = BasicStats.objects.all()

    result = []
    for item in stats:
        temp = []
        temp.append(item.category.name)
        temp.append(item.grams)
        temp.append(item.calories)
        temp.append(item.protein)
        temp.append(item.fat)
        temp.append(item.sat_fat)
        temp.append(item.fiber)
        temp.append(item.carbs)
        result.append(temp)
    
    context = {'table_names': table_names, 'data':result}


    return render(request, 'visualization.html', context=context)



def search_results(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        game = request.POST.get('game')

        results = AllFood.objects.filter(name__contains=game)[:20]

        if len(results) > 0 and len(game) > 0:
            data = []
            for result in results:
                item = {
                    'pk': result.id,
                    'name': result.name,
                    'serving_size': result.serving_size,
                    'calories': result.calories,
                    'total_fat': result.total_fat,
                }
                data.append(item)
            res = data
        else:
            res = "No results found ..."
        return JsonResponse({'data': res})

    return JsonResponse({})



def data_ingredient(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        game = request.POST.get('game')

        result = AllFood.objects.filter(id=int(game)).values()[0]
        if result:
            res = result
        else:
            res = "No results found ..."

        return JsonResponse({'data': res})

    return JsonResponse({})




