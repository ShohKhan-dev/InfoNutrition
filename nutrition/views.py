from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import MainCategory, BasicStats, BasicFood, AllFood, UseInfo, UserRDA, UserLog, UserLogFood, UserSDA
import pytz
from datetime import datetime, timezone
from .calculations import DRICalculations
from django.db.models import F
import random

def home(request):

    return render(request, 'home.html')


def set_user_rda(request, main_info, result, vitamins, minerals, amino_acids):

    calories = main_info["caloric_needs"] 
    water = main_info["total_water"] 
    carbohydrate = result["carbohydrate"] * 1000
    total_fiber = result["total_fiber"] * 1000
    protein = result["protein"] * 1000
    fat = result["fat"] * 1000
    sat_fat = result["sat_fat"] * 1000
    trans_fat = result["trans_fat"] * 1000
    dietary_cholesterol = result["dietary_cholesterol"] 
    sugar = result["sugar"] * 1000
 
    # Vitamins
    vitamin_a = vitamins["vitamin_a"]["rda"] / 1000
    vitamin_b_6 = vitamins["vitamin_b_6"]["rda"] 
    vitamin_b_12 = vitamins["vitamin_b_12"]["rda"] / 1000
    vitamin_c = vitamins["vitamin_c"]["rda"]
    vitamin_d = vitamins["vitamin_d"]["rda"] / 1000
    vitamin_e = vitamins["vitamin_e"]["rda"]
    vitamin_k = vitamins["vitamin_k"]["rda"] / 1000
    thiamin = vitamins["thiamin"]["rda"]
    riboflavin = vitamins["riboflavin"]["rda"]
    folate = vitamins["folate"]["rda"] / 1000 
    niacin = vitamins["niacin"]["rda"] 
    choline = vitamins["choline"]["rda"]
    pantothenic_acid = vitamins["pantothenic_acid"]["rda"] 
    carotenoids = vitamins["carotenoids"]["rda"] / 1000

    # Minerals
    calcium = minerals["calcium"]["rda"]
    copper = minerals["copper"]["rda"] / 1000
    iron = minerals["iron"]["rda"] 
    magnesium = minerals["magnesium"]["rda"] 
    manganese = minerals["manganese"]["rda"] 
    phosphorus = minerals["phosphorus"]["rda"] 
    potassium = minerals["potassium"]["rda"] * 1000
    selenium = minerals["selenium"]["rda"] / 1000
    sodium = minerals["sodium"]["rda"] * 1000
    zinc = minerals["zinc"]["rda"] 

    # Amino Acids
    histidine = amino_acids["histidine"]
    isoleucine = amino_acids["isoleucine"]
    leucine = amino_acids["leucine"] 
    lysine = amino_acids["lysine"] 
    methionine = amino_acids["methionine"] 
    cysteine = amino_acids["cysteine"] 
    phenylalanine = amino_acids["phenylalanine"] 
    tyrosine = amino_acids["tyrosine"] 
    threonine = amino_acids["threonine"] 
    tryptophan = amino_acids["tryptophan"] 
    valine = amino_acids["valine"] 

    if request.user.is_authenticated:
        # timezone = UseInfo.objects.get(created_by=request.user).timezone

        # if timezone:
        #     tz = pytz.timezone(timezone)
        #     current_time = datetime.now(tz).date()
        # else:
        #     current_time = datetime.now(timezone.utc).date()

        if UserRDA.objects.filter(created_by=request.user).exists():
            
            UserRDA.objects.filter(created_by=request.user).update(calories=calories, water=water, carbohydrate=carbohydrate, 
                    total_fiber=total_fiber, protein=protein, fat=fat, sat_fat=sat_fat, trans_fat=trans_fat, dietary_cholesterol=dietary_cholesterol,
                    sugar=sugar, vitamin_a=vitamin_a, vitamin_b_6=vitamin_b_6, vitamin_b_12=vitamin_b_12, vitamin_c=vitamin_c,
                    vitamin_d=vitamin_d, vitamin_e=vitamin_e, vitamin_k=vitamin_k, thiamin=thiamin, riboflavin=riboflavin,
                    folate=folate, niacin=niacin, choline=choline, pantothenic_acid=pantothenic_acid,
                    carotenoids=carotenoids, calcium=calcium, copper=copper, iron=iron, magnesium=magnesium,
                    manganese=manganese, phosphorus=phosphorus, potassium=potassium, selenium=selenium, sodium=sodium, zinc=zinc,
                    histidine=histidine, isoleucine=isoleucine, leucine=leucine, lysine=lysine, methionine=methionine, cysteine=cysteine,
                    phenylalanine=phenylalanine, tyrosine=tyrosine, threonine=threonine, tryptophan=tryptophan, valine=valine)
            
        else:
            UserRDA.objects.create(created_by=request.user, calories=calories, water=water, carbohydrate=carbohydrate, 
                    total_fiber=total_fiber, protein=protein, fat=fat, sat_fat=sat_fat, trans_fat=trans_fat, dietary_cholesterol=dietary_cholesterol,
                    sugar=sugar, vitamin_a=vitamin_a, vitamin_b_6=vitamin_b_6, vitamin_b_12=vitamin_b_12, vitamin_c=vitamin_c,
                    vitamin_d=vitamin_d, vitamin_e=vitamin_e, vitamin_k=vitamin_k, thiamin=thiamin, riboflavin=riboflavin,
                    folate=folate, niacin=niacin, choline=choline, pantothenic_acid=pantothenic_acid,
                    carotenoids=carotenoids, calcium=calcium, copper=copper, iron=iron, magnesium=magnesium,
                    manganese=manganese, phosphorus=phosphorus, potassium=potassium, selenium=selenium, sodium=sodium, zinc=zinc,
                    histidine=histidine, isoleucine=isoleucine, leucine=leucine, lysine=lysine, methionine=methionine, cysteine=cysteine,
                    phenylalanine=phenylalanine, tyrosine=tyrosine, threonine=threonine, tryptophan=tryptophan, valine=valine)


