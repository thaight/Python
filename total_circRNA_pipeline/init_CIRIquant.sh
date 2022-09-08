#!/bin/bash
prefix=$1
read1=$2
read2=$3
outpath=$4
config=$5
threads="4"
pipelinepath=$6
toolspath=/home/thaight/projects/rrg-zovoilis/thaight/circular_RNA_detection/circular_detection/bin/CIRIquant

sbatch "$pipelinepath"run_CIRIquant_"$prefix".sh "$prefix" "$read1" "$read2" "$outpath" "$config" "$pipelinepath"







