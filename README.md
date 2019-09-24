# image-filtering
The goal of this project is to study the optimization methods for computer vision classification algorithms. We believe that the discrete Fourier transform of the signal can be classified in the same way as the raw signal itself. Moreover, due to the property of Fourier expansions, higher Fourier harmonics carry less information about the data than lower harmonics. We claim that only the latter may be used without large decrease in the accuracy of the classification algorithm. We introduce the additional step in both training and classification, which is the Fourier transform of the one-dimensional signal obtained by passing an input picture along a certain space-filling curve. Most of the space-filling curves are not periodic, but Fourier transform assumes the transformed signal to be periodic. That explains the choice of the periodic Sierpinski curve, which can be obtained from the original Sierpinski curve with slight modification.

Here, we analyze the 'cats vs non-cats' dataset, which is a set of 209 RGB train images and 50 test images labeled as cat or non-cat. We train a binary classifier to identify whether there is a cat on the image or not. 

Each image is of shape (64, 64, 3), where 3 is for the 3 channels (RGB). There are 12288 features. We first read pixels in each of the RGB matrices by using periodic Sierpinski curve. 


2nd-order Hilbert curve | 2nd-order modified Sierpiński curve
:----------------------:|:-------------------------:
<img src="https://github.com/anastasiiakim/image-filtering/blob/master/images/hilbertRGB.png" style="width:400px;height:300px"  width="300"/>  |  <img src="https://github.com/anastasiiakim/image-filtering/blob/master/images/readwithcurve.png" style="width:400px;height:300px" width="350"/>



After that, we apply Fourier transform and apply L-layer neural networks to these modified values. Our goal is significantly reduce training time but retain similar classification accuracy.      

Here we have several jupyter notebooks:
* *sierpinski.ipynb* notebook shows how to draw periodic Sierpinski space-filling curve with different orders.
* *fourier.ipynb* notebook shows how to apply Fourier transform on the image.
* *classification_cats_vs_noncats.ipynb* notebook contains full explanation how we use the 'cats vs non-cats' dataset to train a binary classifier after applying Fourier transform of the one-dimensional signal obtained by passing an input picture along the periodic Sierpinski space-filling curve. 
