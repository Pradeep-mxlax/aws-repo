# from attr import fields
from rest_framework import serializers
from .models import * 


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields = '__all__'




class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = '__all__'
   



class EntrySerializers(serializers.ModelSerializer):
    class Meta:
        model= Entry
        fields = '__all__'


# class AssigmentDataSerializer(serializers.ModelSerialize):
#     class Meta:
#         model=AssigmentData
#         exclude = ('created_at', 'updated_at' )
#         # fields='__all__'



# class AssignmentSerializer(AssigmentDataSerializer):

#     class Meta:
#         model= Assignment
#         fields=['name', 'reviewer', 'blind_review', 'start_date', 'end_date', 'recurrence', 
#         'channels', 'filters', 'refkey', 'status', 'created_at', 'updated_at']





