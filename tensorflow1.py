#import tensorflow as tf
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']= '2'
#hello = tf.constant("Hello, TensorFlow!")
#sess = tf.compat.v1.Session()
#print(sess.run(hello))
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)
print(tf.keras.__version__)

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()