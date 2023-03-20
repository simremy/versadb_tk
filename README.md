# VersaDB
Versa DB is a python-based program that bridges popular NMR and MS/MS spectra prediction tools (i.e. NMRShiftDB2 and CFM-ID 4.0) and natural products structural databases such as LOTUS for the generation of adaptable predicted spectral databases.

## Installation
Pre-requisite : 
 - Windows 10
 - Anaconda 3 (add .../condabin to path)
 - Java (add .../javapath to path)
 - Docker Desktop WSL 2 backend https://docs.docker.com/desktop/windows/wsl/

1. Clone VersaDB repo on your Desktop. **DO NOT CHANGE THE FOLDER LOCATION OR NAME**
2. Click on install.bat and wait. This batch file will create a new anaconda environment, install all dependencies, and configure NMRShiftDB and the CFM-ID docker container. (If this doesn't work try the uninstall.bat file and run again install.bat.)

## Run the program
Click on versadb.bat

![Plan de travail 11080](https://user-images.githubusercontent.com/41745996/168621136-db932ff8-f33d-46e2-95d3-2856455a08af.png)

### Create the structural DB:  
1. Select the database you want to search in or select all databases. 
2. Select catergories:  Taxon - Chemical class - Lotus ID - Molecular formula.   
3. Add each category to the input with the button "add to input" in each panel.  
4. The "get all categories" function will return all the compounds belonging to at least one of the selected category.  
   The "get chemical class" function will return all the compound of the selected chemical class in the selected taxon.  
### Predict spectra
5. "Predict MS/MS spectra" will create a .mgf file containing the MS/MS spectra (3 collision energies/compound) predicted locally with CFM-ID 4.0  
"Predict 13C NMR spectra" will create a .sdf file containing the 13C chemical shift predicted locally with NMRShiftDB2 


