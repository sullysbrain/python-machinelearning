# Python sandbox file for testing code snippets
import sys
import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__file__)


def mymainmethod(x):
    logger.info(f'root called with {type(x)}')

#Experimentation with Sets
x1 = {1, 2, 3}
x2 = {"dog", "books", 2}
x = x1.union(x2)
mymainmethod(x)

