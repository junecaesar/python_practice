import tensorflow as tf

a = tf.constant([[2,3]],name = "a")
b = tf.constant([[1],[4]],name = "b")
result = tf.matmul(a,b,name="mul")
print("The result is:\n",result)

#c = tf.constant([2.0,3.0],name="c",shape=(2,0),dtype="float64")
c=tf.zeros([2,2],tf.float32)
print("The tensor is :\n",c)