import tensorflow as tf

xdata = [1,2,3,4,5,6,7]
ydata = [25000,55000,75000,110000,128000,155000,180000]
w = tf.Variable(tf.random_uniform([1], -100, 100))
b = tf.Variable(tf.random_uniform([1], -100, 100))
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
h = w + x + b
cost = tf.reduce_mean(tf.square(h-y))
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Sessin()
sess.run(init)
for i in range(5001):
    sess.fun(train, feed_dict={x: xdata, y: ydata})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict={x: xdata, y: ydata}), sess.run(w),sess.run(b))
    print(sess.run(h, feed_dict={x: [8]}))
