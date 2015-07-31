__author__ = 'john'

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from appstarter.utils import JsonResponseSerializer

class ResponseParcel(object):
    data = {}
    list = []
    error = False
    message = ""
    uri = ""

    def __init__(self):
        pass

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.get_data()

    def set_list(self, data_list):
        self.list = data_list

    def set_message(self, message):
        self.message = message

    def has_error(self):
        self.error = True

    def set_uri(self, uri):
        self.uri = uri

    def to_json(self):
        json = JsonResponseSerializer.JsonResponseSerializer()
        return HttpResponse(json.to_json(self), content_type="application/json")

    def data_to_json(self):
        json = JsonResponseSerializer.JsonResponseSerializer()
        return HttpResponse(json.to_json(self.data), content_type="application/json")

    def redirect(self):
        return HttpResponseRedirect(self.uri, self.data)

    def render(self, request):
        return render(request, self.uri, self.data)
