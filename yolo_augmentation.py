import os
import shutil
import cv2
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
directory_position = "!!!!!!! write your directiry path! !!!!!!"
folder_list = os.listdir(directory_position)
for folder_names in folder_list : 
    folder_path = directory_position + "\\" + str(folder_names)
    file_names = os.listdir(folder_path)
    num_jpg = 0
    num_txt = 0
    error_folder_list = []
    for filename_extension in file_names:
        if filename_extension.endswith(".jpg") :
            num_jpg += 1
        if filename_extension.endswith(".txt") :
            num_txt += 1
    if num_jpg != num_txt :
        error_folder_list.append(str(folder_names) +", jpg:"+ str(num_jpg) +"," + " txt:" + str(num_txt))
error_folder_number = len(error_folder_list)
if error_folder_number != 0 :
    print("check your folder list" + '\n' + str(error_folder_list))
else:
    copy_directory = directory_position + "_augmentation"
    shutil.copytree(directory_position, copy_directory)
    copy_folder_list = os.listdir(copy_directory)
    for copy_folder_names in copy_folder_list :
        copy_folder_path = copy_directory + "\\" + str(copy_folder_names)
        copy_file_list = os.listdir(copy_folder_path)
        for copy_file_names in copy_file_list:
             if copy_file_names.endswith(".jpg") :
                div_names = copy_file_names[0:len(copy_file_names)-4]
                original_image = Image.open(copy_folder_path + '\\'+ copy_file_names)
                flip_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
                flip_image.save(copy_folder_path+ "\\" +str(div_names)+"_flip.jpg")
             if copy_file_names.endswith(".txt") : 
                original_txt = open(copy_folder_path + '\\'+ copy_file_names , 'r')
                div_names = copy_file_names[0:len(copy_file_names)-4]
                flip_txt = open(copy_folder_path+ "\\" + div_names +"_flip.txt" ,'w')  
                lines = original_txt.readlines()
                for line in lines:
                    complete_txt=line.split()
                    class_name = complete_txt[0]
                    x_axis = complete_txt[1]
                    y_axis = complete_txt[2]
                    width = complete_txt[3]
                    height = complete_txt[4]
                    x_axis = 1-float(x_axis)
                    x_axis = round(x_axis,6)
                    flip_txt.write(str(class_name)+" "+str(x_axis)+" "+str(y_axis)+" "+str(width)+" "+str(height)+ '\n')
                    original_txt.close             
                    flip_txt.close
        copy_file_list = os.listdir(copy_folder_path)
        for copy_file_names in copy_file_list:
            if copy_file_names.endswith(".jpg"):
                original_image = Image.open(copy_folder_path + "\\" + copy_file_names)
                div_names = copy_file_names[0:len(copy_file_names)-4]   
                grayscale_image = original_image.filter(ImageFilter.BoxBlur(1.5))  
                grayscale_image.save(copy_folder_path+ "\\" +str(div_names)+"_gray.jpg")       
                blur_image = original_image.convert('L')                 
                blur_image.save(copy_folder_path+ "\\" +str(div_names)+"_blur.jpg") 
            if copy_file_names.endswith(".txt"):
                original_txt = open(copy_folder_path+"\\"+copy_file_names, 'r')                            
                div_names = copy_file_names[0:len(copy_file_names)-4]                                         
                grayscale_txt = open(copy_folder_path+"\\"+div_names+"_gray.txt" ,'w')                   
                blur_txt = open(copy_folder_path+"\\"+div_names+"_blur.txt" ,'w')                   
                txt_data = original_txt.read()                                            
                grayscale_txt.write(txt_data)                                              
                blur_txt.write(txt_data)
                original_txt.close()                                                  
                grayscale_txt.close()                                                  
                blur_txt.close()
