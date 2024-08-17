import traceback
from lxml import html
import re
import datetime
import logging

from django_globals import globals
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class RespPostProcessor(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            response['xx_track_id'] = globals.request.META.get('xx_track_id', None)
            response['xx_req_time'] = globals.request.META.get('xx_req_time', None)
            # res_code = str(response.status_code)

            curr_time = datetime.datetime.now()
            response['xx_res_time'] = curr_time
            diff = curr_time - globals.request.META.get('xx_req_time', curr_time)
            response['xx_process_time'] = diff.total_seconds()

            if request.GET.get('parent_track_id', None) == None:
                print(f"{globals.request.META.get('xx_track_id', None)} *** Track ID - Service End: {request.path} Status: {response} - Response Time: {response['xx_process_time']}")

            return response

        except:
            print("Error in CS_ResponsePostProcessor.call:", traceback.format_exc())
            logger.exception(f"API Error in CS_ResponsePostProcessor - call - Error: {traceback.format_exc()}")

            return response
