from django.shortcuts import redirect, render
from .models import Recipe
from django.contrib import messages

# Create your views here.

def recipes(request):
    # This is the page that helps us show recipes and save new ones.
    print("RECIPES VIEW CALLED")

    # If someone sent the form, we need to save the recipe they typed in.
    if request.method == "POST":
        print("FORM SUBMITTED")

        # Get the words from the form and the picture they picked.
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get("recipe_image")

        # # Show the recipe details in the server's notebook (the console).
        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)

        # Put the new recipe into the recipe box (the database).
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            )
        messages.success(request, "Recipe is added Successfully!!")
        # Send the person back to the recipes page after saving.
        return redirect("/recipes/")


    # Get all the recipes already in the recipe box.
    queryset = Recipe.objects.all()
    # Give the recipes to the page so it can show them.
    context = {'recipes': queryset}

    # Show the recipes page with the list of recipes.
    return render(request, "recipes.html", context)

# request → receives the information Django passes to the function.
def delete_recipe(request, id ):
    recipe = Recipe.objects.get(id = id)
    #delete the image file from media/recipe/
    if recipe.recipe_image:
        recipe.recipe_image.delete(save = False)

    # Delete the recipe from the database
    recipe.delete()

    # Here, request lets Django connect the success message to the current request so it can display it after the redirect.
    messages.success(request, "Recipe deleted successfully!")

    return redirect("/recipes/")

# edit function
def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == "POST":
        print("FILES:",request.FILES)
        print("NEW IMAGE:", request.FILES.get("recipe_image"))
        
        data = request.POST
        recipe.recipe_name = data.get("recipe_name")
        recipe.recipe_description = data.get("recipe_description")

            # get the newly uploaded image
        new_image = request.FILES.get("recipe_image")

        if new_image:
            recipe.recipe_image = new_image

        recipe.save()

        messages.success(request, "Recipe updated Successfully!")
        return redirect("/recipes/")
    # go to recipes.html page

    return render(request,"edit_recipe.html ",{"recipe":recipe})
# Here, Django sends the recipe object to the edit_recipe.html so it can display the existing details.
        
