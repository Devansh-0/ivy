import tensorflow as tf
from tensorflow.python.types.core import Tensor
import ivy


def remainder(x1, x2: Tensor) -> Tensor:
    return tf.math.floormod(x1, x2)
