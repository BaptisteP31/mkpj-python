import logging

def configure_logging(enable_logging):
    logging.basicConfig(level=logging.DEBUG if enable_logging else logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')