def error_404_view(request, exception):
    return render(request,'404.html')


def dri_result(request):
    
    user_data = request.session.get('user_data')

    if user_data and len(user_data) > 0:

        sex, age, pregnancy, height, weight, activity = user_data
        

    else:
        return redirect('calculate')

    
    calculator = DRICalculations(sex, float(age), pregnancy, float(height), float(weight), activity)

    main_info, result, vitamins, minerals, amino_acids = calculator.return_results()

    set_user_rda(request, main_info, result, vitamins, minerals, amino_acids)


    sex = sex.capitalize

    if activity == "sedentary":
        activity = "Sedentary"
    elif activity == "low-active":
        activity = "Low Active"
    elif activity == "active":
        activity = "Active"
    elif activity == "very-active":
        activity = "Very Active"


    context = {"sex":sex, "age":age, "pregnancy":pregnancy, "height":height, "weight":weight, "activity":activity, "main_info":main_info, "result": result, "vitamins": vitamins, "minerals": minerals, "amino_acids": amino_acids}

    return render(request, 'dri_result.html', context=context)




def calculate(request):

    timezones = [timeZone for timeZone in pytz.common_timezones]

    context = {'timezones': timezones}


    if request.method == "POST":
        sex = request.POST.get('sex', None)
        age = request.POST.get('age', None)
        pregnancy = request.POST.get('pregnancy', None)
        height = request.POST.get('height', None)
        weight = request.POST.get('weight', None)
        activity = request.POST.get('activity', None)
        timezone = request.POST.get('timezone', None)
        

        if pregnancy == "not-pregnant-lactating":
            pregnancy = None
        
        user_data = [sex, age, pregnancy, height, weight, activity]

        # print(sex, age, pregnancy, height, weight, activity, timezone)
        
        if request.user.is_authenticated:
            if UseInfo.objects.filter(created_by=request.user).exists():
                UseInfo.objects.filter(created_by=request.user).update(sex=sex, age=age, pregnancy=pregnancy, height=height, weight=weight, activity_level=activity, timezone=timezone)
            else:
                UseInfo.objects.create(created_by=request.user, sex=sex, age=age, pregnancy=pregnancy, height=height, weight=weight, activity_level=activity, timezone=timezone)


        request.session['user_data'] = user_data

        return redirect('dri_result')

    
    return render(request, 'calculate.html', context=context)

def article(request):

    return render(request, 'article.html')
    

@login_required
def add_sda(request):

    return render(request, 'add_sda.html')


