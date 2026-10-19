from django.shortcuts import redirect, render
from .models import Recipe

# Create your views here.

def recipes(request):
    # This is the page that helps us show recipes and save new ones.
    print("RECIPES VIEW CALLED")

    # If someone sent the form, we need to save the recipe they typed in.
    if request.method == "POST":
        print("FORM SUBMITTED")

        # Get the words from the form and the picture they picked.
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        # Show the recipe details in the server's notebook (the console).
        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        # Put the new recipe into the recipe box (the database).
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            )
        # Send the person back to the recipes page after saving.
        return redirect("/recipes/")
    
    # Get all the recipes already in the recipe box.
    queryset = Recipe.objects.all()
    # Give the recipes to the page so it can show them.
    context = {'recipes': queryset}

    # Show the recipes page with the list of recipes.
    return render(request, "recipes.html", context)
    
