# DeepMusics 

  ![image](https://github.com/CancerProfiling/DeepMusics/blob/main/Figures/deepMusics.jpg)
  
  
Multi-omics data, such as gene expression, methylation, mutation and copy number variation, can elucidates valuable insights of molecular mechanisms for various diseases. However, due to their different modalities and high dimension, utilizing and integrating different types of omics data suffers from great challenges. There is an urgent need to develop a powerful method to improve survival prediction and detect functional gene modules from multi-omics data to overcome these difficulties. In this paper, we developed DeepMusics, a flexible, scalable and interpretable method for extracting relationships between the clinical outcomes and multi-omics data based on deep learning framework. DeepMusics can efficiently implement non-linear combination and incorporate prior biological information defined by users (such as signalling pathway and tissue-specific functional gene modules) 

DeepMusics can be applied to different resolved-omics data and any type of clinical outcomes, including categorical (stages of subtypes) and continuous (survival time) ones. DeepMusics was evaluated on eight cancer datasets publicly available with four types of omics data and clinical data of survival time from TCGA project and compare its performance with other five cutting-edge prediction algorithms. In addition, the relevance of the information extracted when spiting the effect of various signatures and demonstrate the integration of activist of pathways estimated in a multi-omics context for the analysis of inter-cancer survival signalling.

## Install
To use DeepMusics, do the following:

1.Install the environment, To run the code please first make sure that you have [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [conda](https://docs.conda.io/) installed.

2.Prepare data

Note.The example datasets are listed in the expreiments/data.

3.Train and evaluate DeepMusics

## Install require softwares

Next step is to create a conda env DeepMusics and install Python v3.7.4 and required packages.

    conda create --name DeepMusics -c conda-forge -c python=3.7.4 
    conda activate DeepMusics
    conda install -c conda-forge statsmodels sebp scikit-survival
    pip install numpy pandas scikit-learn scipy dgl torch==1.5.0 ecos joblib numexpr osqp
    
## Activate the conda env using this command
    
    conda activate DeepMusics

## Now clone the git repo

    git clone https://github.com/CancerProfiling/DeepMusics.git DeepMusics && cd DeepMusics

## Data for Functional Module

Pathway prior knowledge information is from the Molecular Signatures Database MSigDB (http://www.gsea-msigdb.org/gsea/msigdb/index.jsp).


Mutations,expressions,methlations,copy number variation and clinical information of all cancer types are from TCGA Database(https://portal.gdc.cancer.gov/).

Some example data of both are given in the experiments/data/

## Data for omics 
 
The multi-omics data are preprocessed into different sets of matrixes.

For example, you can have either 

1.mutation matrix 

2.expression matrix

3.methylations matrix （cpG sites with gene sites coordinate information needed）

4.copy number variation matrix

The shapes for them are genes * samples, which are inputs of the model.

Some example datasets are given for testing in the experiments/data/.

The input data is a matrix including multiple samples with following features:
omic1_gene1,---,omic1_geneN,omic2_gene1,---,omic2_geneN2,omic3_gene1,---,omic3_geneN3,omic4_gene1,---,omic4_geneN4
Of course, the number of omics typeis is self-defined, the number of genes is self-defined too.

You can define them by yourself as the example data given in the [example data]/(https://github.com/CancerProfiling/DeepMusics/tree/main/experiments/data).

## Model 

Train the model via the following:

    cd DeepMusics
    usage: Run.py [-h] [-G INPUTG] [-F INPUTF]
    please enter the OmicsNum,geneNum,functionMouduleNum
    optional arguments:
    -h, --help            show this help message and exit
    -G INPUTG, --inputG INPUTG
                        this is total gene number
    -F INPUTF, --inputF INPUTF
                        this is functional module or pathways number or your
                        can define your own GO set by yourself

## Contact

Please open an issue or contact zhaolianhe@ict.ac.cn with any questions.
