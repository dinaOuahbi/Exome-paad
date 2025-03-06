# Exome-paad  
**Differential comparison between good and bad prognosis in pancreatic cancer, according to the classification of a deep learning model.**  

## Data Preprocessing  

- Patients without exome data: **model8 (n=25)**.  
- Intersection of exome data (**n=152**) with our patients: **model8 (n=141)**.  
- Removal of single-modality variables: **'disease', 'subtype'**.  
- Checking for missing values: overlapping missing data allow us to separate our dataset into **three subparts**.  

![Missing Data Overview](https://github.com/dinaOuahbi/Exome-paad/blob/main/results/exome_missing_data.PNG)  

## Univariate Analysis  

The univariate analysis aims to identify differentially expressed features between patients with good and bad prognosis.  

![Univariate Analysis Results](https://github.com/dinaOuahbi/Exome-paad/blob/main/results/differential_analysis.PNG)  

## Visualization  

A graphical representation of differentially expressed features between prognosis groups.  

![Visualization](https://github.com/dinaOuahbi/Exome-paad/blob/main/results/differential_analysis_visualization.PNG)  
