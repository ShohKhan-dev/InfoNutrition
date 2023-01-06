

def pregnancy_level(pregnancy, age):

    preg_lev = None

    if pregnancy:
        if pregnancy in ["pregnant-1st-trimester", "pregnant-2nd-trimester", "pregnant-2nd-trimester-more", "pregnant-3rd-trimester"]:
            if age <= 18:
                preg_lev = "pregnant_18"
            else:
                preg_lev = "pregnant_19-50"
        else:
            if age <= 18:
                preg_lev = "lactant_18"
            else:
                preg_lev = "lactant_19-50"
    return preg_lev


def sex_index(sex):
    if sex == "male":
        sex_ind = 0
    else:
        sex_ind = 1

    return sex_ind


def age_stage(age):

    if 0 <= age <= 0.5:
        stage = "0-6m"
    elif 0.5 < age <= 1:
        stage = "7-12m"
    elif 1 < age <= 3:
        stage = "1-3"
    elif 3 < age <= 8:
        stage = "4-8"
    elif 8 < age <= 13:
        stage = "9-13"
    elif 13 < age <= 18:
        stage = "14-18"
    elif 18 < age <= 30:
        stage = "19-30"
    elif 30 < age <= 50:
        stage = "31-50"
    elif 50 < age <= 70:
        stage = "51-70"
    else:
        stage = "70<"

    return stage



class AminoAcids:
    def __init__(self, sex, age, weight, pregnancy):

        self.sex = sex
        self.age = age
        self.pregnancy = pregnancy
        self.weight = weight

        self.histidine = None
        self.isoleucine = None
        self.leucine = None
        self.lysine = None
        self.methionine = None
        self.cysteine = None
        self.phenylalanine = None
        self.tyrosine = None
        self.threonine = None
        self.tryptophan = None
        self.valine = None

    def return_amino_acids(self):

        if self.pregnancy:
            if self.pregnancy in ["pregnant-1st-trimester", "pregnant-2nd-trimester", "pregnant-2nd-trimester-more", "pregnant-3rd-trimester"]:
                self.histidine = self.weight * 18
                self.isoleucine = self.weight * 25
                self.leucine = self.weight * 56
                self.lysine = self.weight * 51
                self.methionine = self.weight * 25
                self.cysteine = self.weight * 25
                self.phenylalanine = self.weight * 44
                self.tyrosine = self.weight * 44
                self.threonine = self.weight * 26
                self.tryptophan = self.weight * 7
                self.valine = self.weight *  31
            else:
                self.histidine = self.weight * 19
                self.isoleucine = self.weight * 30
                self.leucine = self.weight * 62
                self.lysine = self.weight * 52
                self.methionine = self.weight * 26
                self.cysteine = self.weight * 26
                self.phenylalanine = self.weight * 51
                self.tyrosine = self.weight * 51
                self.threonine = self.weight * 30
                self.tryptophan = self.weight * 9
                self.valine = self.weight *  35
        
        else:
            if 0 < self.age <= 0.5:
                self.histidine = self.weight * 36
                self.isoleucine = self.weight * 88
                self.leucine = self.weight * 156
                self.lysine = self.weight * 107
                self.methionine = self.weight * 59
                self.cysteine = self.weight * 59
                self.phenylalanine = self.weight * 135
                self.tyrosine = self.weight * 135
                self.threonine = self.weight * 73
                self.tryptophan = self.weight * 28
                self.valine = self.weight *  87
            elif self.age <= 1:
                self.histidine = self.weight * 32
                self.isoleucine = self.weight * 43
                self.leucine = self.weight * 93
                self.lysine = self.weight * 89
                self.methionine = self.weight * 43
                self.cysteine = self.weight * 43
                self.phenylalanine = self.weight * 84
                self.tyrosine = self.weight * 84
                self.threonine = self.weight * 49
                self.tryptophan = self.weight * 13
                self.valine = self.weight *  58
            elif self.age <= 3:
                self.histidine = self.weight * 21
                self.isoleucine = self.weight * 28
                self.leucine = self.weight * 63
                self.lysine = self.weight * 58
                self.methionine = self.weight * 28
                self.cysteine = self.weight * 28
                self.phenylalanine = self.weight * 54
                self.tyrosine = self.weight * 54
                self.threonine = self.weight * 32
                self.tryptophan = self.weight * 8
                self.valine = self.weight *  37
            elif self.age <= 8:
                self.histidine = self.weight * 16
                self.isoleucine = self.weight * 22
                self.leucine = self.weight * 49
                self.lysine = self.weight * 46
                self.methionine = self.weight * 22
                self.cysteine = self.weight * 22
                self.phenylalanine = self.weight * 41
                self.tyrosine = self.weight * 41
                self.threonine = self.weight * 24
                self.tryptophan = self.weight * 6
                self.valine = self.weight *  28
            elif self.age <= 13 and self.sex == 'male':
                self.histidine = self.weight * 17
                self.isoleucine = self.weight * 22
                self.leucine = self.weight * 49
                self.lysine = self.weight * 46
                self.methionine = self.weight * 22
                self.cysteine = self.weight * 22
                self.phenylalanine = self.weight * 41
                self.tyrosine = self.weight * 41
                self.threonine = self.weight * 24
                self.tryptophan = self.weight * 6
                self.valine = self.weight * 28
            elif self.age <= 13 and self.sex == 'female':
                self.histidine = self.weight * 15
                self.isoleucine = self.weight * 21
                self.leucine = self.weight * 47
                self.lysine = self.weight * 43
                self.methionine = self.weight * 21
                self.cysteine = self.weight * 21
                self.phenylalanine = self.weight * 38
                self.tyrosine = self.weight * 38
                self.threonine = self.weight * 22
                self.tryptophan = self.weight * 6
                self.valine = self.weight * 27
            elif self.age <= 18 and self.sex == 'male':
                self.histidine = self.weight * 15
                self.isoleucine = self.weight * 21
                self.leucine = self.weight * 47
                self.lysine = self.weight * 43
                self.methionine = self.weight * 21
                self.cysteine = self.weight * 21
                self.phenylalanine = self.weight * 38
                self.tyrosine = self.weight * 38
                self.threonine = self.weight * 22
                self.tryptophan = self.weight * 6
                self.valine = self.weight * 27
            elif self.age <= 18 and self.sex == 'female':
                self.histidine = self.weight * 14
                self.isoleucine = self.weight * 19
                self.leucine = self.weight * 44
                self.lysine = self.weight * 40
                self.methionine = self.weight * 19
                self.cysteine = self.weight * 19
                self.phenylalanine = self.weight * 35
                self.tyrosine = self.weight * 35
                self.threonine = self.weight * 21
                self.tryptophan = self.weight * 5
                self.valine = self.weight * 24
            else:
                self.histidine = self.weight * 14
                self.isoleucine = self.weight * 19
                self.leucine = self.weight * 42
                self.lysine = self.weight * 38
                self.methionine = self.weight * 19
                self.cysteine = self.weight * 19
                self.phenylalanine = self.weight * 33
                self.tyrosine = self.weight * 33
                self.threonine = self.weight * 20
                self.tryptophan = self.weight * 5
                self.valine = self.weight * 24
        
        res = {"histidine": self.histidine, "isoleucine": self.isoleucine, "leucine": self.leucine, "lysine": self.lysine,
               "methionine": self.methionine, "cysteine": self.cysteine, "phenylalanine": self.phenylalanine, "tyrosine": self.tyrosine,
               "threonine": self.threonine, "tryptophan": self.tryptophan, "valine": self.valine}

        return res
        
    


