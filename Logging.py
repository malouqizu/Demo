# -*- coding: utf-8 -*-
#https://blog.csdn.net/wendaomudong_l2d4/article/details/79688551
#https://www.cnblogs.com/zzzhfo/archive/2018/04/08/8745222.html
import logging.config
import logging
import sys

logger = logging.getLogger(__file__)

h1=logging.FileHandler('t1.log')
h2=logging.FileHandler('t2.log')
h3=logging.FileHandler('t3.log')
h4=logging.StreamHandler()

formmater1=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:  %(message)s',datefmt='%Y-%m-%d %H:%M:%S %p')
formmater2=logging.Formatter('%(asctime)s :  %(message)s',datefmt='%Y-%m-%d %H:%M:%S %p')
formmater3=logging.Formatter('%(name)s %(message)s')
formmater4=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',datefmt='%Y-%m-%d %H:%M:%S %p')

h1.setFormatter(formmater1)
h2.setFormatter(formmater2)
h3.setFormatter(formmater3)
h4.setFormatter(formmater4)

h1.setLevel(logging.INFO)
h2.setLevel(logging.WARNING)
h3.setLevel(logging.ERROR)
h4.setLevel(logging.INFO)

logger.addHandler(h1)
logger.addHandler(h2)
logger.addHandler(h3)
logger.addHandler(h4)

i = 0
try:
    m=1/0
except:
    logger.info('info')
    logger.debug('debug')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
    logger.exception(sys.exc_info())



