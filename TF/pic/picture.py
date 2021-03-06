# coding: utf-8
import input_data
import tensorflow as tf

# 读取数据
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
# x的folder
x = tf.placeholder(tf.float32, [None, 784])
# W和b是变量
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
# y是求出的softmax
y = tf.nn.softmax(tf.matmul(x, W) + b)
# 再来一个数据里自带的
y_ = tf.placeholder(tf.float32, [None, 10])
# 交叉验证
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()

# 初始化变量
tf.global_variables_initializer().run()
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    # 只需要喂place_folder
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
