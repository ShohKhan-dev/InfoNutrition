from django.db import models

# Create your models here.


class MainCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class BasicStats(models.Model):
    category = models.ForeignKey(MainCategory, related_name='stat_items', on_delete=models.CASCADE)
    grams = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    sat_fat = models.FloatField()
    fiber = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return self.category.name



class BasicFood(models.Model):
    name = models.CharField(max_length=255)
    measure = models.CharField(max_length=250)
    grams = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    sat_fat = models.FloatField()
    fiber = models.FloatField()
    carbs = models.FloatField()
    category = models.ForeignKey(MainCategory, related_name='food_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AllFood(models.Model):
    name = models.CharField(max_length=255)
    serving_size = models.CharField(max_length=100)
    calories = models.FloatField()
    total_fat = models.CharField(max_length=100)
    saturated_fat = models.CharField(max_length=100, null=True)
    cholesterol = models.CharField(max_length=100)
    sodium = models.CharField(max_length=100)
    choline = models.CharField(max_length=100)
    folate = models.CharField(max_length=100)
    folic_acid = models.CharField(max_length=100)
    niacin = models.CharField(max_length=100)
    pantothenic_acid = models.CharField(max_length=100)
    riboflavin = models.CharField(max_length=100)
    thiamin = models.CharField(max_length=100)
    vitamin_a = models.CharField(max_length=100)
    vitamin_a_rae = models.CharField(max_length=100)
    carotene_alpha = models.CharField(max_length=100)
    carotene_beta = models.CharField(max_length=100)
    cryptoxanthin_beta = models.CharField(max_length=100)
    lutein_zeaxanthin = models.CharField(max_length=100)
    lucopene = models.CharField(max_length=100)
    vitamin_b12 = models.CharField(max_length=100)
    vitamin_b6 = models.CharField(max_length=100)
    vitamin_c = models.CharField(max_length=100)
    vitamin_d = models.CharField(max_length=100)
    vitamin_e = models.CharField(max_length=100)
    tocopherol_alpha = models.CharField(max_length=100)
    vitamin_k = models.CharField(max_length=100)
    calcium = models.CharField(max_length=100)
    copper = models.CharField(max_length=100)
    irom = models.CharField(max_length=100)
    magnesium = models.CharField(max_length=100)
    manganese = models.CharField(max_length=100)
    phosphorous = models.CharField(max_length=100)
    potassium = models.CharField(max_length=100)
    selenium = models.CharField(max_length=100)
    zink = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    alanine = models.CharField(max_length=100)
    arginine = models.CharField(max_length=100)
    aspartic_acid = models.CharField(max_length=100)
    cystine = models.CharField(max_length=100)
    glutamic_acid = models.CharField(max_length=100)
    glycine = models.CharField(max_length=100)
    histidine = models.CharField(max_length=100)
    hydroxyproline = models.CharField(max_length=100)
    isoleucine = models.CharField(max_length=100)
    leucine = models.CharField(max_length=100)
    lysine = models.CharField(max_length=100)
    methionine = models.CharField(max_length=100)
    phenylalanine = models.CharField(max_length=100)
    proline = models.CharField(max_length=100)
    serine = models.CharField(max_length=100)
    threonine = models.CharField(max_length=100)
    tryptophan = models.CharField(max_length=100)
    tyrosine = models.CharField(max_length=100)
    valine = models.CharField(max_length=100)
    carbohydrate = models.CharField(max_length=100)
    fiber = models.CharField(max_length=100)
    sugars = models.CharField(max_length=100)
    fructose = models.CharField(max_length=100)
    galactose = models.CharField(max_length=100)
    glucose = models.CharField(max_length=100)
    lactose = models.CharField(max_length=100)
    maltose = models.CharField(max_length=100)
    sucrose = models.CharField(max_length=100)
    fat = models.CharField(max_length=100)
    saturated_fatty_acids = models.CharField(max_length=100)
    monounsaturated_fatty_acids = models.CharField(max_length=100)
    polyunsaturated_fatty_acids = models.CharField(max_length=100)
    fatty_acids_total_trans = models.CharField(max_length=100)
    alcohol = models.CharField(max_length=100)
    ash = models.CharField(max_length=100)
    caffeine = models.CharField(max_length=100)
    theobromine = models.CharField(max_length=100)
    water = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    


    
    