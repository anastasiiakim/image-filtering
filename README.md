# image-filtering
The goal of this project is to study the optimization methods for computer vision classification algorithms. We introduce the additional step in both training and classification, which is reading an input picture along a certain space-filling curve. Most of the space-filling curves are not periodic, we used the periodic Sierpinski curve.  We modified and implemented the Sierpinski curve so that it could go through every pixel. We also considered Hilbert curve, the most common space-filling curve. Because space-filling curves preserve a maximum of spatial locality information between elements, we believe that using space-filling curve mapping as a preprocessing tool, preserves enough information of neighbouring pixels to be used by 1D CNNs. We evaluated the classification performance of 1D CNNs on Cifar-10 image dataset.

Here, we analyze the 'Cifar-10' dataset, which is a set of 50000 RGB train images and 10000 test images. This dataset has 10 classes. We train 1D CNNs to identify the correct object. 

Each image is of shape (32, 32, 3), where 3 is for the 3 channels (RGB). There are 3072 features. We first read pixels in each of the RGB matrices by using either periodic Sierpinski curve or Hilbert curve. 


2nd-order Hilbert curve | 2nd-order modified Sierpiński curve
:----------------------:|:-------------------------:
<img src="https://github.com/anastasiiakim/image-filtering/blob/master/images/hilbertRGB.png" style="width:400px;height:300px"  width="360"/>  |  <img src="https://github.com/anastasiiakim/image-filtering/blob/master/images/readwithcurve.png" style="width:400px;height:300px" width="370"/>


After that, we apply one-dimensional convolutional neural networks. Our goal is to reduce training time but retain similar classification accuracy.

Here we have several jupyter notebooks:
* *sierpinski.ipynb* notebook shows how to draw periodic Sierpinski space-filling curve with different orders.
* *hilbert.ipynb* notebook shows how to draw Hilbert space-filling curve with different orders.
* *cifar10_conv1d.ipynb* notebook contains full explanation how we use the Cifar-10 dataset to train 1D CNNs after mapping 2D data to one-dimensional signal obtained by passing an input picture with space-filling curves. 
* *fourier.ipynb* notebook shows how to apply Fourier transform to reduce noise of the image. I keep this notebook for future use.



