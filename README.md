# Steganography using Least Significant bit (LSB) Embedding Approach
## By Alita Sabu Paul, 21ECA05, as part of DSP assignment 
## What is Image Steganography?
> [Image Steganography](https://towardsdatascience.com/steganography-hiding-an-image-inside-another-77ca66b2acb1) is the practice of concealing a file, message, image, or video within a cover image.
## Implementation using LSB techique
1. The cover image and secret images are converted to 256x256 pixel greyscale image and then converted into numpy arrays.
2. The last 4 binary digits (i.e LSBs) are masked to store the MSBs of secret image.
3. The last 4 binary digots of secret image are also hidden, and the first 4 digits are then shifted right so that the result of operation can be merged with the result form step 2.
4. The results of step 2 and step 3 are merged.
5. The resultant numpy array is then converted to an image.
6. The secret image can be retrived, though less in quality, from the last from 4 digits of each element of numpy array obtained at step 4.
   
![image depicting LSB techique](https://camo.githubusercontent.com/0dbb8ce754678cc1999c1792258eeeae18c434ec9fedd44b26d0ae9d79984c24/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f323030302f312a6b704461306a74366674536365346234445141324d512e706e67)
## Language and Libraries used
I used the **Numpy and PIL libraries in Python** and created a custom library named Steganography to implement this technique.
## Result
The code was simulated, and output was obtained as expected. Though some image quality was lost in the process, the image is still comprehensible.
## References
[Steganography: Hiding an image inside another](https://towardsdatascience.com/steganography-hiding-an-image-inside-another-77ca66b2acb1) by Kelvin Salton do Prado