class Minerals:
    def __init__(self, sex, age, pregnancy):

        self.sex = sex
        self.age = age
        self.pregnancy = pregnancy

        self.stage = age_stage(self.age)
        self.sex_ind = sex_index(self.sex)
        self.preg_lev = pregnancy_level(self.pregnancy, self.age)

        self.calcium = self.calcium_cal()
        self.chloride = self.chloride_cal()
        self.chromium = self.chromium_cal()
        self.copper = self.copper_cal()
        self.fluoride = self.fluoride_cal()
        self.lodine = self.lodine_cal()
        self.iron = self.iron_cal()
        self.magnesium = self.magnesium_cal()
        self.manganese = self.manganese_cal()
        self.molybdenum = self.molybdenum_cal()
        self.phosphorus = self.phosphorus_cal()
        self.potassium = self.potassium_cal()
        self.selenium = self.selenium_cal()
        self.sodium = self.sodium_cal()
        self.zinc = self.zinc_cal()
        


    def get_rda_ul(self, table, pregnant):
        rda = None
        ul = None

        if self.pregnancy:
            rda = pregnant[self.preg_lev][0]
            ul = pregnant[self.preg_lev][1]
        else:
            rda = table[self.stage][self.sex_ind]
            ul = table[self.stage][2]

        res = {"rda": rda, "ul": ul}

        return res

    def return_minerals(self):

        minerals = {"calcium": self.calcium, "chloride": self.chloride, "chromium": self.chromium, "copper": self.copper,
                    "fluoride": self.fluoride, "lodine": self.lodine, "iron": self.iron, "magnesium": self.magnesium,
                    "manganese": self.manganese, "molybdenum": self.molybdenum, "phosphorus": self.phosphorus, "potassium": self.potassium,
                    "selenium": self.selenium, "sodium": self.sodium, "zinc": self.zinc}

        return minerals

    def calcium_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [210, 210, None], 
                "7-12m": [270, 270, None], 
                  "1-3": [500, 500, 2500], 
                  "4-8": [800, 800, 2500], 
                 "9-13": [1300, 1300, 2500], 
                "14-18": [1300, 1300, 2500],
                "19-30": [1000, 1000, 2500],
                "31-50": [1000, 1000, 2500],
                "51-70": [1200, 1200, 2500],
                  "70<": [1200, 1200, 2500]}

        pregnant = {
            "pregnant_18": [1300, 2500],
            "pregnant_19-50": [1000, 2500],
            "lactant_18": [1300, 2500],
            "lactant_19-50": [1000, 2500]
        }

        result = self.get_rda_ul(table, pregnant)
        return result


    def chloride_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.18, 0.18, None], 
                "7-12m": [0.57, 0.57, None], 
                  "1-3": [1.5, 1.5, 2.3], 
                  "4-8": [1.9, 1.9, 2.9], 
                 "9-13": [2.3, 2.3, 3.4], 
                "14-18": [2.3, 2.3, 3.6],
                "19-30": [2.3, 2.3, 3.6],
                "31-50": [2.3, 2.3, 3.6],
                "51-70": [2.0, 2.0, 3.6],
                  "70<": [1.8, 1.8, 3.6]}

        pregnant = {
            "pregnant_18": [2.3, 3.6],
            "pregnant_19-50": [2.3, 3.6],
            "lactant_18": [2.3, 3.6],
            "lactant_19-50": [2.3, 3.6]
        }

        result = self.get_rda_ul(table, pregnant)
        return result


    def sodium_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.12, 0.12, None], 
                "7-12m": [0.37, 0.37, None], 
                  "1-3": [1.0, 1.0, 1.5], 
                  "4-8": [1.2, 1.2, 1.9], 
                 "9-13": [1.5, 1.5, 2.2], 
                "14-18": [1.5, 1.5, 2.3],
                "19-30": [1.5, 1.5, 2.3],
                "31-50": [1.5, 1.5, 2.3],
                "51-70": [1.3, 1.3, 2.3],
                  "70<": [1.2, 1.2, 2.3]}

        pregnant = {
            "pregnant_18": [1.5, 2.3],
            "pregnant_19-50": [1.5, 2.3],
            "lactant_18": [1.5, 2.3],
            "lactant_19-50": [1.5, 2.3]
        }

        result = self.get_rda_ul(table, pregnant)
        return result


    def chromium_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.2, 0.2, None], 
                "7-12m": [5.5, 5.5, None], 
                  "1-3": [11, 11, None], 
                  "4-8": [15, 15, None], 
                 "9-13": [25, 21, None], 
                "14-18": [35, 24, None],
                "19-30": [35, 25, None],
                "31-50": [35, 25, None],
                "51-70": [30, 20, None],
                  "70<": [30, 20, None]}

        pregnant = {
            "pregnant_18": [29, None],
            "pregnant_19-50": [30, None],
            "lactant_18": [44, None],
            "lactant_19-50": [45, None]
        }

        result = self.get_rda_ul(table, pregnant)
        return result


    def copper_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [200, 200, None], 
                "7-12m": [220, 220, None], 
                  "1-3": [340, 340, 1000], 
                  "4-8": [440, 440, 3000], 
                 "9-13": [700, 700, 5000], 
                "14-18": [890, 890, 8000],
                "19-30": [900, 900, 10000],
                "31-50": [900, 900, 10000],
                "51-70": [900, 900, 10000],
                  "70<": [900, 900, 10000]}

        pregnant = {
            "pregnant_18": [1000, 8000],
            "pregnant_19-50": [1000, 10000],
            "lactant_18": [1300, 8000],
            "lactant_19-50": [1300, 10000]
        }

        result = self.get_rda_ul(table, pregnant)
        return result

    def fluoride_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.01, 0.01, 0.7], 
                "7-12m": [0.5, 0.5, 0.9], 
                  "1-3": [0.7, 0.7, 1.3], 
                  "4-8": [1, 1, 2.2], 
                 "9-13": [2, 2, 10], 
                "14-18": [3, 3, 10],
                "19-30": [4, 3, 10],
                "31-50": [4, 3, 10],
                "51-70": [4, 3, 10],
                  "70<": [4, 3, 10]}

        pregnant = {
            "pregnant_18": [3, 10],
            "pregnant_19-50": [3, 10],
            "lactant_18": [3, 10],
            "lactant_19-50": [3, 10]
        }

        result = self.get_rda_ul(table, pregnant)
        return result
 
    def lodine_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [110, 110, None], 
                "7-12m": [130, 130, None], 
                  "1-3": [90, 90, 200], 
                  "4-8": [90, 90, 300], 
                 "9-13": [120, 120, 600], 
                "14-18": [150, 150, 900],
                "19-30": [150, 150, 1100],
                "31-50": [150, 150, 1100],
                "51-70": [150, 150, 1100],
                  "70<": [150, 150, 1100]}

        pregnant = {
            "pregnant_18": [220, 900],
            "pregnant_19-50": [220, 1100],
            "lactant_18": [290, 900],
            "lactant_19-50": [290, 1100]
        }

        result = self.get_rda_ul(table, pregnant)
        return result

    def iron_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.27, 0.27, None], 
                "7-12m": [11, 11, 40], 
                  "1-3": [7, 7, 40], 
                  "4-8": [10, 10, 40], 
                 "9-13": [8, 8, 40], 
                "14-18": [11, 15, 45],
                "19-30": [8, 18, 45],
                "31-50": [8, 18, 45],
                "51-70": [8, 8, 45],
                  "70<": [8, 8, 45]}

        pregnant = {
            "pregnant_18": [27, 45],
            "pregnant_19-50": [27, 45],
            "lactant_18": [10, 45],
            "lactant_19-50": [9, 45]
        }

        result = self.get_rda_ul(table, pregnant)
        return result


    def magnesium_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [30, 30, None], 
                "7-12m": [75, 75, None], 
                  "1-3": [80, 80, 65], 
                  "4-8": [130, 130, 110], 
                 "9-13": [240, 240, 350], 
                "14-18": [410, 360, 350],
                "19-30": [400, 310, 350],
                "31-50": [420, 320, 350],
                "51-70": [420, 320, 350],
                  "70<": [420, 320, 350]}

        pregnant = {
            "pregnant_18": [400, 350],
            "pregnant_19-50": [360, 350],
            "lactant_18": [360, 350],
            "lactant_19-50": [320, 350]
        }

        result = self.get_rda_ul(table, pregnant)
        return result

    def manganese_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.003, 0.003, None], 
                "7-12m": [0.6, 0.6, None], 
                  "1-3": [1.2, 1.2, 2], 
                  "4-8": [1.5, 1.5, 3], 
                 "9-13": [1.9, 1.6, 6], 
                "14-18": [2.2, 1.6, 9],
                "19-30": [2.3, 1.8, 11],
                "31-50": [2.3, 1.8, 11],
                "51-70": [2.3, 1.8, 11],
                  "70<": [2.3, 1.8, 11]}

        pregnant = {
            "pregnant_18": [2.0, 9],
            "pregnant_19-50": [2.0, 11],
            "lactant_18": [2.6, 9],
            "lactant_19-50": [2.6, 11]
        }

        result = self.get_rda_ul(table, pregnant)
        return result
  
    def molybdenum_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [2, 2, None], 
                "7-12m": [3, 3, None], 
                  "1-3": [17, 17, 300], 
                  "4-8": [22, 22, 600], 
                 "9-13": [34, 34, 1100], 
                "14-18": [43, 43, 1700],
                "19-30": [45, 45, 2000],
                "31-50": [45, 45, 2000],
                "51-70": [45, 45, 2000],
                  "70<": [45, 45, 2000]}

        pregnant = {
            "pregnant_18": [50, 1700],
            "pregnant_19-50": [50, 2000],
            "lactant_18": [50, 1700],
            "lactant_19-50": [50, 2000]
        }

        result = self.get_rda_ul(table, pregnant)
        return result

    def phosphorus_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [100, 100, None], 
                "7-12m": [275, 275, None], 
                  "1-3": [460, 460, 3000], 
                  "4-8": [500, 500, 3000], 
                 "9-13": [1250, 1250, 4000], 
                "14-18": [1250, 1250, 4000],
                "19-30": [700, 700, 4000],
                "31-50": [700, 700, 4000],
                "51-70": [700, 700, 4000],
                  "70<": [700, 700, 3000]}

        pregnant = {
            "pregnant_18": [1250, 3500],
            "pregnant_19-50": [700, 3500],
            "lactant_18": [1250, 4000],
            "lactant_19-50": [700, 4000]
        }

        result = self.get_rda_ul(table, pregnant)
        return result

    def potassium_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.4, 0.4, None], 
                "7-12m": [0.7, 0.7, None], 
                  "1-3": [3.0, 3.0, None], 
                  "4-8": [3.8, 3.8, None], 
                 "9-13": [4.5, 4.5, None], 
                "14-18": [4.7, 4.7, None],
                "19-30": [4.7, 4.7, None],
                "31-50": [4.7, 4.7, None],
                "51-70": [4.7, 4.7, None],
                  "70<": [4.7, 4.7, None]}

        pregnant = {
            "pregnant_18": [4.7, None],
            "pregnant_19-50": [4.7, None],
            "lactant_18": [5.1, None],
            "lactant_19-50": [5.1, None]
        }

        result = self.get_rda_ul(table, pregnant)
        return result
    
    def selenium_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [15, 15, 45], 
                "7-12m": [20, 20, 60], 
                  "1-3": [20, 20, 90], 
                  "4-8": [30, 30, 150], 
                 "9-13": [40, 40, 280], 
                "14-18": [55, 55, 400],
                "19-30": [55, 55, 400],
                "31-50": [55, 55, 400],
                "51-70": [55, 55, 400],
                  "70<": [55, 55, 400]}

        pregnant = {
            "pregnant_18": [60, 400],
            "pregnant_19-50": [60, 400],
            "lactant_18": [70, 400],
            "lactant_19-50": [70, 400]
        }

        result = self.get_rda_ul(table, pregnant)
        return result

    def zinc_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [2, 2, 4], 
                "7-12m": [3, 3, 5], 
                  "1-3": [3, 3, 7], 
                  "4-8": [5, 5, 12], 
                 "9-13": [8, 8, 23], 
                "14-18": [11, 9, 34],
                "19-30": [11, 8, 40],
                "31-50": [11, 8, 40],
                "51-70": [11, 8, 40],
                  "70<": [11, 8, 40]}

        pregnant = {
            "pregnant_18": [12, 34],
            "pregnant_19-50": [11, 40],
            "lactant_18": [13, 34],
            "lactant_19-50": [12, 40]
        }

        result = self.get_rda_ul(table, pregnant)
        return result




