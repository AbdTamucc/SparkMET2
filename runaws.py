import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Check if there is GPU(s): {torch.cuda.is_available()}")

from src import FogDataloader as fog
from src import SparkMET as sm


# Exp_Name: embeddingtype_lr_wd_batch_size_nheads_nlayers
Exp_name = '4D_Emb2DPatch_aws_0001_01_32_8_6'
SaveDir  = '/home/ubuntu/EXPs/'

#****************************************************************************************************#
#********************************************** DATA CONFIGS ****************************************#
#****************************************************************************************************#

data_loader_training, data_loader_validate, data_loader_testing = fog.Fog_DataLoader_npz(batch_size = 32, 
                                                                                     WeightR    = False, 
                                                                                     SaveDir    = SaveDir, 
                                                                                     Exp_name   = Exp_name)

#****************************************************************************************************#
#********************************************** Model CONFIGS ****************************************#
#****************************************************************************************************#

# Emb_2D_SP_Patch, Emb_2D_Patch, Emb_2D_Channel
SparkMET_Config = sm.SparkMET_Configs(img_size   = 32, 
                                      in_channel = 388, 
                                      in_time    = 4, 
                                      embd_size  = 1024, 
                                      num_heads  = 8, 
                                      num_layers = 6, 
                                      FactType   = 'Emb_2D_Patch').return_config()

SparkMET_Obj    = sm.SparkMET(SparkMET_Config, 
                           SaveDir = SaveDir, 
                           Exp_Name = Exp_name) 


model, optimizer, loss_func = SparkMET_Obj.compile(optmizer = 'adam', 
                                                   loss = 'NLLLoss', 
                                                   lr = 0.0001, 
                                                   wd = 0.01)
 
model, loss_stat = SparkMET_Obj.train(model, optimizer, loss_func, 
                                      data_loader_training, 
                                      data_loader_validate, 
                                      epochs = 30, 
                                      early_stop_tolerance = 30)

list_outputs     = SparkMET_Obj.predict(model, data_loader_training, 
                                        data_loader_validate, 
                                        data_loader_testing)







