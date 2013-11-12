import logging
logging.basicConfig(filename='logging_test.log', format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)
logging.info("Test1")
logging.info("Test2")
logging.debug("Test3")
logging.warning("Test4")
logging.warning("Test5")
