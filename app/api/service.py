import os
import httpx

LABEL_SERVICE_HOST_URL = 'http://localhost:8020/api/v1/labels/'

def is_label_present(label_id: int):
    return True