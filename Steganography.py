import numpy as np 
from PIL import Image

#to perform image steganography using LSB method
class Steganography:
    def steganography():
        #open the cover image
        img1 = Image.open("image1.jpg")
        #convert cover image to greyscale image
        grey_image1 = np.array(img1.convert('L'))

        #open the secret image
        img2 = Image.open("image2.jpg")
        #convert secret image to greyscale image
        grey_image2 = np.array(img2.convert('L'))

        #array to store final image after embedding
        new = np.zeros(grey_image2.size)
        new.shape = (256,256)

        #to mask the 4 lsb digits to store the values of secret image
        for i in range (256):
            for j in range (256):
                grey_image1[i][j] = grey_image1[i][j] & 240  


        #to mask the 4 msb digits of secret image at the end by shifting them right
        for i in range (256):
            for j in range (256):
                if len(np.binary_repr(grey_image2[i][j])) == 7: #there are 7 bit and 8 bit numbers which are handled seperately
                    grey_image2[i][j] = grey_image2[i][j] >> 3
                elif len(np.binary_repr(grey_image2[i][j])) == 8:
                    grey_image2[i][j] = grey_image2[i][j] >> 4        
        
        #merging msb of secret image as lsb of cover image 
        for i in range (256):
            for j in range (256):
                new[i][j] = grey_image1[i][j] + grey_image2[i][j]
        new = new.astype(int) 
        
        return new
    
    
    #ALERT!! issues in retreiving bytes. to test again.
    def reverse():
        final = Steganography.steganography()
        #to convert int array from cover image to binary
        for i in range (256):
            for j in range (256):
                final[i][j] = np.binary_repr(final[i][j]) 
                final[i][j] = final[i][j] & 15
                #final[i][j] = final[i][j] << 4         
        return final        

        
   
        
        
        
            
                  



        
        
    