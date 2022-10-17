import logging
import time

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tsleep = req.params.get('sleep')

    time.sleep(int(tsleep))
    return func.HttpResponse(f"Slept for {tsleep} seconds.")
