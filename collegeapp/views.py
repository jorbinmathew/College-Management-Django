from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View


class CollegeView(View):
    def get(self, request):
        data = {
            "id": "1",
            "name": "Devagiri College",
            "location": "Kozhikode",
            "university": "University of Calicut",
            "status": "Active"
        }

        return JsonResponse(data)


class StudentView(View):
    def get(self, request):
        data = {
            "id": "1",
            "name": "Anu",
            "course": "BCA",
            "batch": "2023-2026",
            "place": "Kochi"
        }

        return JsonResponse(data)


class TeacherView(View):
    def get(self, request):
        data = {
            "id": "1",
            "name": "Rahul",
            "subject": "Python",
            "experience": "5 Years",
            "qualification": "MCA"
        }

        return JsonResponse(data)


class CourseView(View):
    def get(self, request):
        data = {
            "id": "1",
            "course_name": "Bachelor of Computer Applications",
            "short_name": "BCA",
            "duration": "3 Years",
            "department": "Computer Applications"
        }

        return JsonResponse(data)


class DepartmentView(View):
    def get(self, request):
        data = {
            "id": "1",
            "department_name": "Computer Applications",
            "head": "Dr. Thomas",
            "location": "Main Block",
            "status": "Active"
        }

        return JsonResponse(data)