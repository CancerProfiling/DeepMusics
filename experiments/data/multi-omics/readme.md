# Example datasets

To get started, you can download example datasets as shown in multi-omics file:

there are combined copy number varint and RNA expression omics data together.

For example , if you data is

 rna_expression_omic_file

 rna_functional_module_file

 copy_number_variant_omic_file
 
 cnv_functional_module_file, 

you can use combine.sh to combine them into the following datasets

You can also set your own data as the example given in the following link.

[scna_rna_train data](https://github.com/CancerProfiling/DeepMusics/blob/main/experiments/data/multi-omics/scna_rna.train.csv)

[scna_rna_test data](https://github.com/CancerProfiling/DeepMusics/blob/main/experiments/data/multi-omics/scna_rna.test.csv)

[scna_rna_validation data](https://github.com/CancerProfiling/DeepMusics/blob/main/experiments/data/multi-omics/scna_rna.validation.csv)

[scna_rna_functional module data](https://github.com/CancerProfiling/DeepMusics/blob/main/experiments/data/multi-omics/pathway_mask_scna_rna.csv)
# Run example case

To test multi-omics example, we provide scna and rna expression omics as example here.

   Run.py: to train the model with the inputs from train.csv.
   
   
   Hyperparmeters are optimized by validation.csv. 
   
   
   C-index is used to evaluate the model performance with test.csv.

Your can run 


    python Run.py
