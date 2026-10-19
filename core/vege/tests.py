from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from .models import Receipe


class RecipeViewTests(TestCase):
    def setUp(self):
        self.media_dir = TemporaryDirectory()
        self.addCleanup(self.media_dir.cleanup)
        media_override = override_settings(MEDIA_ROOT=self.media_dir.name)
        media_override.enable()
        self.addCleanup(media_override.disable)

    def test_home_page_recipe_link_resolves(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/recipes/"')

    def test_recipe_submission_saves_text_and_uploaded_image(self):
        image = SimpleUploadedFile(
            "recipe.jpg",
            b"test image contents",
            content_type="image/jpeg",
        )

        response = self.client.post(
            "/recipes/",
            {
                "recipe_name": "Tomato soup",
                "recipe_description": "A simple soup",
                "recipe_image": image,
            },
        )

        self.assertRedirects(response, "/recipes/")
        recipe = Receipe.objects.get(recipe_name="Tomato soup")
        self.assertEqual(recipe.recipe_description, "A simple soup")
        self.assertTrue(recipe.recipe_image.name.startswith("recipe/"))
        self.assertTrue(recipe.recipe_image.storage.exists(recipe.recipe_image.name))

    def test_recipe_submission_without_image_succeeds(self):
        response = self.client.post(
            "/recipes/",
            {
                "recipe_name": "Garden salad",
                "recipe_description": "Fresh vegetables",
            },
        )

        self.assertRedirects(response, "/recipes/")
        recipe = Receipe.objects.get(recipe_name="Garden salad")
        self.assertFalse(recipe.recipe_image)
