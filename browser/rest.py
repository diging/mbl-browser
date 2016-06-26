from django.db.models import Count

from rest_framework import viewsets, filters

from browser.models import *
from browser.serializers import *

import django_filters


class CourseGroupFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='icontains')

    class Meta:
        model = CourseGroup
        fields = ['name', ]


class PersonFilter(filters.FilterSet):
    last_name = django_filters.CharFilter(name='last_name', lookup_type='icontains')
    first_name = django_filters.CharFilter(name='first_name', lookup_type='icontains')
    is_investigator = django_filters.MethodFilter()

    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'is_investigator']

    def filter_is_investigator(self, queryset, value):
        queryset = queryset.annotate(num_investigations=Count('investigator'))
        return queryset.filter(num_investigations__gt=0)


class CourseGroupViewSet(viewsets.ModelViewSet):
    queryset = CourseGroup.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CourseGroupFilter

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return CourseGroupListSerializer
        return CourseGroupDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return CourseListSerializer
        return CourseDetailSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PersonFilter

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return PersonListSerializer
        return PersonDetailSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return InstitutionListSerializer
        return InstitutionDetailSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return LocationListSerializer
        return LocationDetailSerializer
