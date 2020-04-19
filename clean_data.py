import os 
import shutil
from PIL import Image

class clean_data:
    def __init__(self):

        self.root_folder = os.getcwd()
        self.folder_list = ['subject_1', 'subject_2']
        self.folder_full = []
        self.s1_folder = self.root_folder+'/'+self.folder_list[0]
        self.s2_folder = self.root_folder+'/'+self.folder_list[1]
        self.clean_folder = self.root_folder+'/data_clean'
        self.folder_full.append(self.s1_folder)
        self.folder_full.append(self.s2_folder)
        self.faces = []

        #=========Creating directories===============
        if 'data_clean' in os.listdir():
            shutil.rmtree('data_clean')
        os.mkdir('data_clean')
        os.chdir(self.clean_folder)

        if self.folder_list[0] in os.listdir():
            shutil.rmtree(self.folder_list[0]) 
        os.mkdir(self.folder_list[0])
        if self.folder_list[1] in os.listdir():
            shutil.rmtree(self.folder_list[1])
        os.mkdir(self.folder_list[1])


    def load_images(self, folder_name):
        self.faces.clear()
        os.chdir(folder_name)
        self.images = os.listdir()
        for image in self.images:
            picture = Image.open(image)
            picture = picture.resize((250, 300), resample=0, box=None)
            self.faces.append(picture)
        os.chdir(self.root_folder)
        print(self.faces)
        return self.faces

    def body(self):
        for index, folder in  enumerate(self.folder_list):
            images = self.load_images(self.folder_full[index])
            os.chdir(self.root_folder+'/data_clean/'+self.folder_list[index])
            for im_index, img in enumerate(images):
                img.save('image{}.png'.format(im_index))
            os.chdir(self.root_folder)

cleaner_script = clean_data()
cleaner_script.body()