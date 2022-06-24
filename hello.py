'''
Author: FeiPF2020 wpfn218925@163.com
Date: 2022-06-25 02:11:20
LastEditors: FeiPF2020 wpfn218925@163.com
LastEditTime: 2022-06-25 02:13:39
FilePath: \seuProject\ch1\hello.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from ensurepip import version
from platform import python_compiler
import py_compile
import numpy as np
import torch

m = np.array([[2,3,4],[5,6,7]])
n = torch.tensor(m)
print(n,n.dtype)

print("hello wpf")
print(version(python_compiler()))