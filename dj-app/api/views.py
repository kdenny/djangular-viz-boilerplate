# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status
import json



result_path = 'C:/Users/kdenny/Documents/djangular-viz-boilerplate/dj-app/api/'

class GetResult(APIView):

    def get(self, request, result_key='0'):

        if result_key != '0':
            result_filename = result_path + 'example.json'
            with open(result_filename) as data_file:
                data = json.load(data_file)['v16'][result_key]
                return Response(data)
        else:
            result_filename = result_path + 'example2.json'
            with open(result_filename) as data_file:
                data = json.load(data_file)
                return Response(data)

