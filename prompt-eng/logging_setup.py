import logging
import inspect

# Configure logging
logging.basicConfig(
    filename="genai_pipeline.log",  # Log file name
    level=logging.INFO,  # Set logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

def get_class_name():
    """
    Retrieves the name of the class where the function is called.
    """
    stack = inspect.stack()
    for frame in stack:
        if 'self' in frame.frame.f_locals:
            return frame.frame.f_locals['self'].__class__.__name__
    return "UnknownClass"

def log_request(payload):
    """
    Logs the request payload before sending it, along with the class name.
    """
    class_name = get_class_name()
    logger.info("[%s] Request Payload: %s", class_name, payload)

def log_response(time_taken, response):
    """
    Logs only the response and execution time, along with the class name.
    """
    class_name = get_class_name()
    if time_taken == -1:
        logger.error("[%s] Error in response: %s", class_name, response)
    else:
        logger.info("[%s] Response received in %ss: %s", class_name, time_taken, response)