import logging

def setup_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.FileHandler(filename='multimod_log.log')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def main():
    log = setup_logger("default")
    log.info("logging_test started")

if __name__ == "__main__":
    main()
    import submodule

