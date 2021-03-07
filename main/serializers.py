from rest_framework import serializers
from main.models import StudentData

class StudentDataSerializer(serializers.ModelSerializer):
    """
    Serializer class takes request data as input
    Converts django objects to readable json
    """
    sexton_distinction = serializers.SerializerMethodField() # method field to create a pseudo field, not actually in the database

    def get_sexton_distinction(self, obj):
        """'
        fucntion that determines what will be the value of the pseudofield based on specific conditions
        """
        if obj.cgpa:
            if float(obj.cgpa) >= 3.85:
                return 'Sexton Distinction'
            elif float(obj.cgpa) >= 3.70:
                return 'Distinction'
            else:
                return 'Co-op Designation'
    class Meta:
        """
        Contains the metadata info, i.e the name of the model(table) and the fields to be displayed to user
        (Example: we want to display the first name but dont want to display the user password from the user table)
        """
        model = StudentData
        fields = ('first_name', 'last_name', 'idn', 'sexton_distinction',)

class StudentDataPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'