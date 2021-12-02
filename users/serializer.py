from django.db.models import fields
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# class Rsvp_AEROCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_AEROCLUB
#         fields = '__all__'
        
# class Rsvp_AICLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_AICLUB
#         fields = '__all__'

# class Rsvp_ALCHERCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_ALCHERCLUB
#         fields = '__all__'

# class Rsvp_ASTROCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_ASTROCLUB
#         fields = '__all__'

# class Rsvp_BT_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_BT
#         fields = '__all__'

# class Rsvp_CACLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CACLUB
#         fields = '__all__'

# class Rsvp_CCDCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CCDCLUB
#         fields = '__all__'

# class Rsvp_CE_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CE
#         fields = '__all__'

# class Rsvp_CH_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CH
#         fields = '__all__'

# class Rsvp_CL_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CL
#         fields = '__all__'

# class Rsvp_CODINGCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CODINGCLUB
#         fields = '__all__'

# class Rsvp_CSE_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_CSE
#         fields = '__all__'
# class Rsvp_DES_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_DES
#         fields = '__all__'

# class Rsvp_ECE_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_ECE
#         fields = '__all__'
        
# class Rsvp_EDCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_EDCLUB
#         fields = '__all__'

# class Rsvp_EECLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_EECLUB
#         fields = '__all__'

# class Rsvp_EEE_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_EEE
#         fields = '__all__'

# class Rsvp_FNCCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_FNCCLUB
#         fields = '__all__'

# class Rsvp_MA_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_MA
#         fields = '__all__'

# class Rsvp_ME_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_ME
#         fields = '__all__'

# class Rsvp_OTHERCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_OTHERCLUB
#         fields = '__all__'

# class Rsvp_PH_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_PH
#         fields = '__all__'

# class Rsvp_PRAKRITICLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_PRAKRITICLUB
#         fields = '__all__'

# class Rsvp_ROBOTICSCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_ROBOTICSCLUB
#         fields = '__all__'

# class Rsvp_SAILCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_SAILCLUB
#         fields = '__all__'

# class Rsvp_SWC_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_SWC
#         fields = '__all__'

# class Rsvp_Task_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_Task
#         fields = '__all__'

# class Rsvp_TechnicheCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_TechnicheCLUB
#         fields = '__all__'
        
# class Rsvp_UGCLUB_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_models.Rsvp_UGCLUB
#         fields = '__all__'
