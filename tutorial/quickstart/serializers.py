from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Employee, Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User Class
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Group Class
    """
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee Class
    """

    group = GroupSerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_title', 'group', 'user']

    def create(self, validated_data):
        """
        Create method handles POST events
        """
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        job_title = validated_data.get('job_title')

        user = validated_data.get('user')
        group = validated_data.get('group')

        instance = Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
            user=user,
            group=group
        )

        return instance

    def update(self, instance, validated_data):
        """
        Create method handles PATCH/PUT events
        """
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        job_title = validated_data.get('job_title')

        user = validated_data.get('user')
        group = validated_data.get('group')

        instance.first_name = first_name
        instance.last_name = last_name
        instance.job_title = job_title
        instance.user = user
        instance.group = group

        instance.save()

    def to_representation(self, instance):
        representation = {
            "id": instance.id,
            "full name": instance.first_name + " " + instance.last_name,
            "job title": instance.job_title,
            "group": GroupSerializer(instance.group, context={
                'request': self.context['request']}).data,
            "user": UserSerializer(instance.user, context={
                'request': self.context['request']}).data
        }

        return representation


class ProjectEmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project's Employee
    """
    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    group = GroupSerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'job_title', 'group', 'user']


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project Class
    """
    employees = ProjectEmployeeSerializer(required=False, many=True)

    class Meta:
        model = Project
        fields = ['name', 'duration', 'is_active', 'employees']

    def create(self, validated_data):
        employee_list = validated_data.get('employees')

        employee_list_set = []
        if employee_list:
            for employee in employee_list:
                _id = employee.get('id')
                if _id:
                    employee_list_set.append(Employee.objects.get(id=_id))
                elif employee.get('first_name'):
                    employee_list_set.append(Employee.objects.get(first_name=employee.get('first_name'),
                                                                  last_name=employee.get('last_name')))

        instance = Project.objects.create(
            name=validated_data.get('name'),
            duration=validated_data.get('duration'),
            is_active=validated_data.get('is_active'),
        )

        instance.employees.set(employee_list_set)

        return instance



