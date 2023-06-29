import os
import shutil


def findLogo():
    root = 'F:/CarLogo/cc'
    for d in os.listdir(root):
        if os.path.exists(os.path.join(root, d, 'logo.jpg')):
            shutil.copy(os.path.join(root, d, 'logo.jpg'), 'data/logos/{}.jpg'.format(d))
        else:
            print('[miss] {}'.format(d))



