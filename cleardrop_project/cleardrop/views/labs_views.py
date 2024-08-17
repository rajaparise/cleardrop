import base64
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

import logging
import json

logger = logging.getLogger(__name__)

class LabsViewSet(ViewSet):
    swagger_schema = None

    @action(methods=['post'], detail=False, url_path=r'upload', url_name='labs')
    def send_metrics_pbsb(self, request):
        print("Start")

        request_dict = json.loads(request.body)
        # cs_log_message(f"send_metrics_pbsb - request_dict: {request_dict}", logger, loggable=True)
        
        if request_dict.get('message', None) is None:
            msg_data = request_dict
        else:
            encoded = request_dict['message']['data']
            msg_data = json.loads(base64.b64decode(encoded).decode())

        # if isinstance(msg_data, dict):
        #     cs_log_message(f"send_metrics_pbsb - msg_data: {msg_data} - type: {type(msg_data)}", logger, loggable=True)
        #     res = send_pricing_to_bq(msg_data=msg_data)
        #     return Response(res)
        
        return Response(None)
    