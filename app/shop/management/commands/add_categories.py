import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category

CATEGORY_LIST = [
    "drinks",
    "sweets",
    "mint",
    "water",
    "chips",
    "coffee",
    "tea",
    "juice",
]


class CategoryProvider(faker.providers.BaseProvider):
    def category_list(self):
        return self.random_element(CATEGORY_LIST)


class Command(BaseCommand):
    help = "Create fake categories"

    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(CategoryProvider)
        print(fake.unique.category_list())
        for _ in range(8):
            Category.objects.create(name=fake.unique.category_list())
        self.stdout.write(self.style.SUCCESS("Successfully created fake categories"))