def add_log(ind, value, log_date, user):

    food = AllFood.objects.get(id=ind)

    measure = value / 100

    UserLogFood.objects.create(created_by=user, created_at=log_date, food_name=food.name, measure=value)

    



    calories = food.calories * measure# 1 = 0.001
    water = (float(food.water.split()[0]) * 0.001) * measure
    carbohydrate = ((float(food.carbohydrate.split()[0])*1000) + (float(food.fructose.split()[0])*1000) + (float(food.glucose.split()[0])*1000) + (float(food.maltose.split()[0])*1000) + (float(food.sucrose.split()[0])*1000)) * measure
    total_fiber = (float(food.fiber.split()[0]) * 1000) * measure
    protein = float(food.protein.split()[0]) * 1000 * measure
    fat = float(food.total_fat.replace('g', '')) * 1000 * measure
    sat_fat = float(food.saturated_fat.replace('g', '')) * 1000 * measure
    trans_fat = float(food.fatty_acids_total_trans.split()[0]) * measure
    dietary_cholesterol = float(food.cholesterol.replace('mg', '')) * measure
    sugar = float(food.sugars.split()[0]) * 1000 * measure
 
    # # Vitamins
    vitamin_a = ((float(food.vitamin_a.split()[0]) * 0.3) / 1000 + (float(food.vitamin_a_rae.split()[0]) / 1000)) * measure
    vitamin_b_6 = float(food.vitamin_b6.split()[0]) * measure
    vitamin_b_12 = (float(food.vitamin_b12.split()[0]) / 1000) * measure
    vitamin_c = float(food.vitamin_c.split()[0]) * measure
    vitamin_d = (float(food.vitamin_d.split()[0]) * 0.025) / 1000 * measure
    vitamin_e = (float(food.vitamin_e.split()[0]) + float(food.tocopherol_alpha.split()[0])) * measure
    vitamin_k = (float(food.vitamin_k.split()[0]) / 1000) * measure
    thiamin = float(food.thiamin.split()[0]) * measure
    riboflavin = float(food.riboflavin.split()[0]) * measure
    folate = float(food.folate.split()[0]) / 1000 * measure
    niacin = float(food.niacin.split()[0]) * measure
    choline = float(food.choline.split()[0]) * measure
    pantothenic_acid = float(food.pantothenic_acid.split()[0]) * measure
    carotenoids = (float(food.carotene_alpha.split()[0]) / 1000 + float(food.carotene_beta.split()[0]) / 1000 + float(food.cryptoxanthin_beta.split()[0]) / 1000 + float(food.lutein_zeaxanthin.split()[0]) / 1000) * measure

    # # Minerals
    calcium = float(food.calcium.split()[0]) * measure
    copper = float(food.copper.split()[0]) * measure
    iron = float(food.irom.split()[0]) * measure
    magnesium = float(food.magnesium.split()[0]) * measure
    manganese = float(food.manganese.split()[0]) * measure
    phosphorus = float(food.phosphorous.split()[0]) * measure
    potassium = float(food.potassium.split()[0]) * measure
    selenium = float(food.selenium.split()[0]) / 1000 * measure
    sodium = float(food.sodium.split()[0]) * measure
    zinc = float(food.zink.split()[0]) * measure

    # # Amino Acids
    histidine = float(food.histidine.split()[0]) * 1000 * measure 
    isoleucine = float(food.isoleucine.split()[0]) * 1000 * measure
    leucine = float(food.leucine.split()[0]) * 1000 * measure
    lysine = float(food.lysine.split()[0]) * 1000 * measure
    methionine = float(food.methionine.split()[0]) * 1000 * measure
    cysteine = float(food.cystine.split()[0]) * 1000 * measure
    phenylalanine = float(food.phenylalanine.split()[0]) * 1000 * measure
    tyrosine = float(food.tyrosine.split()[0]) * 1000 * measure
    threonine = float(food.threonine.split()[0]) * 1000 * measure
    tryptophan = float(food.tryptophan.split()[0]) * 1000 * measure
    valine = float(food.valine.split()[0]) * 1000 * measure


    if UserLog.objects.filter(created_at=log_date, created_by=user).exists():

        UserLog.objects.filter(created_at=log_date, created_by=user).update(calories=F('calories')+calories, water=F('water')+water, carbohydrate=F('carbohydrate')+carbohydrate, 
                    total_fiber=F('total_fiber')+total_fiber, protein=F('protein')+protein, fat=F('fat')+fat, sat_fat=F('sat_fat')+sat_fat, trans_fat=F('trans_fat')+trans_fat, dietary_cholesterol=F('dietary_cholesterol')+dietary_cholesterol,
                    sugar=F('sugar')+sugar, vitamin_a=F('vitamin_a')+vitamin_a, vitamin_b_6=F('vitamin_b_6')+vitamin_b_6, vitamin_b_12=F('vitamin_b_12')+vitamin_b_12, vitamin_c=F('vitamin_c')+vitamin_c,
                    vitamin_d=F('vitamin_d')+vitamin_d, vitamin_e=F('vitamin_e')+vitamin_e, vitamin_k=F('vitamin_k')+vitamin_k, thiamin=F('thiamin')+thiamin, riboflavin=F('riboflavin')+riboflavin,
                    folate=F('folate')+folate, niacin=F('niacin')+niacin, choline=F('choline')+choline, pantothenic_acid=F('pantothenic_acid')+pantothenic_acid,
                    carotenoids=F('carotenoids')+carotenoids, calcium=F('calcium')+calcium, copper=F('copper')+copper, iron=F('iron')+iron, magnesium=F('magnesium')+magnesium,
                    manganese=F('manganese')+manganese, phosphorus=F('phosphorus')+phosphorus, potassium=F('potassium')+potassium, selenium=F('selenium')+selenium, sodium=F('sodium')+sodium, zinc=F('zinc')+zinc,
                    histidine=F('histidine')+histidine, isoleucine=F('isoleucine')+histidine, leucine=F('leucine')+leucine, lysine=F('lysine')+lysine, methionine=F('methionine')+methionine, cysteine=F('cysteine')+cysteine,
                    phenylalanine=F('phenylalanine')+phenylalanine, tyrosine=F('tyrosine')+tyrosine, threonine=F('threonine')+threonine, tryptophan=F('tryptophan')+tryptophan, valine=F('valine')+valine)

    else:
        UserLog.objects.create(created_by=user, created_at=log_date, calories=calories, water=water, carbohydrate=carbohydrate, 
                    total_fiber=total_fiber, protein=protein, fat=fat, sat_fat=sat_fat, trans_fat=trans_fat, dietary_cholesterol=dietary_cholesterol,
                    sugar=sugar, vitamin_a=vitamin_a, vitamin_b_6=vitamin_b_6, vitamin_b_12=vitamin_b_12, vitamin_c=vitamin_c,
                    vitamin_d=vitamin_d, vitamin_e=vitamin_e, vitamin_k=vitamin_k, thiamin=thiamin, riboflavin=riboflavin,
                    folate=folate, niacin=niacin, choline=choline, pantothenic_acid=pantothenic_acid,
                    carotenoids=carotenoids, calcium=calcium, copper=copper, iron=iron, magnesium=magnesium,
                    manganese=manganese, phosphorus=phosphorus, potassium=potassium, selenium=selenium, sodium=sodium, zinc=zinc,
                    histidine=histidine, isoleucine=isoleucine, leucine=leucine, lysine=lysine, methionine=methionine, cysteine=cysteine,
                    phenylalanine=phenylalanine, tyrosine=tyrosine, threonine=threonine, tryptophan=tryptophan, valine=valine)


