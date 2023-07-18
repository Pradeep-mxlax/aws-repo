import imp
import factory
from factory.django import  DjangoModelFactory 
from .models import * 


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog  



    name = factory.Fakar(
         "name",
        nb_words=5,
        variable_nb_words=True
    )
    tagline =factory.Fakar(
         "name",
        nb_words=10,
        variable_nb_words=True
    )


b = BlogFactory()





class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker("name")
    email  = factory.Faker(
        "Email"
    )


a =AuthorFactory()