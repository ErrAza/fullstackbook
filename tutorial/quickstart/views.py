from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, EmployeeSerializer, ProjectSerializer
from .models import Employee, Project
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
        instance_id = instance.id

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"Success": "Deleted Employee {0}.".format(instance_id)})


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

####################################
#          Template Views          #
####################################


class IndexView(TemplateView):
    """
    Index View
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        """
        Get context data
        """
        employees = Employee.objects.all()
        projects = Project.objects.all()
        context = {
            'employees': employees,
            'projects': projects
        }
        return context


class ProjectView(TemplateView):
    """
    Project View
    """
    template_name = 'project.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        """
        Get context data
        """
        employees = Employee.objects.all()
        projects = Project.objects.all()
        context = {
            'employees': employees,
            'projects': projects
        }
        return context


class EmployeeView(TemplateView):
    """
    Employee View
    """
    template_name = 'employee.html'

    def get_context_data(self, **kwargs):
        """
        Get context data
        """
        employee = get_object_or_404(Employee, id=self.kwargs['employee'])
        projects = Project.objects.filter(employees=employee)
        context = {
            'employee': employee,
            'projects': projects
        }

        return context
