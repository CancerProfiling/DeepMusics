#!/bin/bash
# rna.final.final.csv pathway_rna_final_new.csv 5541 scna.final.trans.csv pathway_mask_scna.csv 5507 517
echo "Shell input rna_expression_omic_filename, rna_functional_module_filename,copy_number_variant_omic_filename,cnv_functional_module_filename";
echo "the exe shell file is ：$0";
echo "rna omics file is ：$1";
echo "rna functional module：$2";
echo "genes number in rna functional module：$3"; #5541
echo "scna omics file is ：$4";
echo "scna functional module file is ：$5";
echo "genes number in scna functional module：$6"; #5507
echo "total sample number is ：$7"; 
rnafile=$1;
scnafile=$2;
a=$3;
b=$6;
num=$7
paste $1 $4 > scna_rna_omics_entire.csv ;
paste $2 $5 > pathway_mask_scna_rna.csv ;
