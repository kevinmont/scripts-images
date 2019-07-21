# Python 3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
from os import rename 
from os import listdir
from shutil import move
from PIL import Image as image
import PIL
  
# Function to rename multiple files 
def rename_files(): 
    i = 1
      
    for filename in listdir("image"): 
        dst = str(i) + ".png"
        src ='image/'+ filename 
        dst ='image/'+ dst 
          
        # rename() function will 
        # rename all the files 
        rename(src, dst) 
        i += 1
  
# Funtion to rotate 90ª degrees leftmultiple
# multiple files
# with a proportion of 1050 x 650  
def rotate():
    for filename in listdir("image"):
        src = str("image/")+filename
        im = image.open(src)
        im.load()
        im_resized = im.resize((650,1050),PIL.Image.BILINEAR)
        im_rotated = im_resized.rotate(90,PIL.Image.BILINEAR ,True)
        im_rotated.save(im.filename,'png')
        
    
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    #rename_files()
    rotate()
    