def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100


def logdata(user, cur_date):

    if not UserRDA.objects.filter(created_by=user).exists():
        return redirect('calculate')

    user_rda = UserRDA.objects.filter(created_by=user).values()[0]

    is_log = UserLog.objects.filter(created_by=user, created_at=cur_date).exists()

    if is_log:
        today_log = UserLog.objects.filter(created_by=user, created_at=cur_date).values()[0]

    rda = {}

    for k, v in user_rda.items():

        if k == "water":
            if is_log:
                rda["Water"] = {"rd": str(v) + " liters", "lg": str(round(today_log[k], 2)) + " liters", "ps": is_what_percent_of(today_log[k], v)}
            else:
                rda["Water"] = {"rd": str(v) + " liters", "lg": "0 liters", "ps": 0}

        elif k == "calories":
            if is_log:
                rda["Calories"] = {"rd": str(v) + " kcal", "lg": str(round(today_log[k], 2)) + " kcal", "ps": is_what_percent_of(today_log[k], v)}
            else:
                rda["Calories"] = {"rd": str(v) + " kcal", "lg": "0 kcal", "ps": 0}

        elif k == "created_by_id" or k == "created_at" or k == "updated_at" or k == "id":
            continue
        else:
            if v >= 1000:
                new_value = str(v / 1000) + " grams"
            else:
                new_value = str(v) + " mg"

            if is_log:
                if today_log[k] >= 1000:
                    log_value = str(round(today_log[k] / 1000, 2)) + " grams"
                else:
                    log_value = str(round(today_log[k], 2)) + " mg"
                
                percentage = is_what_percent_of(today_log[k], v)
            else:
                log_value = "0 grams"
                percentage = 0
            
            new_key = k.replace("_", " ").title()
            rda[new_key] = {"rd": new_value, "lg": log_value, "ps": percentage}

    food_objs = UserLogFood.objects.filter(created_by=user, created_at=cur_date)

    foods = []

    for food in food_objs:
        temp={}
        temp["name"] = food.food_name
        temp["measure"] = food.measure
        foods.append(temp)


    context = {"rda": rda, 'foods': foods}

    return context


        


