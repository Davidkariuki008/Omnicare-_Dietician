from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from random import randint

# Create your views here.
def index(request):
    detail_form = forms.DetailForm()
    context = {'form': detail_form, 'message': "0"}


    if request.method == 'POST':
        details_form = forms.DetailForm(request.POST)

        if details_form.is_valid():

            details_form.save(commit=True)


            #business logic here

            name = request.POST.get('name')
            gender = request.POST.get('gender')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            age = request.POST.get('age')
            activity = request.POST.get('activity')

            # print(name)
            # print(gender)
            # print(weight)
            # print(height)
            # print(age)
            # print(activity)

            context['message'] = "1"
            context["name"] = name
            context["gender"] = gender
            context["height"] = height
            context["weight"] = weight
            context["data_1"] = ""
            context["data_2"] = ""
            context["data_3"] = ""
            context["data_4"] = ""
            context["data_5"] = ""

            protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)']
            fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
            vegetable = ['Any vegetable(80g)']
            grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas']
            ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
            taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-calorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']


            w = weight
            h = height
            age = age
            act = activity
            gender = gender





            if gender == 'Male':
                cal = float()
                cal = 88.362 + (13.397*float(w)) + (4.799*float(h)) - (5.677*float(age))
                print (cal)
            elif gender == 'Female':
                cal = float()
                cal = 447.593 + (9.247*float(w)) + (3.098*float(h)) - (4.330*float(age))


            if act == 'Sedentary (little or no exercise)':
                cal = cal*1.2

            elif act == 'Lightly active (1-3 days/week)':
                cal = cal*1.375

            elif act == 'Moderately active (3-5 days/week)':
                cal = cal*1.55

            elif act == 'Very active (6-7 days/week)':
                cal = cal*1.725

            elif act == 'Super active (twice/day)':
                cal = cal*1.9

            print (cal)


            if cal<1500:
                context["data_1"] = "Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)]
                context["data_2"] = "Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]
                context["data_3"] = "Snack: "+ps[randint(0, 4)]+" + "+vegetable[0]
                context["data_4"] = "Dinner: "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]
                context["data_5"] = "Snack: "+fruit[randint(0, 5)]


            elif cal<1800:
                context["data_1"] = "Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]
                context["data_2"] = "Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)]
                context["data_3"] = "Snack: "+ps[randint(0, 4)]+" + "+vegetable[0]
                context["data_4"] = "Dinner: 2 "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]
                context["data_5"] = "Snack: "+fruit[randint(0, 5)]
                

            elif cal<2200:
                context["data_1"] = "Breakfast: "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]
                context["data_2"] = "Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)]
                context["data_3"] = "Snack: "+ps[randint(0, 4)]+" + "+vegetable[0]
                context["data_4"] = "Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]
                context["data_5"] = "Snack: "+fruit[randint(0, 5)]


            elif cal>=2200:
                context["data_1"] = "Breakfast: 2 "+protein[randint(0, 5)]+" + "+fruit[randint(0, 5)]+" + "+grains[randint(0,4)]
                context["data_2"] = "Lunch: "+protein[randint(0, 5)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)]
                context["data_3"] = "Snack: "+ps[randint(0, 4)]+" + "+vegetable[0]
                context["data_4"] = "Dinner: 2 "+protein[randint(0, 5)]+" + 2 "+vegetable[0]+" + Leafy Greens + 2 "+grains[randint(0,4)]+" + 2 "+taste_en[randint(0,5)]
                context["data_5"] = "Snack: "+fruit[randint(0, 5)]








            return render(request,'home/index.html',context=context)







        else:
            context = {'form':details_form, "message":"0"}
            return render(request,'index/contact.html',context=context)


    return render(request, 'home/index.html', context=context)