class Vitamins:
    def __init__(self, sex, age, pregnancy):

        self.sex = sex
        self.age = age
        self.pregnancy = pregnancy

        self.stage = age_stage(self.age)
        self.sex_ind = sex_index(self.sex)
        self.preg_lev = pregnancy_level(self.pregnancy, self.age)

        self.vit_a = self.vitamin_a()
        self.vit_b_6 = self.vitamin_b_6()
        self.vit_b_12 = self.vitamin_b_12()
        self.vit_c = self.vitamin_c()
        self.vit_d = self.vitamin_d()
        self.vit_e = self.vitamin_e()
        self.vit_k = self.vitamin_k()

        self.thiamin = self.thiamin_cal()
        self.riboflavin = self.riboflavin_cal()
        self.folate = self.folate_cal()
        self.niacin = self.niacin_cal()
        self.choline = self.choline_cal()
        self.pantot_acid = self.pantot_cal()
        self.biotin = self.biotin_cal()
        self.carot = self.carot_cal()
        


    def get_rda_ul(self, table, pregnant):
        rda = None
        ul = None

        if self.pregnancy:
            rda = pregnant[self.preg_lev][0]
            ul = pregnant[self.preg_lev][1]
        else:
            rda = table[self.stage][self.sex_ind]
            ul = table[self.stage][2]

        
        res = {"rda": rda, "ul": ul}

        return res

    def return_vitamins(self):

        vitamins = {"vitamin_a": self.vit_a, "vitamin_b_6": self.vit_b_6, "vitamin_b_12": self.vit_b_12, "vitamin_c": self.vit_c,
                    "vitamin_d": self.vit_d, "vitamin_e": self.vit_e, "vitamin_k": self.vit_k, "thiamin": self.thiamin, "riboflavin": self.riboflavin,
                    "folate": self.folate, "niacin": self.niacin, "choline": self.choline, "pantothenic_acid": self.pantot_acid,
                    "biotin": self.biotin, "carotenoids": self.carot}

        return vitamins

    def vitamin_a(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [400, 400, 600], 
                "7-12m": [500, 500, 600], 
                  "1-3": [300, 300, 600], 
                  "4-8": [400, 400, 900], 
                 "9-13": [600, 600, 1700], 
                "14-18": [900, 700, 2800],
                "19-30": [900, 700, 3000],
                "31-50": [900, 700, 3000],
                "51-70": [900, 700, 3000],
                  "70<": [900, 700, 3000]}

        pregnant = {
            "pregnant_18": [750, 2800],
            "pregnant_19-50": [770, 3000],
            "lactant_18": [1200, 2800],
            "lactant_19-50": [1300, 3000]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def vitamin_b_6(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.1, 0.1, None], 
                "7-12m": [0.3, 0.3, None], 
                  "1-3": [0.5, 0.5, 30], 
                  "4-8": [0.6, 0.6, 40], 
                 "9-13": [1.0, 1.0, 60], 
                "14-18": [1.3, 1.2, 80],
                "19-30": [1.3, 1.3, 100],
                "31-50": [1.3, 1.3, 100],
                "51-70": [1.7, 1.5, 100],
                  "70<": [1.7, 1.5, 100]}

        pregnant = {
            "pregnant_18": [1.9, 80],
            "pregnant_19-50": [1.9, 100],
            "lactant_18": [2.0, 80],
            "lactant_19-50": [2.0, 100]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def vitamin_b_12(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.4, 0.4, None], 
                "7-12m": [0.5, 0.5, None], 
                  "1-3": [0.9, 0.9, None], 
                  "4-8": [1.2, 1.2, None], 
                 "9-13": [1.8, 1.8, None], 
                "14-18": [2.4, 2.4, None],
                "19-30": [2.4, 2.4, None],
                "31-50": [2.4, 2.4, None],
                "51-70": [2.4, 2.4, None],
                  "70<": [2.4, 2.4, None]}

        pregnant = {
            "pregnant_18": [2.6, None],
            "pregnant_19-50": [2.6, None],
            "lactant_18": [2.8, None],
            "lactant_19-50": [2.8, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def vitamin_c(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [40, 40, None], 
                "7-12m": [50, 50, None], 
                  "1-3": [15, 15, 400], 
                  "4-8": [25, 25, 650], 
                 "9-13": [45, 45, 1200], 
                "14-18": [75, 65, 1800],
                "19-30": [90, 75, 2000],
                "31-50": [90, 75, 2000],
                "51-70": [90, 75, 2000],
                  "70<": [90, 75, 2000]}

        pregnant = {
            "pregnant_18": [80, 1800],
            "pregnant_19-50": [85, 2000],
            "lactant_18": [115, 1800],
            "lactant_19-50": [120, 2000]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def vitamin_d(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [5, 5, 25], 
                "7-12m": [5, 5, 25], 
                  "1-3": [5, 5, 50], 
                  "4-8": [5, 5, 50], 
                 "9-13": [5, 5, 50], 
                "14-18": [5, 5, 50],
                "19-30": [5, 5, 50],
                "31-50": [5, 5, 50],
                "51-70": [10, 10, 50],
                  "70<": [15, 15, 50]}

        pregnant = {
            "pregnant_18": [5, 50],
            "pregnant_19-50": [5, 50],
            "lactant_18": [5, 50],
            "lactant_19-50": [5, 50]
        }

        result = self.get_rda_ul(table, pregnant)

        return result
 
    def vitamin_e(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [4, 4, None], 
                "7-12m": [5, 5, None], 
                  "1-3": [6, 6, 200], 
                  "4-8": [7, 7, 300], 
                 "9-13": [11, 11, 600], 
                "14-18": [15, 15, 800],
                "19-30": [15, 15, 1000],
                "31-50": [15, 15, 1000],
                "51-70": [15, 15, 1000],
                  "70<": [15, 15, 1000]}

        pregnant = {
            "pregnant_18": [15, 800],
            "pregnant_19-50": [15, 1000],
            "lactant_18": [19, 800],
            "lactant_19-50": [19, 1000]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def vitamin_k(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [2.0, 2.0, None], 
                "7-12m": [2.5, 2.5, None], 
                  "1-3": [30, 30, None], 
                  "4-8": [55, 55, None], 
                 "9-13": [60, 60, None], 
                "14-18": [75, 75, None],
                "19-30": [90, 90, None],
                "31-50": [90, 90, None],
                "51-70": [90, 90, None],
                  "70<": [90, 90, None]}

        pregnant = {
            "pregnant_18": [75, None],
            "pregnant_19-50": [90, None],
            "lactant_18": [75, None],
            "lactant_19-50": [90, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result


    def thiamin_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.2, 0.2, None], 
                "7-12m": [0.3, 0.3, None], 
                  "1-3": [0.5, 0.5, None], 
                  "4-8": [0.6, 0.6, None], 
                 "9-13": [0.9, 0.9, None], 
                "14-18": [1.2, 1.0, None],
                "19-30": [1.2, 1.1, None],
                "31-50": [1.2, 1.1, None],
                "51-70": [1.2, 1.1, None],
                  "70<": [1.2, 1.1, None]}

        pregnant = {
            "pregnant_18": [1.4, None],
            "pregnant_19-50": [1.4, None],
            "lactant_18": [1.4, None],
            "lactant_19-50": [1.4, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def riboflavin_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [0.3, 0.3, None], 
                "7-12m": [0.4, 0.4, None], 
                  "1-3": [0.5, 0.5, None], 
                  "4-8": [0.6, 0.6, None], 
                 "9-13": [0.9, 0.9, None], 
                "14-18": [1.3, 1.0, None],
                "19-30": [1.3, 1.1, None],
                "31-50": [1.3, 1.1, None],
                "51-70": [1.3, 1.1, None],
                  "70<": [1.3, 1.1, None]}

        pregnant = {
            "pregnant_18": [1.4, None],
            "pregnant_19-50": [1.4, None],
            "lactant_18": [1.6, None],
            "lactant_19-50": [1.6, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result
  
    def folate_cal(self):
            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [65, 65, None], 
                "7-12m": [80, 80, None], 
                  "1-3": [150, 150, 300], 
                  "4-8": [200, 200, 400], 
                 "9-13": [300, 300, 600], 
                "14-18": [400, 400, 800],
                "19-30": [400, 400, 1000],
                "31-50": [400, 400, 1000],
                "51-70": [400, 400, 1000],
                  "70<": [400, 400, 1000]}

        pregnant = {
            "pregnant_18": [600, 800],
            "pregnant_19-50": [600, 1000],
            "lactant_18": [500, 800],
            "lactant_19-50": [500, 1000]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def niacin_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [2, 2, None], 
                "7-12m": [4, 4, None], 
                  "1-3": [6, 6, 10], 
                  "4-8": [8, 8, 15], 
                 "9-13": [12, 12, 20], 
                "14-18": [16, 14, 30],
                "19-30": [16, 14, 35],
                "31-50": [16, 14, 35],
                "51-70": [16, 14, 35],
                  "70<": [16, 14, 35]}

        pregnant = {
            "pregnant_18": [18, 30],
            "pregnant_19-50": [18, 35],
            "lactant_18": [17, 30],
            "lactant_19-50": [17, 35]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def choline_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [125, 125, None], 
                "7-12m": [150, 150, None], 
                  "1-3": [200, 200, 1000], 
                  "4-8": [250, 250, 1000], 
                 "9-13": [375, 375, 2000], 
                "14-18": [550, 400, 3000],
                "19-30": [550, 425, 3500],
                "31-50": [550, 425, 3500],
                "51-70": [550, 425, 3500],
                  "70<": [550, 425, 3500]}

        pregnant = {
            "pregnant_18": [450, 3000],
            "pregnant_19-50": [450, 3500],
            "lactant_18": [550, 3000],
            "lactant_19-50": [550, 3500]
        }

        result = self.get_rda_ul(table, pregnant)

        return result
    
    def pantot_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [1.7, 1.7, None], 
                "7-12m": [1.8, 1.8, None], 
                  "1-3": [2, 2, None], 
                  "4-8": [3, 3, None], 
                 "9-13": [4, 4, None], 
                "14-18": [5, 5, None],
                "19-30": [5, 5, None],
                "31-50": [5, 5, None],
                "51-70": [5, 5, None],
                  "70<": [5, 5, None]}

        pregnant = {
            "pregnant_18": [6, None],
            "pregnant_19-50": [6, None],
            "lactant_18": [7, None],
            "lactant_19-50": [7, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def biotin_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [5, 5, None], 
                "7-12m": [6, 6, None], 
                  "1-3": [8, 8, None], 
                  "4-8": [12, 12, None], 
                 "9-13": [20, 20, None], 
                "14-18": [25, 25, None],
                "19-30": [30, 30, None],
                "31-50": [30, 30, None],
                "51-70": [30, 30, None],
                  "70<": [30, 30, None]}

        pregnant = {
            "pregnant_18": [30, None],
            "pregnant_19-50": [30, None],
            "lactant_18": [35, None],
            "lactant_19-50": [35, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

    def carot_cal(self):

            #[RDA_male, RDA_female, UL]
        table = {"0-6m": [5, 5, None], 
                "7-12m": [5, 5, None], 
                  "1-3": [5, 5, None], 
                  "4-8": [5, 5, None], 
                 "9-13": [5, 5, None], 
                "14-18": [5, 5, None],
                "19-30": [6, 5, None],
                "31-50": [6, 5, None],
                "51-70": [6, 5, None],
                  "70<": [6, 5, None]}

        pregnant = {
            "pregnant_18": [5, None],
            "pregnant_19-50": [6, None],
            "lactant_18": [5, None],
            "lactant_19-50": [6, None]
        }

        result = self.get_rda_ul(table, pregnant)

        return result

        



class DRICalculations:
    def __init__(self, sex, age, pregnancy, height, weight, activity):
        self.sex = sex
        self.age = age
        self.pregnancy = pregnancy
        self.height = height
        self.h_m = round(self.height / 100, 2)
        self.weight = weight
        self.activity = activity
        
        ## Calculated ones

        self.pal = self.physical_activity_level()
        self.bmi = self.body_mass_index()
        self.eer = self.energy()
        self.dri = self.dietary_reference_intakes()
        self.carbohydrate = 520
        self.t_f = self.total_fiber()
        self.protein = self.protein_cal()
        self.fat = None
        self.sat_fat = None
        self.trans_fat = None
        self.l_acid = self.linolenic_acid()
        self.al_acid = self.a_linolenic_acid()
        self.dietary_cholesterol = None
        self.water = self.total_water()


    
    def physical_activity_level(self):

        if self.activity == "sedentary":
            pal = 1.0
        elif self.activity == "low-active":
            if self.sex == "male":
                if self.age <= 18:
                    pal = 1.13
                else:
                    pal = 1.11
            else:
                if self.age <= 18:
                    pal = 1.16
                else:
                    pal = 1.12
        elif self.activity == "active":
            if self.sex == "male":
                if self.age <= 18:
                    pal = 1.26
                else:
                    pal = 1.25
            else:
                if self.age <= 18:
                    pal = 1.31
                else:
                    pal = 1.27
        else:
            if self.sex == "male":
                if self.age <= 18:
                    pal = 1.42
                else:
                    pal = 1.48
            else:
                if self.age <= 18:
                    pal = 1.56
                else:
                    pal = 1.45

        return pal
    
    
    def body_mass_index(self):
        # weight (kilograms) / height(meters)^2

        bmi = round(self.weight / (self.h_m**2), 1)

        return bmi

        
    def energy(self):

        # Total Energy Expenditure + Energy Deposition
        if 0 <= self.age <= 0.25:
            eer = (89 * self.weight - 100) + 175
        
        elif 0.25 < self.age <= 0.5:
            eer = (89 * self.weight - 100) + 56

        elif 0.5 < self.age <= 1:
            eer = (89 * self.weight - 100) + 22
        
        elif 1 < self.age < 3:
            eer = (89 * self.weight - 100) + 20

        elif 3 <= self.age <= 8:

            if self.sex == "male":
                eer = 88.5 - (61.9 * self.age) + self.pal * ((26.7 * self.weight) + (903 * self.h_m)) + 20
            else:
                eer = 135.3 - (30.8 * self.age) + self.pal * ((10.0 * self.weight) + (934 * self.h_m)) + 20

        elif 8 < self.age <= 18:

            if self.sex == "male":
                eer = 88.5 - (61.9 * self.age) + self.pal * ((26.7 * self.weight) + (903 * self.h_m)) + 25
            else:
                eer = 135.3 - (30.8 * self.age) + self.pal * ((10.0 * self.weight) + (934 * self.h_m)) + 25
        # Total Energy Expenditure
        else:

            if self.sex == "male":
                eer = 662 - (9.53 * self.age) + self.pal * ((15.91 * self.weight) + (539.6 * self.h_m)) 
            else:
                eer = 354 - (6.91 * self.age) + self.pal * ((9.36 * self.weight) + (726 * self.h_m))

        
        if self.pregnancy:
            # Nonpregnant EER + Pregnancy Energy Deposition

            if self.pregnancy == "pregnant-1st-trimester":
                eer = eer + 0
            elif self.pregnancy == "pregnant-2nd-trimester" or self.pregnancy == "pregnant-2nd-trimester-more":
                eer = eer + 340
            elif self.pregnancy == "pregnant-3rd-trimester":
                eer = eer + 452

            # Nonpregnant EER + Milk Energy Output – Weight Loss

            elif self.pregnancy == "lactating-0-6-months":
                eer = eer + 500 - 170
            elif self.pregnancy == "lactating-over-7-months":
                eer = eer + 400 - 0

        eer = round(eer)

        return eer

    
    def dietary_reference_intakes(self): # Sugars and Starches by Life Stage Group

        # (g/day)

        if 0 <= self.age <= 0.5:
            dri = 60 
        elif 0.5 < self.age <= 1:
            dri = 95
        else:
            dri = 110

        if self.pregnancy:
            dri = 170

        return dri
    
    
    def total_fiber(self):
        
        if 0 <= self.age <= 3:
            t_f = 19
        elif 3 < self.age <= 8:
            t_f = 25
        elif 8 < self.age <= 13:
            if self.sex == "male":
                t_f = 31
            else:
                t_f = 25
        elif 13 < self.age <= 50 and self.sex == "male":
            t_f = 38
        elif 13 < self.age <= 50 and self.sex == "female":
            t_f = 25
        else:
            if self.sex == "male":
                t_f = 30
            else:
                t_f = 21
        
        if self.pregnancy:
            t_f = 28


        return t_f
    
    
    def linolenic_acid(self):

        if 0 <= self.age <= 0.5:
            l_a = 4.4
            al_a = 0.5
        elif 0.5 < self.age <= 1:
            l_a = 4.6
            al_a = 0.5
        elif 1 < self.age <= 3:
            l_a = 7
            al_a = 0.7
        elif 3 < self.age <= 8:
            l_a = 10
            al_a = 9
        
        elif 8 < self.age <= 13 and self.sex == "male":
            l_a = 12
            al_a = 12
        elif self.age > 13 and self.sex == "male":
            l_a = 15
            al_a = 1.6
        
        elif self.age > 8 and self.sex == "female":
            l_a = 11
            al_a = 1.1
        
        if self.pregnancy:
            l_a = 13
            al_a = 1.3

        return l_a

    
    def a_linolenic_acid(self):

        if 0 <= self.age <= 0.5:
            l_a = 4.4
            al_a = 0.5
        elif 0.5 < self.age <= 1:
            l_a = 4.6
            al_a = 0.5
        elif 1 < self.age <= 3:
            l_a = 7
            al_a = 0.7
        elif 3 < self.age <= 8:
            l_a = 10
            al_a = 9
        
        elif 8 < self.age <= 13 and self.sex == "male":
            l_a = 12
            al_a = 12
        elif self.age > 13 and self.sex == "male":
            l_a = 15
            al_a = 1.6
        
        elif self.age > 8 and self.sex == "female":
            l_a = 11
            al_a = 1.1
        
        if self.pregnancy:
            l_a = 13
            al_a = 1.3

        return al_a

    
    def protein_cal(self):
        
        if 0 <= self.age <= 0.5:
            protein = 9.1
        elif 0.5 < self.age <= 1:
            protein = 11
        elif 1 < self.age <= 3:
            protein = 13
        elif 3 < self.age <= 8:
            protein = 19
        elif 8 < self.age <= 13:
            protein = 34
        elif 13 < self.age <= 18:
            if self.sex == "male":
                protein = 52
            else:
                protein = 46

        elif 18 < self.age:
            if self.sex == "male":
                protein = 56
            else:
                protein = 46

        if self.pregnancy:
            protein = 71
            

        return protein

    
    def total_water(self):

        if 0 <= self.age <= 0.5:
            water = 0.7
        elif 0.5 < self.age <= 1:
            water = 0.8
        elif 1 < self.age <= 3:
            water = 1.3
        elif 3 < self.age <= 8:
            water = 1.7
        elif 8 < self.age <= 13:
            if self.sex == "male":
                water = 2.4
            else:
                water = 2.1
        elif 13 < self.age <= 18:
            if self.sex == "male":
                water = 3.3
            else:
                water = 2.3
        else:
            if self.sex == "male":
                water = 3.7
            else:
                water = 2.7

        if self.pregnancy:
            if self.pregnancy in ["pregnant-1st-trimester", "pregnant-2nd-trimester", "pregnant-2nd-trimester-more", "pregnant-3rd-trimester"]:
                water = 3.0
            else:
                water = 3.8
    
        return water

    def fat_cal(self):
        if 0 < self.eer <= 1200:
            self.sat_fat = 11
            if self.sex == "male":
                self.fat = 47
            else:
                self.fat = 36
        elif 1200 < self.eer <= 1500:
            self.sat_fat = 12
            if self.sex == "male":
                self.fat = 58
            else:
                self.fat = 55
        elif 1500 < self.eer <= 1800:
            self.sat_fat = 13
            if self.sex == "male":
                self.fat = 70
            else:
                self.fat = 70
        elif 1800 < self.eer <= 2000:
            self.sat_fat = 15
            if self.sex == "male":
                self.fat = 78
            else:
                self.fat = 75
        elif 2000 < self.eer <= 2200:
            self.sat_fat = 16
            if self.sex == "male":
                self.fat = 80
            else:
                self.fat = 80
        else:
            self.sat_fat = 18
            self.fat = 93

        if self.age <= 15:
            self.trans_fat = 1
        else:
            self.trans_fat = 2
    
    def return_results(self):


        vitamins = Vitamins(sex=self.sex, age=self.age, pregnancy=self.pregnancy)
        all_vitamins = vitamins.return_vitamins()

        minerals = Minerals(sex=self.sex, age=self.age, pregnancy=self.pregnancy)
        all_minerals = minerals.return_minerals()

        amino_acids = AminoAcids(sex=self.sex, age=self.age, weight=self.weight, pregnancy=self.pregnancy)
        all_amino_acids = amino_acids.return_amino_acids()

        main_info = {"bmi": self.bmi, "caloric_needs": self.eer, "total_water": self.water}

        if self.age < 15:
            sugar = 24
        else:
            sugar = 36

        self.fat_cal()
        self.dietary_cholesterol = 300


        result = {"carbohydrate": self.carbohydrate,
                  "total_fiber": self.t_f, "protein": self.protein, "fat": self.fat, "sat_fat": self.sat_fat, "trans_fat": self.trans_fat,
                  "l_acid": self.l_acid, "al_acid": self.al_acid, "dietary_cholesterol": self.dietary_cholesterol, "sugar":sugar}


        
        return main_info, result, all_vitamins, all_minerals, all_amino_acids