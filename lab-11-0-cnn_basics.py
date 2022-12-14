{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 3, 3, 1)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x10db29e10>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAQ8AAAD8CAYAAABpXiE9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAADghJREFUeJzt3X+snmV9x/H3ZxQqUWaLRWlKFckaO+eWiCeIuphmaoKN\noUtkCf4hYDRnOsl00WSoCSYmy9Q/XGYwkgaJsBgkE6PHpcYg4HBZYBxJoRRSaUkWWjtAsEWiU8q+\n++PcmMfj+dXruc/zPAffr+TJc933fZ37+vZq8+n9s01VIUkn6w/GXYCktcnwkNTE8JDUxPCQ1MTw\nkNTE8JDUZKjwSHJmkluTPNx9b1yk33NJ9nafmWHGlDQZMsxzHkk+DzxVVZ9NchWwsar+foF+z1TV\nS4aoU9KEGTY8DgA7qupoks3AD6rqNQv0MzykF5hhw+NYVW3o2gF+9vzyvH4ngL3ACeCzVfWtRfY3\nDUwDvPjFL37D9u3bm2t7oXvuuefGXcLEe/bZZ8ddwsTbv3//T6vqrJafXbdchyTfB85eYNOnBheq\nqpIslkSvqqojSc4Dbk+yr6oOze9UVbuB3QBTU1M1Ozu77C/g99WxY8fGXcLEe+yxx8ZdwsTbvn37\nf7f+7LLhUVVvX2xbkseSbB44bXl8kX0c6b4fSfID4PXA74SHpLVj2Fu1M8DlXfty4NvzOyTZmGR9\n194EvAV4cMhxJY3ZsOHxWeAdSR4G3t4tk2QqyXVdnz8GZpPcB9zB3DUPw0Na45Y9bVlKVT0JvG2B\n9bPAB7r2fwJ/Osw4kiaPT5hKamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4\nSGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhI\namJ4SGpieEhq0kt4JLkoyYEkB5NctcD29Ulu7rbfneTcPsaVND5Dh0eSU4AvAe8EXgu8J8lr53V7\nP/Czqvoj4J+Azw07rqTx6uPI4wLgYFU9UlW/Br4O7JrXZxdwQ9f+BvC2JOlhbElj0kd4bAEeHVg+\n3K1bsE9VnQCOAy/rYWxJYzJRF0yTTCeZTTL7xBNPjLscSUvoIzyOAFsHls/p1i3YJ8k64KXAk/N3\nVFW7q2qqqqbOOuusHkqTtFr6CI97gG1JXp3kNOBSYGZenxng8q59CXB7VVUPY0sak3XD7qCqTiS5\nEvgecApwfVXtT/IZYLaqZoCvAP+S5CDwFHMBI2kNGzo8AKpqD7Bn3rqrB9r/C/xVH2NJmgwTdcFU\n0tpheEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhI\namJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGpieEhqYnhIamJ4SGrSS3gk\nuSjJgSQHk1y1wPYrkjyRZG/3+UAf40oan3XD7iDJKcCXgHcAh4F7ksxU1YPzut5cVVcOO56kydDH\nkccFwMGqeqSqfg18HdjVw34lTbChjzyALcCjA8uHgTcu0O/dSd4K/Bj4u6p6dH6HJNPANMDLX/5y\nbrvtth7Ke2E6cODAuEuYeIcOHRp3CS9oo7pg+h3g3Kr6M+BW4IaFOlXV7qqaqqqpDRs2jKg0SS36\nCI8jwNaB5XO6db9RVU9W1a+6xeuAN/QwrqQx6iM87gG2JXl1ktOAS4GZwQ5JNg8sXgw81MO4ksZo\n6GseVXUiyZXA94BTgOuran+SzwCzVTUD/G2Si4ETwFPAFcOOK2m8+rhgSlXtAfbMW3f1QPsTwCf6\nGEvSZPAJU0lNDA9JTQwPSU0MD0lNDA9JTQwPSU0MD0lNDA9JTQwPSU0MD0lNDA9JTQwPSU0MD0lN\nDA9JTQwPSU0MD0lNDA9JTQwPSU0MD0lNDA9JTQwPSU0MD0lNDA9JTQwPSU0MD0lNDA9JTQwPSU16\nCY8k1yd5PMkDi2xPki8mOZjk/iTn9zGupPHp68jjq8BFS2x/J7Ct+0wDX+5pXElj0kt4VNWdwFNL\ndNkF3Fhz7gI2JNncx9iSxmNU1zy2AI8OLB/u1v2WJNNJZpPMHjt2bESlSWoxURdMq2p3VU1V1dSG\nDRvGXY6kJYwqPI4AWweWz+nWSVqjRhUeM8Bl3V2XC4HjVXV0RGNLWgXr+thJkpuAHcCmJIeBTwOn\nAlTVtcAeYCdwEPgF8L4+xpU0Pr2ER1W9Z5ntBXy4j7EkTYaJumAqae0wPCQ1MTwkNTE8JDUxPCQ1\nMTwkNTE8JDUxPCQ1MTwkNTE8JDUxPCQ1MTwkNTE8JDUxPCQ1MTwkNTE8JDUxPCQ1MTwkNTE8JDUx\nPCQ1MTwkNTE8JDUxPCQ1MTwkNTE8JDUxPCQ1MTwkNeklPJJcn+TxJA8ssn1HkuNJ9nafq/sYV9L4\n9PIfXQNfBa4Bblyizw+r6l09jSdpzHo58qiqO4Gn+tiXpLWhryOPlXhTkvuAnwAfr6r98zskmQam\nAU4//XSuueaaEZa3tuzbt2/cJUy8Q4cOjbuEF7RRhce9wKuq6pkkO4FvAdvmd6qq3cBugI0bN9aI\napPUYCR3W6rq6ap6pmvvAU5NsmkUY0taHSMJjyRnJ0nXvqAb98lRjC1pdfRy2pLkJmAHsCnJYeDT\nwKkAVXUtcAnwoSQngF8Cl1aVpyXSGtZLeFTVe5bZfg1zt3IlvUD4hKmkJoaHpCaGh6QmhoekJoaH\npCaGh6QmhoekJoaHpCaGh6QmhoekJoaHpCaGh6QmhoekJoaHpCaGh6QmhoekJoaHpCaGh6Qmhoek\nJoaHpCaGh6QmhoekJoaHpCaGh6QmhoekJoaHpCaGh6QmQ4dHkq1J7kjyYJL9ST6yQJ8k+WKSg0nu\nT3L+sONKGq8+/qPrE8DHqureJGcAP0pya1U9ONDnncC27vNG4Mvdt6Q1augjj6o6WlX3du2fAw8B\nW+Z12wXcWHPuAjYk2Tzs2JLGp9drHknOBV4P3D1v0xbg0YHlw/xuwEhaQ/o4bQEgyUuAW4CPVtXT\njfuYBqYBTj/99L5Kk7QKejnySHIqc8Hxtar65gJdjgBbB5bP6db9lqraXVVTVTW1fv36PkqTtEr6\nuNsS4CvAQ1X1hUW6zQCXdXddLgSOV9XRYceWND59nLa8BXgvsC/J3m7dJ4FXAlTVtcAeYCdwEPgF\n8L4expU0RkOHR1X9B5Bl+hTw4WHHkjQ5fMJUUhPDQ1ITw0NSE8NDUhPDQ1ITw0NSE8NDUhPDQ1IT\nw0NSE8NDUhPDQ1ITw0NSE8NDUhPDQ1ITw0NSE8NDUhPDQ1ITw0NSE8NDUhPDQ1ITw0NSE8NDUhPD\nQ1ITw0NSE8NDUhPDQ1ITw0NSE8NDUpOhwyPJ1iR3JHkwyf4kH1mgz44kx5Ps7T5XDzuupPFa18M+\nTgAfq6p7k5wB/CjJrVX14Lx+P6yqd/UwnqQJMPSRR1Udrap7u/bPgYeALcPuV9JkS1X1t7PkXOBO\n4HVV9fTA+h3ALcBh4CfAx6tq/wI/Pw1Md4uvAx7orbh+bAJ+Ou4iBljP0iatHpi8ml5TVWe0/GBv\n4ZHkJcC/A/9QVd+ct+0Pgf+rqmeS7AT+uaq2LbO/2aqa6qW4nkxaTdaztEmrByavpmHq6eVuS5JT\nmTuy+Nr84ACoqqer6pmuvQc4NcmmPsaWNB593G0J8BXgoar6wiJ9zu76keSCbtwnhx1b0vj0cbfl\nLcB7gX1J9nbrPgm8EqCqrgUuAT6U5ATwS+DSWv58aXcPtfVt0mqynqVNWj0weTU119PrBVNJvz98\nwlRSE8NDUpOJCY8kZya5NcnD3ffGRfo9N/CY+8wq1HFRkgNJDia5aoHt65Pc3G2/u3u2ZVWtoKYr\nkjwxMC8fWMVark/yeJIFn8HJnC92td6f5PzVquUkahrZ6xErfF1jpHO0aq+QVNVEfIDPA1d17auA\nzy3S75lVrOEU4BBwHnAacB/w2nl9/ga4tmtfCty8yvOykpquAK4Z0e/TW4HzgQcW2b4T+C4Q4ELg\n7gmoaQfwbyOan83A+V37DODHC/x+jXSOVljTSc/RxBx5ALuAG7r2DcBfjqGGC4CDVfVIVf0a+HpX\n16DBOr8BvO3529BjrGlkqupO4KkluuwCbqw5dwEbkmwec00jUyt7XWOkc7TCmk7aJIXHK6rqaNf+\nH+AVi/R7UZLZJHcl6TtgtgCPDiwf5ncn+Td9quoEcBx4Wc91nGxNAO/uDoG/kWTrKtaznJXWO2pv\nSnJfku8m+ZNRDNid0r4euHveprHN0RI1wUnOUR/PeaxYku8DZy+w6VODC1VVSRa7h/yqqjqS5Dzg\n9iT7qupQ37WuMd8BbqqqXyX5a+aOjP5izDVNknuZ+3Pz/OsR3wKWfD1iWN3rGrcAH62B97zGaZma\nTnqORnrkUVVvr6rXLfD5NvDY84du3ffji+zjSPf9CPAD5lK0L0eAwb+1z+nWLdgnyTrgpazu07LL\n1lRVT1bVr7rF64A3rGI9y1nJHI5Ujfj1iOVe12AMc7Qar5BM0mnLDHB5174c+Pb8Dkk2JlnftTcx\n93Tr/H83ZBj3ANuSvDrJacxdEJ1/R2ewzkuA26u74rRKlq1p3vnyxcyd047LDHBZd0fhQuD4wOno\nWIzy9YhunCVf12DEc7SSmprmaBRXoFd4RfhlwG3Aw8D3gTO79VPAdV37zcA+5u447APevwp17GTu\navQh4FPdus8AF3ftFwH/ChwE/gs4bwRzs1xN/wjs7+blDmD7KtZyE3AUeJa5c/X3Ax8EPthtD/Cl\nrtZ9wNQI5me5mq4cmJ+7gDevYi1/DhRwP7C3++wc5xytsKaTniMfT5fUZJJOWyStIYaHpCaGh6Qm\nhoekJoaHpCaGh6QmhoekJv8PCCQPV9d2xkgAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10da8ee10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sess = tf.InteractiveSession()\n",
    "image = np.array([[[[1],[2],[3]],\n",
    "                   [[4],[5],[6]], \n",
    "                   [[7],[8],[9]]]], dtype=np.float32)\n",
    "print(image.shape)\n",
    "plt.imshow(image.reshape(3,3), cmap='Greys')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1 filter (2,2,1,1) with padding: VALID\n",
    "\n",
    "weight.shape = 1 filter (2 , 2 , 1, 1)\n",
    "![image](https://cloud.githubusercontent.com/assets/901975/24833375/c0d9c262-1cf9-11e7-9efc-5dd6fe0fedb0.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "image.shape (1, 3, 3, 1)\n",
      "weight.shape (2, 2, 1, 1)\n",
      "conv2d_img.shape (1, 2, 2, 1)\n",
      "[[ 12.  16.]\n",
      " [ 24.  28.]]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10dad0160>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# print(\"imag:\\n\", image)\n",
    "print(\"image.shape\", image.shape)\n",
    "weight = tf.constant([[[[1.]],[[1.]]],\n",
    "                      [[[1.]],[[1.]]]])\n",
    "print(\"weight.shape\", weight.shape)\n",
    "conv2d = tf.nn.conv2d(image, weight, strides=[1, 1, 1, 1], padding='VALID')\n",
    "conv2d_img = conv2d.eval()\n",
    "print(\"conv2d_img.shape\", conv2d_img.shape)\n",
    "conv2d_img = np.swapaxes(conv2d_img, 0, 3)\n",
    "for i, one_img in enumerate(conv2d_img):\n",
    "    print(one_img.reshape(2,2))\n",
    "    plt.subplot(1,2,i+1), plt.imshow(one_img.reshape(2,2), cmap='gray')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1 filter (2,2,1,1) with padding:SAME\n",
    "![image](https://cloud.githubusercontent.com/assets/901975/24833381/fd01869e-1cf9-11e7-9d59-df08c7c6e5c4.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "image.shape (1, 3, 3, 1)\n",
      "weight.shape (2, 2, 1, 1)\n",
      "conv2d_img.shape (1, 3, 3, 1)\n",
      "[[ 12.  16.   9.]\n",
      " [ 24.  28.  15.]\n",
      " [ 15.  17.   9.]]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10dcb3a90>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# print(\"imag:\\n\", image)\n",
    "print(\"image.shape\", image.shape)\n",
    "\n",
    "weight = tf.constant([[[[1.]],[[1.]]],\n",
    "                      [[[1.]],[[1.]]]])\n",
    "print(\"weight.shape\", weight.shape)\n",
    "conv2d = tf.nn.conv2d(image, weight, strides=[1, 1, 1, 1], padding='SAME')\n",
    "conv2d_img = conv2d.eval()\n",
    "print(\"conv2d_img.shape\", conv2d_img.shape)\n",
    "conv2d_img = np.swapaxes(conv2d_img, 0, 3)\n",
    "for i, one_img in enumerate(conv2d_img):\n",
    "    print(one_img.reshape(3,3))\n",
    "    plt.subplot(1,2,i+1), plt.imshow(one_img.reshape(3,3), cmap='gray')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3 filters (2,2,1,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "image.shape (1, 3, 3, 1)\n",
      "weight.shape (2, 2, 1, 3)\n",
      "conv2d_img.shape (1, 3, 3, 3)\n",
      "[[ 12.  16.   9.]\n",
      " [ 24.  28.  15.]\n",
      " [ 15.  17.   9.]]\n",
      "[[ 120.  160.   90.]\n",
      " [ 240.  280.  150.]\n",
      " [ 150.  170.   90.]]\n",
      "[[-12. -16.  -9.]\n",
      " [-24. -28. -15.]\n",
      " [-15. -17.  -9.]]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10df0c4e0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# print(\"imag:\\n\", image)\n",
    "print(\"image.shape\", image.shape)\n",
    "\n",
    "weight = tf.constant([[[[1.,10.,-1.]],[[1.,10.,-1.]]],\n",
    "                      [[[1.,10.,-1.]],[[1.,10.,-1.]]]])\n",
    "print(\"weight.shape\", weight.shape)\n",
    "conv2d = tf.nn.conv2d(image, weight, strides=[1, 1, 1, 1], padding='SAME')\n",
    "conv2d_img = conv2d.eval()\n",
    "print(\"conv2d_img.shape\", conv2d_img.shape)\n",
    "conv2d_img = np.swapaxes(conv2d_img, 0, 3)\n",
    "for i, one_img in enumerate(conv2d_img):\n",
    "    print(one_img.reshape(3,3))\n",
    "    plt.subplot(1,3,i+1), plt.imshow(one_img.reshape(3,3), cmap='gray')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## MAX POOLING\n",
    "![image](https://cloud.githubusercontent.com/assets/901975/23337676/bd154da2-fc30-11e6-888c-d86bc2206066.png)\n",
    "\n",
    "![image](https://cloud.githubusercontent.com/assets/901975/23340355/a4bd3c08-fc6f-11e6-8a99-1e3bbbe86733.png)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 1, 1, 1)\n",
      "[[[[ 4.]]]]\n"
     ]
    }
   ],
   "source": [
    "image = np.array([[[[4],[3]],\n",
    "                    [[2],[1]]]], dtype=np.float32)\n",
    "pool = tf.nn.max_pool(image, ksize=[1, 2, 2, 1],\n",
    "                    strides=[1, 1, 1, 1], padding='VALID')\n",
    "print(pool.shape)\n",
    "print(pool.eval())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## SAME: Zero paddings\n",
    "\n",
    "![image](https://cloud.githubusercontent.com/assets/901975/23340337/71b27652-fc6f-11e6-96ef-760998755f77.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 2, 1)\n",
      "[[[[ 4.]\n",
      "   [ 3.]]\n",
      "\n",
      "  [[ 2.]\n",
      "   [ 1.]]]]\n"
     ]
    }
   ],
   "source": [
    "image = np.array([[[[4],[3]],\n",
    "                    [[2],[1]]]], dtype=np.float32)\n",
    "pool = tf.nn.max_pool(image, ksize=[1, 2, 2, 1],\n",
    "                    strides=[1, 1, 1, 1], padding='SAME')\n",
    "print(pool.shape)\n",
    "print(pool.eval())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extracting MNIST_data/train-images-idx3-ubyte.gz\n",
      "Extracting MNIST_data/train-labels-idx1-ubyte.gz\n",
      "Extracting MNIST_data/t10k-images-idx3-ubyte.gz\n",
      "Extracting MNIST_data/t10k-labels-idx1-ubyte.gz\n"
     ]
    }
   ],
   "source": [
    "from tensorflow.examples.tutorials.mnist import input_data\n",
    "mnist = input_data.read_data_sets(\"MNIST_data/\", one_hot=True)\n",
    "# Check out https://www.tensorflow.org/get_started/mnist/beginners for\n",
    "# more information about the mnist dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1152b2048>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAP8AAAD8CAYAAAC4nHJkAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAADY1JREFUeJzt3WuMHXUZx/HfY2kDQcNFcbOhlbXlVuFFhYVIJEaRGiAm\nxYQUN0EqGFdISSgpiQRJ7AteGNNaTEgka2gsRqoSBQox2ktIalMRWlJ3uSlo2rSl9EKh3QaCUh5f\n7KAL7PzP4czMmdl9vp9ks+fMM5cnJ/vbmXNmzvzN3QUgno/V3QCAehB+ICjCDwRF+IGgCD8QFOEH\ngiL8QFCEHwiK8ANBHdfNjZkZlxMCFXN3a2e+Qnt+M7vCzP5uZi+b2R1F1gWgu6zTa/vNbJqkf0ia\nL2m3pKclDbj784ll2PMDFevGnv9iSS+7+7/c/d+Sfi1pQYH1AeiiIuE/XdKucc93Z9Pex8wGzWyr\nmW0tsC0AJav8Az93H5I0JHHYDzRJkT3/Hkmzxj2fmU0DMAkUCf/Tks4ys8+a2QxJ35S0tpy2AFSt\n48N+d3/HzG6R9CdJ0yStcvfnSusMQKU6PtXX0cZ4zw9UrisX+QCYvAg/EBThB4Ii/EBQhB8IivAD\nQRF+ICjCDwRF+IGgCD8QFOEHgiL8QFCEHwiK8ANBEX4gKMIPBEX4gaAIPxAU4QeCIvxAUIQfCIrw\nA0ERfiAowg8ERfiBoAg/EBThB4Ii/EBQhB8IquMhuiXJzHZIGpV0TNI77t5fRlMAqlco/JmvuPvB\nEtYDoIs47AeCKhp+l7TOzLaZ2WAZDQHojqKH/Ze6+x4z+7Sk9Wb2ortvGj9D9k+BfwxAw5i7l7Mi\ns2WSjrr78sQ85WwMQC53t3bm6/iw38xONLNPvPdY0tckPdvp+gB0V5HD/h5JD5vZe+t50N3/WEpX\nACpX2mF/WxvjsB+oXOWH/QAmN8IPBEX4gaAIPxAU4QeCIvxAUGV8qw81u+GGG3JrrU7lvvbaa8n6\n3Llzk/UtW7Yk65s3b07WUR/2/EBQhB8IivADQRF+ICjCDwRF+IGgCD8Q1JQ5zz8wMJCsX3DBBcl6\n6lx505188skdL3vs2LFkfcaMGcn6W2+9lay/+eabubWRkZHksgsXLkzWDxw4kKwjjT0/EBThB4Ii\n/EBQhB8IivADQRF+ICjCDwQ1qW7dvWLFitzarbfemlx22rRpRTaNGjzxxBPJeqtrO/bt21dmO5MG\nt+4GkET4gaAIPxAU4QeCIvxAUIQfCIrwA0G1PM9vZqskfV3Sfnc/P5t2qqTfSOqTtEPSQnd/veXG\nCp7n37VrV25t5syZyWWHh4eT9VbfS69Sq3vbP/LII13q5KObP39+sn799dfn1vr6+gptu9V1ANde\ne21ubSrfC6DM8/y/kHTFB6bdIWmju58laWP2HMAk0jL87r5J0qEPTF4gaXX2eLWkq0vuC0DFOn3P\n3+Pue7PHr0rqKakfAF1S+B5+7u6p9/JmNihpsOh2AJSr0z3/PjPrlaTs9/68Gd19yN373b2/w20B\nqECn4V8raVH2eJGkR8tpB0C3tAy/ma2R9BdJ55jZbjP7jqQfSZpvZi9Jujx7DmASmVTf5z/77LNz\na+edd15y2Q0bNiTro6OjHfWEtNmzZ+fWHn/88eSyc+fOLbTt22+/PbeWujfEZMf3+QEkEX4gKMIP\nBEX4gaAIPxAU4QeCmlSn+jC1XHPNNcn6Qw89VGj9Bw8ezK2ddtpphdbdZJzqA5BE+IGgCD8QFOEH\ngiL8QFCEHwiK8ANBEX4gKMIPBEX4gaAIPxAU4QeCIvxAUIQfCIrwA0EVHq4LSLn55ptzaxdddFGl\n2z7++ONzaxdeeGFy2W3btpXdTuOw5weCIvxAUIQfCIrwA0ERfiAowg8ERfiBoFret9/MVkn6uqT9\n7n5+Nm2ZpO9KOpDNdqe7/6HlxrhvfyV6e3tza9ddd11y2SVLlpTdzvukejNr6/bylThy5EiyftJJ\nJ3Wpk/KVed/+X0i6YoLpK919XvbTMvgAmqVl+N19k6RDXegFQBcVec9/i5kNm9kqMzultI4AdEWn\n4f+ZpDmS5knaK2lF3oxmNmhmW81sa4fbAlCBjsLv7vvc/Zi7vyvp55IuTsw75O797t7faZMAytdR\n+M1s/Ee435D0bDntAOiWll/pNbM1kr4s6VNmtlvSDyV92czmSXJJOyR9r8IeAVSgZfjdfWCCyfdX\n0EtYl19+ebLe6rvng4ODubXZs2d31NNUt2rVqrpbqB1X+AFBEX4gKMIPBEX4gaAIPxAU4QeC4tbd\nJTjzzDOT9fvuuy9Zv+yyy5L1Kr/6unPnzmT99ddfL7T+u+66K7f29ttvJ5e99957k/Vzzjmno54k\n6ZVXXul42amCPT8QFOEHgiL8QFCEHwiK8ANBEX4gKMIPBMV5/jbddtttubXFixcnl50zZ06yfvTo\n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\nIvxAUIQfCOq/esVX4lsZQ0YAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1047a8278>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "img = mnist.train.images[0].reshape(28,28)\n",
    "plt.imshow(img, cmap='gray')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tensor(\"Conv2D_3:0\", shape=(1, 14, 14, 5), dtype=float32)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\nBnRCCLGE/wPkBmjsLVFsSgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x11250f748>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sess = tf.InteractiveSession()\n",
    "\n",
    "img = img.reshape(-1,28,28,1)\n",
    "W1 = tf.Variable(tf.random_normal([3, 3, 1, 5], stddev=0.01))\n",
    "conv2d = tf.nn.conv2d(img, W1, strides=[1, 2, 2, 1], padding='SAME')\n",
    "print(conv2d)\n",
    "sess.run(tf.global_variables_initializer())\n",
    "conv2d_img = conv2d.eval()\n",
    "conv2d_img = np.swapaxes(conv2d_img, 0, 3)\n",
    "for i, one_img in enumerate(conv2d_img):\n",
    "    plt.subplot(1,5,i+1), plt.imshow(one_img.reshape(14,14), cmap='gray')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tensor(\"MaxPool_2:0\", shape=(1, 7, 7, 5), dtype=float32)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x11ba50a58>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pool = tf.nn.max_pool(conv2d, ksize=[1, 2, 2, 1], strides=[\n",
    "                        1, 2, 2, 1], padding='SAME')\n",
    "print(pool)\n",
    "sess.run(tf.global_variables_initializer())\n",
    "pool_img = pool.eval()\n",
    "pool_img = np.swapaxes(pool_img, 0, 3)\n",
    "for i, one_img in enumerate(pool_img):\n",
    "    plt.subplot(1,5,i+1), plt.imshow(one_img.reshape(7, 7), cmap='gray')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}