@login_required
def profile(request):

    today = datetime.today().date()

            # log[new_key] = log_value

    # for k, v in user_rda.items():
    #     if k == "water":
    #         if is_log:
    #             rda["Water"] = str(round(today_log[k], 2)) + " liters / " + str(v) + " liters  " + str(v-today_log[k]) + " liters need" if str(today_log[k] < v) else + today_log[k]-v + " liters over"
    #         else:
    #             rda["Water"] = "0 liters / " + str(v) + " liters" + str(-v) + " liters"

    #     elif k == "calories":
    #         if is_log:
    #             rda["Calories"] = str(round(today_log[k], 2)) + " kcal / " + str(v) + " kcal"
    #         else:
    #             rda["Calories"] = "0 kcal / " + str(v) + " kcal" 
    #     elif k == "created_by_id" or k == "created_at" or k == "updated_at" or k == "id":
    #         continue
    #     else:
    #         if v >= 1000:
    #             new_value = str(v / 1000) + " grams"
    #         else:
    #             new_value = str(v) + " mg"

    #         if is_log:
    #             if today_log[k] >= 1000:
    #                 log_value = str(round(today_log[k] / 1000, 2)) + " grams"
    #             else:
    #                 log_value = str(round(today_log[k], 2)) + " mg"
    #         else:
    #             log_value = "0 grams"
            
    #         new_key = k.replace("_", " ").title()
    #         rda[new_key] = log_value + " / " + new_value

    

    
    context = logdata(request.user, today)


    return render(request, 'profile.html', context=context)


@login_required
def data_date(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cur_date = request.POST.get('cur_date')

        date_time_obj = datetime.strptime(cur_date, '%Y-%m-%d')

        cur_dt = date_time_obj.date()

        data = logdata(request.user, cur_dt)
         
        return JsonResponse({'data': data})

    return JsonResponse({})


@login_required
def add_nutrition(request):

    return render(request, 'add_nutrition.html')


@login_required
def store_consumed_nutritions(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        log_date = request.POST.get('log_date')
        consumed_nutritions = request.POST.getlist('consumed_nutritions[]')

        user = request.user

        tmz = user.user_info.timezone

        log_date= datetime.strptime(log_date, '%Y-%m-%d').date()
        
        
        new = False

        if UserLog.objects.filter(created_at=log_date, created_by=user).exists():
            old = UserLog.objects.filter(created_at=log_date, created_by=user).values()[0]
        else:
            new = True
            old = 0
        
        for nut in consumed_nutritions:
            ind, val = nut.split(',')
            ind = int(ind)
            val = int(val)

            add_log(ind, val, log_date, user)

        data = {}

        if new:
            new = UserLog.objects.filter(created_at=log_date, created_by=user).values()[0]
            for k, v in new.items():
                if k == "water":
                    data["Water"] = str(round(v, 3)) + " liters" 
                elif k == "calories":
                    data["Calories"] = str(round(v, 3)) + " ckal"
                elif k == "created_by_id" or k == "created_at" or k == "updated_at" or k == "id":
                    continue
                else:

                    if v >= 1000:
                        new_value = str(round(v / 1000, 3)) + " grams"
                    else:
                        new_value = str(round(v, 3)) + " mg"
                
                    new_key = k.replace("_", " ").title()
                    data[new_key] = new_value
        else:

            new = UserLog.objects.filter(created_at=log_date, created_by=user).values()[0]
            for k in new:
                if k == "water":
                    val = round(new[k] - old[k], 3)
                    data["Water"] = str(val) + " liters" 
                elif k == "calories":
                    val = round(new[k] - old[k], 3)
                    data["Calories"] = str(val) + " ckal"
                elif k == "created_by_id" or k == "created_at" or k == "updated_at" or k == "id":
                    continue
                else:
                    val = round(new[k] - old[k], 3)

                    if val >= 1000:
                        new_value = str(round(val / 1000, 3)) + " grams"
                    else:
                        new_value = str(round(val, 3)) + " mg"


                    new_key = k.replace("_", " ").title()
                    data[new_key] = new_value


        return JsonResponse({'data': data})

    return JsonResponse({})



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




