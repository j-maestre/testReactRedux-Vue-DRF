from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from app.core.utils import generate_random_string

from .models import Travels, Valoration

@receiver(pre_save, sender=Travels)
def add_slug_to_travel_if_not_exists(sender, instance, *args, **kwargs):
    print("----------ADD SLUG TO TRAVEL----------")
    MAXIMUM_SLUG_LENGTH = 200

    if instance and not instance.slug:
        slug = slugify(instance.city)
        unique = generate_random_string()

        if len(slug) > MAXIMUM_SLUG_LENGTH:
            slug = slug[:MAXIMUM_SLUG_LENGTH]

        while len(slug + '-' + unique) > MAXIMUM_SLUG_LENGTH:
            parts = slug.split('-')

            if len(parts) == 1:
                # The slug has no hypens. To append the unique string we must
                # arbitrarly remove `len(unique)` characters from the end of
                # `slug`. Subtract one to account for extra hyphen.
                slug = slug[:MAXIMUM_SLUG_LENGTH - len(unique) - 1]
            else:
                slug = '-'.join(parts[:-1])

        instance.slug = slug + '-' + unique


@receiver(pre_save, sender=Valoration)
def add_slug_to_valoration_if_not_exists(sender, instance, *args, **kwargs):
    print("*************CREANDO SLUG VALORATION*************")
    # print(instance.author)
    MAXIMUM_SLUG_LENGTH = 200

    if instance and not instance.slug:
        slug = slugify(instance.author)
        unique = generate_random_string()

        if len(slug) > MAXIMUM_SLUG_LENGTH:
            slug = slug[:MAXIMUM_SLUG_LENGTH]

        while len(slug + '-' + unique) > MAXIMUM_SLUG_LENGTH:
            parts = slug.split('-')

            if len(parts) == 1:
                # The slug has no hypens. To append the unique string we must
                # arbitrarly remove `len(unique)` characters from the end of
                # `slug`. Subtract one to account for extra hyphen.
                slug = slug[:MAXIMUM_SLUG_LENGTH - len(unique) - 1]
            else:
                slug = '-'.join(parts[:-1])

        instance.slug = slug + '-' + unique