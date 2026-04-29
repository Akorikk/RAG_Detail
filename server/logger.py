import logging 

def setup_logger(name="Medic"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)