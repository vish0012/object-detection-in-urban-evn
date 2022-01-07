import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    
    
    # refer from github
    # getting data from waymo dataset
    waymo_data = os.listdir(data_dir + '/training_and_validation')
    random.shuffle(waymo_data)

    # variables
    num_tfrecords  = len(waymo_data)
    training_data   = num_tfrecords*0.75
    val_data = num_tfrecords*0.15
    test_data    = num_tfrecords*0.10
    
    #iterate through all tfrecords 
    for i,tfrecord in enumerate(waymo_data):
        # Number of Tfrecords for training
        if i < training_data:
            shutil.move(data_dir+'/training_and_validation/'+tfrecord, data_dir + '/train')
          
        # Number of Tfrecords for validation
        elif i >= training_data and i < training_data+val_data:
            shutil.move(data_dir+'/training_and_validation/'+tfrecord, data_dir + '/val')
         
        # Number of Tfrecords for testing
        else:
            shutil.move(data_dir+'/training_and_validation/'+tfrecord, data_dir + '/test')
    
    #Provice information about the splits created
    print('The {} tfrecords were splitted as follows: Training: {} | Validation {} | Testing {}'
          .format(num_tfrecords,training_data,val_data,test_data))

    
    
     
    
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)