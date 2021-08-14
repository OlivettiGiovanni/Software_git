# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:17:27 2021

@author: Giovanni Olivetti
"""

import numpy as np
import pandas as pd
from lxml import *

page = 'https://www.britannica.com/topic/Nobel-Prize-Winners-by-Year-1856946'
wikitable = pd.read_html(page)

print(len(wikitable))