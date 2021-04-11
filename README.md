# DeepMusics 

  ![image](https://github.com/CancerProfiling/DeepMusics/blob/main/Figures/deepMusics.jpg)
  
  
Multi-omics data, such as gene expression, methylation, mutation and copy number variation, can elucidates valuable insights of molecular mechanisms for various diseases. However, due to their different modalities and high dimension, utilizing and integrating different types of omics data suffers from great challenges. There is an urgent need to develop a powerful method to improve survival prediction and detect functional gene modules from multi-omics data to overcome these difficulties. In this paper, we developed DeepMusics, a flexible, scalable and interpretable method for extracting relationships between the clinical outcomes and multi-omics data based on deep learning framework. DeepMusics can efficiently implement non-linear combination and incorporate prior biological information defined by users (such as signalling pathway and tissue-specific functional gene modules) 

DeepMusics can be applied to different resolved-omics data and any type of clinical outcomes, including categorical (stages of subtypes) and continuous (survival time) ones. DeepMusics was evaluated on eight cancer datasets publicly available with four types of omics data and clinical data of survival time from TCGA project and compare its performance with other five cutting-edge prediction algorithms. In addition, the relevance of the information extracted when spiting the effect of various signatures and demonstrate the integration of activist of pathways estimated in a multi-omics context for the analysis of inter-cancer survival signalling.

## Install
To use DeepMusics, do the following:

1.Install the environment

2.Prepare data

Note.The example datasets are listed in the expreiments/data.

3.Train and evaluate DeepMusics

## Data

Pathway prior knowledge information is from the Molecular Signatures Database MSigDB (http://www.gsea-msigdb.org/gsea/msigdb/index.jsp).


Mutations,expressions,methlations,copy number variation and clinical information of all cancer types are from TCGA Database(https://portal.gdc.cancer.gov/).

Some example data of both are given in the experiments/data/example.csv

## Model
 
The multi-omics data are preprocessed into four sets of matrixes.

1.mutation matrix 

2.expression matrix

3.methylations matrix （cpG sites with gene sites coordinate information needed）

4.copy number variation matrix

The shapes for them are genes * samples, which are inputs of the model.

Some example datasets are given for testing.

The input data is a matrix including multiple samples with following features:
omic1_gene1,---,omic1_geneN,omic2_gene1,---,omic2_geneN2,omic3_gene1,---,omic3_geneN3,omic4_gene1,---,omic4_geneN4

Of course, the number of omics typeis is self-defined, the number of genes is self-defined too.

Train the model via the following:

    cd DeepMusics
    usage: Run.py [-h] [-N OMICSNUM] [-G INPUTG] [-F INPUTF]
    please enter the OmicsNum,geneNum,functionMouduleNum
    optional arguments:
    -h, --help            show this help message and exit
    -N OMICSNUM, --input OMICSNUM
                        this is total omics number
    -G INPUTG, --inputG INPUTG
                        this is total gene number
    -F INPUTF, --inputF INPUTF
                        this is functional module or pathways number and your
                        can define by yourself

## Contact

Please open an issue or contact zhaolianhe@ict.ac.cn with any questions.
