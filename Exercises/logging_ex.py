# import logging modules
import logging
import logging.handlers
import sys

def init_logger():
    # specify logger object
    gw_logger = logging.getLogger(name='gw_log')
    gw_logger.setLevel(logging.DEBUG) # set logger object level

    # specify message formatter
    gw_format = logging.Formatter(
        '[%(asctime)s, %(module)s, line: %(lineno)s, %(levelname)s] %(message)s'
    )

    # set stream handler
    gw_stream_handle = logging.StreamHandler(sys.stdout)
    gw_stream_handle.setLevel(logging.WARNING) # set stream handler level
    gw_stream_handle.setFormatter(gw_format) # set formatter for stream handler
    gw_logger.addHandler(gw_stream_handle) # add handler to logger

    # set file handler
    gw_file_handle = logging.FileHandler('C://OUTPUT/gw_log.log')
    gw_file_handle.setLevel(logging.DEBUG) # set file handler level
    gw_file_handle.setFormatter(gw_format) # set formatter for file handler
    gw_logger.addHandler(gw_file_handle) # add handler to logger

    # set log messages where needed in code
    gw_logger.debug('Debug message here.')
    gw_logger.info('Info message here.')
    gw_logger.warning('Warning message here.')
    gw_logger.error('Error message here.')
    gw_logger.critical('Critical message here.')

def main():
    init_logger()

if __name__ == '__main__':
    main()
