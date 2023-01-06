from django.db import models
from django.contrib.auth.models import User

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
    saturated_fat = models.CharField(max_length=100)
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



class UseInfo(models.Model):
    created_by = models.OneToOneField(User, related_name='user_info', on_delete=models.CASCADE)
    sex = models.CharField(max_length=10)
    age = models.FloatField()
    pregnancy = models.CharField(max_length=100, null=True)
    height = models.FloatField()
    weight = models.FloatField()
    activity_level = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.created_by.username + '_Info'



class UserLog(models.Model):

    created_by = models.ForeignKey(User, related_name='user_logs', on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    # Macronutrient
    calories = models.FloatField(default=0) # calories
    water = models.FloatField(default=0) # water
    carbohydrate = models.FloatField(default=0) # carbohydrate + fructose + glucose + galactose + lactose + maltose + sucrose
    total_fiber = models.FloatField(default=0) # fiber
    protein = models.FloatField(default=0) # protein + alanine + arginine + aspartic_acid
    fat = models.FloatField(default=0) # total_fat
    sat_fat = models.FloatField(default=0) # saturated_fat
    trans_fat = models.FloatField(default=0) # fatty_acids_total_trans
    dietary_cholesterol = models.FloatField(default=0) # cholesterol
    sugar = models.FloatField(default=0) # sugars
 
    # Vitamins
    vitamin_a = models.FloatField(default=0) # vitamin_a + vitamin_a_rae
    vitamin_b_6 = models.FloatField(default=0) # vitamin_b6
    vitamin_b_12 = models.FloatField(default=0) # vitamin_b12
    vitamin_c = models.FloatField(default=0) # vitamin_c
    vitamin_d = models.FloatField(default=0) # vitamin_d
    vitamin_e = models.FloatField(default=0) # vitamin_e + tocopherol_alpha
    vitamin_k = models.FloatField(default=0) # vitamin_k
    thiamin = models.FloatField(default=0) # thiamin
    riboflavin = models.FloatField(default=0) # riboflavin
    folate = models.FloatField(default=0) # folate
    niacin = models.FloatField(default=0) # niacin
    choline = models.FloatField(default=0) # choline
    pantothenic_acid = models.FloatField(default=0) # pantothenic_acid
    carotenoids = models.FloatField(default=0) # carotene_alpha + carotene_beta + cryptoxanthin_beta + lutein zeaxanthin + lucopene

    # Minerals
    calcium = models.FloatField(default=0) # calcium
    copper = models.FloatField(default=0) # copper
    iron = models.FloatField(default=0) # irom
    magnesium = models.FloatField(default=0) # magnesium
    manganese = models.FloatField(default=0) # manganese
    phosphorus = models.FloatField(default=0) # phosphorous
    potassium = models.FloatField(default=0) # potassium
    selenium = models.FloatField(default=0) # selenium
    sodium = models.FloatField(default=0) # sodium
    zinc = models.FloatField(default=0) # zink

    # Amino Acids
    histidine = models.FloatField(default=0) # histidine
    isoleucine = models.FloatField(default=0) # isoleucine
    leucine = models.FloatField(default=0) # leucine
    lysine = models.FloatField(default=0) # lysine
    methionine = models.FloatField(default=0) # methionine
    cysteine = models.FloatField(default=0) # cystine
    phenylalanine = models.FloatField(default=0) # phenylalanine
    tyrosine = models.FloatField(default=0) # tyrosine
    threonine = models.FloatField(default=0) # threonine
    tryptophan = models.FloatField(default=0) # tryptophan
    valine = models.FloatField(default=0) # valine

    def __str__(self):
        return self.created_by.username+'_'+str(self.created_at)+'_Log'



class UserRDA(models.Model):

    created_by = models.OneToOneField(User, related_name='user_rda', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Macronutrient
    calories = models.FloatField(null=True) # calories
    water = models.FloatField(null=True) # water
    carbohydrate = models.FloatField(null=True) # carbohydrate + fructose + glucose + galactose + lactose + maltose + sucrose
    total_fiber = models.FloatField(null=True) # fiber
    protein = models.FloatField(null=True) # protein + alanine + arginine + aspartic_acid
    fat = models.FloatField(null=True) # total_fat
    sat_fat = models.FloatField(null=True) # saturated_fat
    trans_fat = models.FloatField(null=True) # fatty_acids_total_trans
    dietary_cholesterol = models.FloatField(null=True) # cholesterol
    sugar = models.FloatField(null=True) # sugars
 
    # Vitamins
    vitamin_a = models.FloatField(null=True) # vitamin_a + vitamin_a_rae
    vitamin_b_6 = models.FloatField(null=True) # vitamin_b6
    vitamin_b_12 = models.FloatField(null=True) # vitamin_b12
    vitamin_c = models.FloatField(null=True) # vitamin_c
    vitamin_d = models.FloatField(null=True) # vitamin_d
    vitamin_e = models.FloatField(null=True) # vitamin_e + tocopherol_alpha
    vitamin_k = models.FloatField(null=True) # vitamin_k
    thiamin = models.FloatField(null=True) # thiamin
    riboflavin = models.FloatField(null=True) # riboflavin
    folate = models.FloatField(null=True) # folate
    niacin = models.FloatField(null=True) # niacin
    choline = models.FloatField(null=True) # choline
    pantothenic_acid = models.FloatField(null=True) # pantothenic_acid
    carotenoids = models.FloatField(null=True) # carotene_alpha + carotene_beta + cryptoxanthin_beta + lutein zeaxanthin + lucopene

    # Minerals
    calcium = models.FloatField(null=True) # calcium
    copper = models.FloatField(null=True) # copper
    iron = models.FloatField(null=True) # irom
    magnesium = models.FloatField(null=True) # magnesium
    manganese = models.FloatField(null=True) # manganese
    phosphorus = models.FloatField(null=True) # phosphorous
    potassium = models.FloatField(null=True) # potassium
    selenium = models.FloatField(null=True) # selenium
    sodium = models.FloatField(null=True) # sodium
    zinc = models.FloatField(null=True) # zink

    # Amino Acids
    histidine = models.FloatField(null=True) # histidine
    isoleucine = models.FloatField(null=True) # isoleucine
    leucine = models.FloatField(null=True) # leucine
    lysine = models.FloatField(null=True) # lysine
    methionine = models.FloatField(null=True) # methionine
    cysteine = models.FloatField(null=True) # cystine
    phenylalanine = models.FloatField(null=True) # phenylalanine
    tyrosine = models.FloatField(null=True) # tyrosine
    threonine = models.FloatField(null=True) # threonine
    tryptophan = models.FloatField(null=True) # tryptophan
    valine = models.FloatField(null=True) # valine

    def __str__(self):
        return self.created_by.username + '_RDA'



class UserSDA(models.Model):

    created_by = models.OneToOneField(User, related_name='user_sda', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Macronutrient
    calories = models.FloatField(null=True) # calories
    water = models.FloatField(null=True) # water
    carbohydrate = models.FloatField(null=True) # carbohydrate + fructose + glucose + galactose + lactose + maltose + sucrose
    total_fiber = models.FloatField(null=True) # fiber
    protein = models.FloatField(null=True) # protein + alanine + arginine + aspartic_acid
    fat = models.FloatField(null=True) # total_fat
    sat_fat = models.FloatField(null=True) # saturated_fat
    trans_fat = models.FloatField(null=True) # fatty_acids_total_trans
    dietary_cholesterol = models.FloatField(null=True) # cholesterol
    sugar = models.FloatField(null=True) # sugars
 
    # Vitamins
    vitamin_a = models.FloatField(null=True) # vitamin_a + vitamin_a_rae
    vitamin_b_6 = models.FloatField(null=True) # vitamin_b6
    vitamin_b_12 = models.FloatField(null=True) # vitamin_b12
    vitamin_c = models.FloatField(null=True) # vitamin_c
    vitamin_d = models.FloatField(null=True) # vitamin_d
    vitamin_e = models.FloatField(null=True) # vitamin_e + tocopherol_alpha
    vitamin_k = models.FloatField(null=True) # vitamin_k
    thiamin = models.FloatField(null=True) # thiamin
    riboflavin = models.FloatField(null=True) # riboflavin
    folate = models.FloatField(null=True) # folate
    niacin = models.FloatField(null=True) # niacin
    choline = models.FloatField(null=True) # choline
    pantothenic_acid = models.FloatField(null=True) # pantothenic_acid
    carotenoids = models.FloatField(null=True) # carotene_alpha + carotene_beta + cryptoxanthin_beta + lutein zeaxanthin + lucopene

    # Minerals
    calcium = models.FloatField(null=True) # calcium
    copper = models.FloatField(null=True) # copper
    iron = models.FloatField(null=True) # irom
    magnesium = models.FloatField(null=True) # magnesium
    manganese = models.FloatField(null=True) # manganese
    phosphorus = models.FloatField(null=True) # phosphorous
    potassium = models.FloatField(null=True) # potassium
    selenium = models.FloatField(null=True) # selenium
    sodium = models.FloatField(null=True) # sodium
    zinc = models.FloatField(null=True) # zink

    # Amino Acids
    histidine = models.FloatField(null=True) # histidine
    isoleucine = models.FloatField(null=True) # isoleucine
    leucine = models.FloatField(null=True) # leucine
    lysine = models.FloatField(null=True) # lysine
    methionine = models.FloatField(null=True) # methionine
    cysteine = models.FloatField(null=True) # cystine
    phenylalanine = models.FloatField(null=True) # phenylalanine
    tyrosine = models.FloatField(null=True) # tyrosine
    threonine = models.FloatField(null=True) # threonine
    tryptophan = models.FloatField(null=True) # tryptophan
    valine = models.FloatField(null=True) # valine

    def __str__(self):
        return self.created_by.username + '_SDA'




class UserLogFood(models.Model):

    created_by = models.ForeignKey(User, related_name='user_log_foods', on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    food_name = models.CharField(max_length=255)
    measure = models.FloatField(default=1) 
    
 
    def __str__(self):
        return self.created_by.username+'_'+str(self.created_at)+'_Log_Food'
