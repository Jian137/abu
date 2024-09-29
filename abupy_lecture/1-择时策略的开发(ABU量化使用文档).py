# 基础库导入，注意第一次运行时会比较慢，要做数据的解压等处理操作
from __future__ import print_function
from __future__ import division

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
import sys
# 使用insert 0即只使用github，避免交叉使用了pip安装的abupy，导致的版本不一致问题
sys.path.insert(0, os.path.abspath('../'))
sys.path.append("./")
import abupy

# 使用沙盒数据，目的是和书中一样的数据环境
abupy.env.enable_example_env_ipython()


from abupy import ABuSymbolPd
ABuSymbolPd.make_kl_df('usJD') is None


abupy.env.disable_example_env_ipython()
# 关闭沙盒数据
us_jd = ABuSymbolPd.make_kl_df('usJD')

# 再次开启沙盒环境，本节的示例都是在沙盒数据环境下运行
abupy.env.enable_example_env_ipython()
tail = None
if us_jd is not None:
    tail = us_jd.tail()
tail