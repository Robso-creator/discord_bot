import logging

import colorlog


def setup_logger(logger_name, level=logging.INFO):
    date_colored = '%(bold_black)s%(asctime)s'
    level_colored = '%(log_color)s%(levelname)7s%(reset)s'
    file_path_colored = '%(purple)s%(filename)s:%(name)s:%(funcName)s%(reset)s'
    formatting = f'{date_colored}   {level_colored}   {file_path_colored} | %(message)s'

    color_formatter = colorlog.ColoredFormatter(
        formatting,
        datefmt='%Y-%m-%d %H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
    )

    handler = colorlog.StreamHandler()
    handler.setFormatter(color_formatter)

    logger = logging.getLogger(logger_name)
    logger.addHandler(handler)
    logger.setLevel(level)

    return logger
