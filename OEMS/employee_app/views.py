from django.shortcuts import render

# Create your views here.


def index(requests):
    return render(requests, "index.html")


def all_emp(requests):
    return render(requests, "all_emp.html")


def add_emp(requests):
    return render(requests, "add_emp.html")


def remove_emp(requests):
    return render(requests, "remove_emp.html")


def filter_emp(requests):
    return render(requests, "filter_emp.html")
