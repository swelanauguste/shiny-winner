import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Product

PRODUCT_LIST = [
    "panadol",
    "starlight mints",
    "butter toffees",
    "soldanza",
    "ole",
    "classic selects",
    "caramel crunch",
    "pringles",
    "nescafe",
    "green tea",
    "earl grey",
    "angostura chill",
    "ting",
    "schweppes",
    "pinehill orange juice drink",
    "fruta cranberry raspberry",
    "fruta orange carrot",
    "piton malta",
]


class ProductProvider(faker.providers.BaseProvider):
    def product_list(self):
        return self.random_element(PRODUCT_LIST)


class Command(BaseCommand):
    help = "Create fake product"

    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(ProductProvider)
        # print(fake.random_int(min=1, max=5))
        for _ in range(17):
            Product.objects.create(
                name=fake.unique.product_list(),
                price=fake.random_int(min=1, max=5),
                details=fake.sentence(nb_words=10),
            )
        self.stdout.write(self.style.SUCCESS("Successfully created fake products"))
