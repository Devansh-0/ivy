import ivy
from typing import Union
from ivy.framework_handler import current_framework as _cur_framework


def remainder(x1: ivy.Array, x2: ivy.Array) \
        -> ivy.Array:
    """
    Returns the remainder of division for each element x1_i of the input array x1 and the respective element x2_i of the
     input array x2.

     :param x1: dividend input array. Should have a numeric data type.
     :param x2: divisor input array. Must be compatible with x1 (see Broadcasting). Should have a numeric data type.
     :return: an array containing the element-wise results. Each element-wise result must have the same sign as the
              respective element x2_i. The returned array must have a data type determined by Type Promotion Rules.

    """
    return _cur_framework(x1, x2).remainder(x1, x2)
