from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Recipe

# Create your views here.

def recipes(request):
    print("RECIPES VIEW CALLED")

    if request.method == "POST":
        print("FORM SUBMITTED")

        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )
        #     recipe_name=request.POST.get("recipe_name", "").strip(),
        #     recipe_description=request.POST.get("recipe_description", "").strip(),
        #     recipe_image=request.FILES.get("recipe_image") or "",
        # )

        # messages.success(request, "Recipe added successfully.")
        # return redirect("recipes")

    return render(request, "recipes.html")
    
