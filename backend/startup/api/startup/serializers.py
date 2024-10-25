
from rest_framework import serializers
from ...models import Startup, Category, Founder, Batch

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = ['id', 'name', 'email']

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'name']

class StartupSerializer(serializers.ModelSerializer):
    founders = serializers.SlugRelatedField(
        many=True, 
        slug_field='name', 
        queryset=Founder.objects.all(),
        required=False
    )
    categories = serializers.SlugRelatedField(
        many=True, 
        slug_field='name', 
        queryset=Category.objects.all(),
        required=False
    )

    class Meta:
        model = Startup
        fields = [
            'name',
            'short_description',
            'description',
            'phase',
            'status',
            'priority',
            'contact_email',
            'linkedin_url',
            'facebook_url',
            'founders',
            'categories',
            'batch',
            'pitch_deck'
        ]

    def create(self, validated_data):
        founders_data = validated_data.pop('founders', [])
        categories_data = validated_data.pop('categories', [])
         
        startup = Startup.objects.create(**validated_data)
         
        for category_name in categories_data:
            category, created = Category.objects.get_or_create(name=category_name)
            startup.categories.add(category)
         
        for founder_name in founders_data:
            first_name, last_name = founder_name.split(" ", 1)   
            founder, created = Founder.objects.get_or_create(first_name=first_name, last_name=last_name)
            startup.founders.add(founder)
        
        return startup