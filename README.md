# cs640GroupProject

SCC configuration that is required:
- 1 GPU
- 8.9 core

Directions:
- Ensure that you have the pretrained model provided in the repo in your path. Ensure that you have the traning, testing , and metadata files in the correct SCC filepath.
- To convert the file output of the model to binary classifier labels, simply run the conversion.py file. 

Debugging:
- If you encounter errors running the hyper-paramater tuning with Ray tune, change the device used to just CPU. You can change this via CONFIG['device'] = 'cpu'. Also make sure to set resources_per_trial to {cpu:32, gpu:0} 
