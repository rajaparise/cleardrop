from datetime import datetime
import logging
import socket
import random
import os

from logging import Filter, LogRecord

logger = logging.getLogger(__name__)

LOGGER_EXCLUDE_URI = ['/admin', '/favicon.ico', '/docs/swagger']

def getTrack_id():
    try:
        curr_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
        random_str = random.randint(11111111,99999999)
        uniq_id = socket.gethostname() + "." + str(os.getpid()) +"." + curr_time + "." + str(random_str)
        return uniq_id
    except Exception as e:
        logger.exception("Error occured inside getTrack_id")
        return curr_time

class TrackId(Filter):
    def filter(self, record: LogRecord) -> bool:
      try:
        """
        Determines that the specified record is to be logged.
        From the docs:
                Is the specified record to be logged? Returns 0 for no, nonzero for
                yes. If deemed appropriate, the record may be modified in-place.
        :param record: Log record
        :return: True
        """
        if hasattr(globals, 'request') and 'xx_track_id' in globals.request.META:
            record.track_id = globals.request.META['xx_track_id']
        else:
            record.track_id = "SYSTEM_MESSAGES"   #getTrack_id()
        return True
      except:
        logger.exception("error occured inside TrackId")
        record.track_id = "ERROR_MESSAGES"
        return True


class P_TrackId(Filter):
    def filter(self, record: LogRecord) -> bool:
      try:
        """
        Determines that the specified record is to be logged.
        From the docs:
                Is the specified record to be logged? Returns 0 for no, nonzero for
                yes. If deemed appropriate, the record may be modified in-place.
        :param record: Log record
        :return: True
        """
        if hasattr(globals, 'request') and 'p_xx_track_id' in globals.request.META:
            record.p_track_id = globals.request.META['p_xx_track_id']
        else:
            record.p_track_id = "-"   #getTrack_id()
        return True
      except:
        logger.exception("error occured inside TrackId")
        record.p_track_id = "ERROR_MESSAGES"
        return True
