from django.conf import settings
from django.http import request
from django.utils.deprecation import MiddlewareMixin
import datetime
import logging
import pytz
import json
import socket
import random
import traceback

from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

logger = logging.getLogger(__name__)

class ReqPreProcessor(MiddlewareMixin):
   def process_request(self, request):
      try:
         # print("request.path_info--:", request.path_info)
         if 'cd' not in request.path_info and 'swagger' not in request.path_info:
            response = Response({"detail": "Not a valid service call"},
                                 content_type="application/json",
                                 status=status.HTTP_401_UNAUTHORIZED)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()

            return response

         curr_time_str = datetime.datetime.strftime(datetime.datetime.now(pytz.timezone(time_zone)), "%d%H%M%S%f") + short_time_zone
         random_str = random.randint(1111,9999)
         track_id = curr_time_str + '.' + str(random_str)

         if str(request.path) != "/":
            # host_name = ''.join(letter for letter in socket.gethostname() if letter.isalnum())
            track_id_prefix = 'ST'
            if request.GET.get('parent_track_id', None) == None:
               if request.body:
                  try:
                     request_data = json.loads(request.body)

                     if isinstance(request_data, list):
                        request_data = request_data[0]

                     if request_data.get('parent_track_id', None) != None:
                        track_id = request_data.get('parent_track_id', None)
                  except:
                     logger.exception(f"Error occured while reading json data: {request.body} - Error: {traceback.format_exc()}")

               print(f"{track_id_prefix + '.' + track_id} *** Track ID - Service Begin: {request.path}")
            else:
               track_id_prefix = request.GET.get('parent_track_id', 'ST')[0:2]

            request.META['xx_track_id'] = track_id_prefix + '.' + track_id

         # print("request.META: ",request.META)
         # print("header:", request.headers, request, "------", request.GET)

      except:
         # print("Error in CS_RequestPreProcessor.process_request:", traceback.format_exc())
         logger.exception(f"Error occured inside ReqPreProcessor - Error: {traceback.format_exc()}")
