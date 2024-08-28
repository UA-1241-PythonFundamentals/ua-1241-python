import logging

logging.basicConfig(level=logging.ERROR,
                    filename='./lessons/lesson11/app.log',
                    filemode='w',
                    encoding="utf-8",
                    format='%(name)s - %(asctime)s- %(levelname)s - %(funcName)s >> %(message)s')



if __name__ == "__main__":
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')




