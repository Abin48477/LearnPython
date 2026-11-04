from django.shortcuts import redirect, render
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# UserCreationForm — Django's built-in form for creating a user account. It handles password validation and secure password hashing through Django's authentication system.

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

    # Get search text from the URL meaning get that data sent through the URL
    search_query = request.GET.get("search", "")
    # .get("search", "") = find the item named search; if it's missing, give me an empty string.

    # Get all recipes from the database
    queryset = Recipe.objects.all()

    # Filter recipes if the user searches
    if search_query:
        queryset = queryset.filter(recipe_name__icontains=search_query)
# recipe_name__icontains
# Means: "Look inside the recipe name and find text that contains the word I'm searching for. Ignore uppercase and lowercase differences."
   
    # send the results to the recipes.HTML file
    return render(request, "recipes.html",{
        "recipes": queryset,
        "search_query": search_query
    })

    # # Get all the recipes already in the recipe box.
    # queryset = Recipe.objects.all()
    # # Give the recipes to the page so it can show them.
    # context = {'recipes': queryset}
# context = {'recipes': queryset} and "recipes": queryset do the same job here. The dictionary can be created in a separate variable or written directly inside render().
    # # Show the recipes page with the list of recipes.
    # return render(request, "recipes.html", context)

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


def register(request):
    # if post
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #if valid
        if form.is_valid():
            user = form.save()
            print('USER CREATED:',user.username)
            return redirect("/login/")
        
        else:
            print("REGISTRATION ERRORS:" , form.errors)
    else:
        #if get
        form = UserCreationForm()

    return render(request, "register.html",{
       "form":form
   })
# Understand it simply
# 1. def register(request): — creates a view that handles requests to the registration page.
# 2. form = UserCreationForm() — creates an empty registration form.
# 3. render(...) — sends that form to register.html so the browser can display it.
# 4. "form": form — passes the form to the HTML template.

# 1. Create the function
def user_login(request):
# 2. Check whether the user submitted the form
    if request.method == "POST":
        # 3. Receive the submitted information
        form = AuthenticationForm(request, data = request.POST)
        # 4. Check the username and password
        if form.is_valid():
            # 5. Get the authenticated user
            user = form.get_user()
            # 6. Actually log the user in
            login(request, user)#Django creates an authenticated session for that user.
# After successful login, the user goes to your recipes page.
            return redirect("/recipes/")
        else:
            print("LOGIN ERREORS:" , form.errors)
            

    else:
        # 8. Display an empty form for GET requests
        form = AuthenticationForm()#When someone first visits the login page, Django creates an empty login form.

# This displays the login page. If the submitted credentials are invalid, the form is displayed again with errors.
    return render(request, "login.html", {
        "form": form
    })