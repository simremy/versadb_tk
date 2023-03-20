#!/usr/bin/env python
# coding: utf-8

#import libraries 

import os
import string
import glob
import subprocess
from subprocess import Popen
import shutil
import time
import datetime
from datetime import datetime
import pandas as pd
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from itertools import count, cycle

#import packages
from packages import tool_path, ginfo, action, prediction




# create app main window
def create_main_window():
    tool_path.check_setup()
    
    global window
    window = tk.Tk()
    window.title('VERSA DB V1.2 ٩(̾●̮̮̃̾•̃̾)۶ URCA ICMR')
    
    global w, h
    w = Tk.winfo_screenwidth(window)
    h = Tk.winfo_screenheight(window)
    print(w, h)
    window.minsize(640,480)
  
    window.geometry("%dx%d" % (640, 480))
    
    global scale_list   #create a variable for resizing the main window
    scale_list = ['']
    window.bind('<Configure>', on_resize)
    
    

    
    create_criteria_main_frame()     # -> create a global frame for the criteria selection
    create_taxonomy_db_frame()       # -> create a taxonomy db criteria frame 
    create_criteria_subframe()       # -> create a subframe in criteria_frame
    create_taxonomy_frame()          # -> create listboxes for taxonomy criteria
    create_chemontology_frame()      # -> create listboxes for chemontology criteria
    create_action_main_frame()       # -> create an action frame to process selected criteria
    create_lotus_id_frame()          # -> create a frame to search directly from LOTUS ID (e.i. LTS0193685)
    create_molecular_formula_frame() # -> create a frame to search directly from molecular formula (e.i. C6H12O6)
    create_action_subframe()
    
    window.iconphoto(False, tk.PhotoImage(file='./packages/versadb.png'))
    window.mainloop()


def create_criteria_main_frame():
    global criteria_frame
    criteria_frame = Frame(window, borderwidth=10, relief=GROOVE, width=int((2/3)*w), height=h)
    criteria_frame.pack(side=LEFT, fill=BOTH, expand=1)



def create_action_main_frame():
    global action_main_frame
    action_main_frame = Frame(window, borderwidth=10, relief=GROOVE, width=int((1/3)*w), height=h)
    action_main_frame.pack(side=LEFT, fill=BOTH, expand=1)



def on_resize(event):
    # determine the ratio of old width/height to new width/height      
    wscale = Tk.winfo_width(window)/w
    hscale = Tk.winfo_height(window)/h
    
    all_scale = str(wscale + hscale)
    scale_list.append(all_scale)
    if len(scale_list) >2:
        del scale_list[0]
    if scale_list[0] != scale_list[1]:

        criteria_frame['width'] =int(((2/3)*w)*wscale)
        criteria_frame['height'] =int((h)*hscale)

        taxonomy_db_main_frame['width'] = int(((2/3)*w)*wscale)
        taxonomy_db_subframe_1['width'] = int(((2/3)*w)*wscale)
        taxonomy_db_subframe_2['width'] = int(((2/3)*w)*wscale)
        taxonomy_db_subframe_3['width'] = int(((2/3)*w)*wscale)
        taxonomy_db_main_frame['height'] = int(((2/3)*w)*hscale)
        taxonomy_db_subframe_1['height'] = int(((2/3)*w)*hscale)
        taxonomy_db_subframe_2['height'] = int(((2/3)*w)*hscale)
        taxonomy_db_subframe_3['height'] = int(((2/3)*w)*hscale)

        taxonomy_main_frame['width']= int(((2/3)*w)*wscale)
        taxonomy_main_frame['height']= int(h*hscale)

        taxonomy_family_frame['height']= int(h*hscale)
        taxonomy_genus_frame['height']= int(h*hscale)
        taxonomy_species_frame['height']= int(h*hscale)
        taxonomy_family_frame['height']= int(h*hscale)
        taxonomy_genus_frame['height']= int(h*hscale)
        taxonomy_species_frame['height']= int(h*hscale)

        taxonomy_family_listbox['width'] = int((((80*w)/1920))*wscale)
        taxonomy_genus_listbox['width']= int((((80*w)/1920))*wscale)
        taxonomy_species_listbox['width']= int((((80*w)/1920))*wscale)
        taxonomy_family_listbox['height'] = int((((10*h)/880))*hscale)
        taxonomy_genus_listbox['height']=  int((((10*h)/880))*hscale)
        taxonomy_species_listbox['height']=  int((((10*h)/880))*hscale)

        action_main_frame['width'] =int(((1/3)*w)*wscale)
        action_main_frame['height'] =int((h)*hscale)

        chemontology_main_frame['width']= int(((2/3)*w)*wscale)
        chemontology_main_frame['height']= int(h*hscale)

        chemontology_pathway_frame['width']= int((((2/3)*w)/2)*wscale)
        chemontology_superclass_frame['width']= int((((2/3)*w)/2)*wscale)
        chemontology_class_frame['width']= int((((2/3)*w)/2)*wscale)
        chemontology_pathway_frame['height']= int((h/3)-((1/3)*(h/3))*hscale)
        chemontology_superclass_frame['height']= int((h/3)-((1/3)*(h/3))*hscale)
        chemontology_class_frame['height']= int((h/3)-((1/3)*(h/3))*hscale)

        chemontology_pathway_listbox['width'] = int((((80*w)/1920))*wscale)
        chemontology_pathway_listbox['height'] = int((((10*h)/880))*hscale)
        chemontology_superclass_listbox['width'] =  int((((80*w)/1920))*wscale)
        chemontology_superclass_listbox['height'] = int((((10*h)/880))*hscale)
        chemontology_class_listbox['width'] =  int((((80*w)/1920))*wscale)
        chemontology_class_listbox['height'] = int((((10*h)/880))*hscale)
    
    
        taxonomy_action_frame['width'] =int((((2/3)*w)/2)*wscale)
        taxonomy_action_frame['height'] =int(((2*h)/1080)*hscale)

        chemontology_action_frame['width'] =int((((2/3)*w)/2)*wscale)
        chemontology_action_frame['height'] =int(((2*h)/1080)*hscale)
    
    ############################################################
    
        lotus_id_main_frame['width']=int((1/3)*w*wscale)
        lotus_id_main_frame['height']=int(((1/8)*h)*hscale)
      
        molecular_formula_main_frame['width']=int((1/3)*w*wscale)
        molecular_formula_main_frame['height']=int(((1/8)*h*hscale))
        

        action_subframe_1['width']=int((1/3)*w*wscale)
        action_subframe_1['height']=int(((1/4)*h*hscale))
                              
        lotus_search_criteria_frame['width']=int((1/3)*w*wscale)
        lotus_search_criteria_frame['height']=int(((1/4)*h*hscale))
        
        prediction_main_frame['width']=int((1/3)*w*wscale)
        prediction_main_frame['height']=int((1/4)*h*hscale)

        prediction_mass_mode_frame['width']=int((1/3)*w*wscale)
        prediction_mass_mode_frame['height']=int((1/8)*h*hscale)
        
        prediction_mass_main_frame['width']=int((1/3)*w*wscale)
        prediction_mass_main_frame['height']=int((1/8)*h*hscale)
        
        lotus_search_criteria_listbox['height']=int(2*hscale)
        



def create_taxonomy_db_frame():
    global taxonomy_db_main_frame
    taxonomy_db_main_frame= Frame(criteria_frame, borderwidth=2, relief=GROOVE, width = int((2/3)*w) )
    taxonomy_db_main_frame.pack(side=TOP, expand=1, fill=BOTH)
    Label(taxonomy_db_main_frame, text="Taxonomy").pack(side = "top", fill=BOTH, expand=1)
    
    global taxonomy_db_subframe_1
    taxonomy_db_subframe_1 = Frame(taxonomy_db_main_frame, borderwidth=0, relief=GROOVE, width = int((2/3)*w) )
    taxonomy_db_subframe_1.pack(side=TOP, fill=BOTH, expand=1)

    
    global taxonomy_db_subframe_2
    taxonomy_db_subframe_2 = Frame(taxonomy_db_main_frame, borderwidth=0, relief=GROOVE, width = int((2/3)*w) )
    taxonomy_db_subframe_2.pack(side=TOP, fill=BOTH, expand=1)
    
    global taxonomy_db_subframe_3
    taxonomy_db_subframe_3 = Frame(taxonomy_db_main_frame, borderwidth=0, relief=GROOVE, width = int((2/3)*w) )
    taxonomy_db_subframe_3.pack(side=TOP, fill=BOTH, expand=1)
    
    # Create radiobox for Taxonomy Criteria
    global taxonomy_db_var
    taxonomy_db_var=StringVar()
    taxonomy_db_var.set("All_Taxonomy_DB") # Keep this choice !  Otherwise you won't be able to do anything else.
    global list_taxonomy_db_var
    list_taxonomy_db_var = ['','']
    # Create Radiobox for Taxonomy criteria selection
    but_BirdLife_International=Radiobutton(taxonomy_db_subframe_1, variable=taxonomy_db_var, text="BirdLife International", value="BirdLife International",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_GBIF_Backbone_Taxonomy=Radiobutton(taxonomy_db_subframe_1, variable=taxonomy_db_var, text="GBIF Backbone Taxonomy", value="GBIF Backbone Taxonomy",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_iNaturalist=Radiobutton(taxonomy_db_subframe_1, variable=taxonomy_db_var, text="iNaturalist", value="iNaturalist",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_Index_Fungorum=Radiobutton(taxonomy_db_subframe_2, variable=taxonomy_db_var, text="Index Fungorum", value="Index Fungorum",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_ITIS=Radiobutton(taxonomy_db_subframe_2, variable=taxonomy_db_var, text="ITIS", value="ITIS",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_Mammal_Species_of_the_World=Radiobutton(taxonomy_db_subframe_2, variable=taxonomy_db_var, text="Mammal Species of the World", value="Mammal Species of the World",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_NCBI=Radiobutton(taxonomy_db_subframe_3, variable=taxonomy_db_var, text="NCBI", value="NCBI",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_Open_Tree_of_Life=Radiobutton(taxonomy_db_subframe_3, variable=taxonomy_db_var, text="Open Tree of Life", value="Open Tree of Life",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_VASCAN=Radiobutton(taxonomy_db_subframe_3, variable=taxonomy_db_var, text="VASCAN", value="VASCAN",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    but_All_Taxonomy_DB=Radiobutton(taxonomy_db_subframe_3, variable=taxonomy_db_var, text="All_Taxonomy_DB", value="All_Taxonomy_DB",command=action.get_delected_taxonomy_db).pack(side='left',fill=BOTH, expand=1)
    
    

def create_criteria_subframe():
    global criteria_subframe
    criteria_subframe = Frame(criteria_frame, borderwidth=0, relief=GROOVE, width = int((2/3)*w), height = h )
    criteria_subframe.pack(side=TOP, fill=BOTH, expand=1)
    

def create_taxonomy_frame():
    global taxonomy_main_frame
    global taxonomy_family_frame
    global taxonomy_genus_frame
    global taxonomy_species_frame
    
    global taxonomy_family_listbox
    global taxonomy_genus_listbox
    global taxonomy_species_listbox
    
    global taxonomy_action_frame
    
    taxonomy_main_frame = Frame(criteria_subframe, borderwidth=0, relief=GROOVE, width= int(((2/3)*w)/2), height=h)
    taxonomy_main_frame.pack(side=LEFT, fill=BOTH, expand=1)
    
    
    # Create Taxonomy_Family Frame
    taxonomy_family_frame = Frame(taxonomy_main_frame, borderwidth=0, relief=GROOVE, width = int(((2/3)*w)/2) , height = int((h/3)-((1/3)*(h/3))))
    taxonomy_family_frame.pack(side=TOP, fill=BOTH, expand=1)
    
    # Create Taxonomy_Genus Frame
    taxonomy_genus_frame = Frame(taxonomy_main_frame, borderwidth=0, relief=GROOVE, width = int(((2/3)*w)/2) , height = int((h/3)-((1/3)*(h/3))))
    taxonomy_genus_frame.pack(side=TOP, fill=BOTH, expand=1)
    
    # Create Taxonomy_Species Frame
    taxonomy_species_frame = Frame(taxonomy_main_frame, borderwidth=0, relief=GROOVE, width = int(((2/3)*w)/2) , height = int((h/3)-((1/3)*(h/3))))
    taxonomy_species_frame.pack(side=TOP, fill=BOTH, expand=1)
    
    # Scrollbar for Taxonomy_Family Frame

    taxonomy_family_var = tk.StringVar()
    taxonomy_family_var.set('')
    global taxonomy_family_listbox
    taxonomy_family_listbox = tk.Listbox(taxonomy_family_frame, listvariable=taxonomy_family_var, width =int(((2/3)*w)/2), height = int((h/3)-((1/3)*(h/3))))
    
    taxonomy_family_scrollbar = Scrollbar(taxonomy_family_frame)
    taxonomy_family_scrollbar.pack(side = RIGHT, fill = Y)
    taxonomy_family_listbox.config(yscrollcommand = taxonomy_family_scrollbar.set)
    taxonomy_family_scrollbar.config(command = taxonomy_family_listbox.yview)
    
    # Scrollbar for Taxonomy_Genus Frame
    taxonomy_genus_var = tk.StringVar()
    taxonomy_genus_var.set('')
    global taxonomy_genus_listbox
    taxonomy_genus_listbox = tk.Listbox(taxonomy_genus_frame, listvariable=taxonomy_genus_var , width =  int(((2/3)*w)/2), height = int((h/3)-((1/3)*(h/3))))
    
    taxonomy_genus_scrollbar = Scrollbar(taxonomy_genus_frame)
    taxonomy_genus_scrollbar.pack(side = RIGHT, fill = Y)
    taxonomy_genus_listbox.config(yscrollcommand = taxonomy_genus_scrollbar.set)
    taxonomy_genus_scrollbar.config(command = taxonomy_genus_listbox.yview)
    
    # Scrollbar for Taxonomy_Species Frame
    taxonomy_species_var = tk.StringVar()
    taxonomy_species_var.set('')
    global taxonomy_species_listbox
    taxonomy_species_listbox = tk.Listbox(taxonomy_species_frame, listvariable=taxonomy_species_var, width = int(((2/3)*w)/2),height = int((h/3)-((1/3)*(h/3))))
    
    taxonomy_species_scrollbar = Scrollbar(taxonomy_species_frame)
    taxonomy_species_scrollbar.pack(side = RIGHT, fill = Y)
    taxonomy_species_listbox.config(yscrollcommand = taxonomy_species_scrollbar.set)
    taxonomy_species_scrollbar.config(command = taxonomy_species_listbox.yview)
    
    #Put Label to Taxonomy Criteria
    Label(taxonomy_family_frame, text="Family").pack(side = TOP)
    Label(taxonomy_genus_frame, text="Genus").pack(side = TOP)
    Label(taxonomy_species_frame, text="Species").pack(side = TOP)
    
    # Refresh Family, Genus and Species ListBox
    taxonomy_family_listbox.pack(side = LEFT, fill=BOTH, expand=1)
    taxonomy_genus_listbox.pack(side = LEFT, fill=BOTH, expand=1)
    taxonomy_species_listbox.pack(side = LEFT, fill=BOTH, expand=1) 
    
    taxonomy_family_listbox.bind("<<ListboxSelect>>", action.callback_genus)
    taxonomy_genus_listbox.bind("<<ListboxSelect>>", action.callback_species)
    
    
    taxonomy_action_frame = Frame(taxonomy_main_frame, borderwidth=0, relief=GROOVE, width = int(((2/3)*w)/2), height=int(((10*h)/1080)))
    taxonomy_action_frame.pack(side = TOP, fill=BOTH, expand=1)
    
    # Add Taxonomy Criteria to selected Criteria
        
    but_add_input_taxonomy_criteria = Button(taxonomy_action_frame, text = "Add to the Input", command= action.put_taxonomy_criteria_to_search_criteria)
    but_add_input_taxonomy_criteria.pack(side = LEFT, fill=BOTH, expand=1)
    
    # Create button to clean Taxonomy ListBox
    but_clean_taxonomy_criteria = Button(taxonomy_action_frame, text = "Clean", command = action.clear_taxonomy)
    but_clean_taxonomy_criteria.pack(side = LEFT, fill=BOTH, expand=1)
    
    

def create_chemontology_frame():
    # Create Chemontoly Frame
    global chemontology_main_frame
    global chemontology_pathway_frame
    global chemontology_superclass_frame
    global chemontology_class_frame
    
    global chemontology_pathway_listbox
    global chemontology_superclass_listbox
    global chemontology_class_listbox
    
    global chemontology_action_frame
    
    chemontology_main_frame = Frame(criteria_subframe, borderwidth=0, relief=GROOVE, width = int(((2/3)*w)/2) , height = int((h/3)-((1/3)*(h/3))))
    chemontology_main_frame.pack(side = LEFT, fill=BOTH, expand=1)
    
    # Create NP_Pathway Frame
    chemontology_pathway_frame = Frame(chemontology_main_frame, borderwidth=0, relief=GROOVE, width = int(((2/3)*w)/2) , height = int((h/3)-((1/3)*(h/3))))
    chemontology_pathway_frame.pack(side = TOP, fill=BOTH, expand=1)
    
    # Create NP_Superclass Frame
    chemontology_superclass_frame = Frame(chemontology_main_frame, borderwidth=0, relief=GROOVE, width =  int(((2/3)*w)/2) , height =  int((h/3)-((1/3)*(h/3))))
    chemontology_superclass_frame.pack(side = TOP, fill=BOTH, expand=1)
    
    # Create NP_Class Frame
    chemontology_class_frame = Frame(chemontology_main_frame, borderwidth=0, relief=GROOVE, width =  int(((2/3)*w)/2) , height =  int((h/3)-((1/3)*(h/3))))
    chemontology_class_frame.pack(side = TOP, fill=BOTH, expand=1)
    
#     ##############################################################################################
    
    
    # Scrollbar for NP_Pathway Frame
    
    chemontology_pathway_var = tk.StringVar()
    chemontology_pathway_var.set('')
    global chemontology_pathway_listbox
    chemontology_pathway_listbox = tk.Listbox(chemontology_pathway_frame, listvariable=chemontology_pathway_var, width = int(((2/3)*w)/2), height = int((h/3)-((1/3)*(h/3))))
    chemontology_pathway_scrollbar = Scrollbar(chemontology_pathway_frame)
    chemontology_pathway_scrollbar.pack(side = RIGHT, fill = BOTH)
    chemontology_pathway_listbox.config(yscrollcommand = chemontology_pathway_scrollbar.set)
    chemontology_pathway_scrollbar.config(command = chemontology_pathway_listbox.yview)
    
    
    # Scrollbar for NP_Superclass Frame
    chemontology_superclass_var = tk.StringVar()
    chemontology_superclass_var.set('')
    global chemontology_superclass_listbox
    chemontology_superclass_listbox = tk.Listbox(chemontology_superclass_frame, listvariable=chemontology_superclass_var, width =int(((2/3)*w)/2), height = int((h/3)-((1/3)*(h/3))))
    chemontology_superclass_scrollbar = Scrollbar(chemontology_superclass_frame)
    chemontology_superclass_scrollbar.pack(side = RIGHT, fill = BOTH)
    chemontology_superclass_listbox.config(yscrollcommand = chemontology_superclass_scrollbar.set)
    chemontology_superclass_scrollbar.config(command = chemontology_superclass_listbox.yview)
    
    # Scrollbar for NP_Class Frame
    chemontology_class_var = tk.StringVar()
    chemontology_class_var.set('')
    global chemontology_class_listbox
    chemontology_class_listbox = tk.Listbox(chemontology_class_frame, listvariable=chemontology_class_var, width = int(((2/3)*w)/2), height = int((h/3)-((1/3)*(h/3))))
    chemontology_class_scrollbar = Scrollbar(chemontology_class_frame)
    chemontology_class_scrollbar.pack(side = RIGHT, fill = BOTH)
    chemontology_class_listbox.config(yscrollcommand = chemontology_class_scrollbar.set)
    chemontology_class_scrollbar.config(command = chemontology_class_listbox.yview)
    
    # Put Label to Chemontoly Criteria
    Label(chemontology_pathway_frame, text="NP_Pathway").pack(side = TOP)
    Label(chemontology_superclass_frame, text="NP_Superclass").pack(side = TOP)
    Label(chemontology_class_frame, text="NP_Class").pack(side = TOP)
    
    chemontology_pathway_listbox.pack(side = LEFT, fill=BOTH, expand=1)
    chemontology_superclass_listbox.pack(side = LEFT, fill=BOTH, expand=1) 
    chemontology_class_listbox.pack(side = LEFT, fill=BOTH, expand=1) 
    
    chemontology_pathway_listbox.bind("<<ListboxSelect>>", action.callback_Superclass)
    chemontology_superclass_listbox.bind("<<ListboxSelect>>", action.callback_Class)
    
    chemontology_action_frame = Frame(chemontology_main_frame, borderwidth=0, relief=GROOVE, width = int((((2/3)*w)/2)),  height=int(((10*h)/1080)))
    chemontology_action_frame.pack(side = TOP, fill=BOTH, expand=1)
    #Add Taxonomy Criteria to selected Criteria
    but_add_input_chemontology_criteria = Button(chemontology_action_frame, text = "Add to the Input", command= action.put_chemontology_criteria_to_search_criteria)
    but_add_input_chemontology_criteria.pack(side = LEFT, fill=BOTH, expand=1)
    
    # Create button to clean Taxonomy ListBox
    but_clean_chemontology_criteria = Button(chemontology_action_frame, text = "Clean", command= action.clear_chemontology)
    but_clean_chemontology_criteria.pack(side = LEFT, fill=BOTH, expand=1)

    action.get_NPclassifierPathway()

def create_action_subframe():
    global action_subframe_1
    global lotus_search_criteria_frame
  
    
    global prediction_main_frame, prediction_mass_main_frame, prediction_mass_mode_frame
    
    # Create a Frame for the actions you want to do on selected criteria
    action_subframe_1 = Frame(action_main_frame, borderwidth=2, relief=GROOVE, width = int((1/3)*w), height=int(((1/4)*h)))
    action_subframe_1.pack(side = TOP,  fill=BOTH,expand=1 )
    Label(action_subframe_1, text="Selected categories").pack()
    
    lotus_search_criteria_var = tk.StringVar()
    lotus_search_criteria_var.set('')
    global lotus_search_criteria_listbox
    lotus_search_criteria_listbox = tk.Listbox(action_subframe_1, listvariable=lotus_search_criteria_var, width = int((1/3)*w), height=2)
    lotus_search_criteria_listbox.pack(side = LEFT, fill = BOTH, expand=1) 
    lotus_search_criteria_scrollbar = Scrollbar(lotus_search_criteria_listbox)
    lotus_search_criteria_scrollbar.pack(side = RIGHT, fill = Y)
    lotus_search_criteria_listbox.config(yscrollcommand = lotus_search_criteria_scrollbar.set)
    lotus_search_criteria_scrollbar.config(command = lotus_search_criteria_listbox.yview)


    # Create a Frame to mokae lotus search
    lotus_search_criteria_frame = Frame(action_main_frame, borderwidth=0, relief=GROOVE,width = int((1/3)*w), height=int(((1/4)*h)))
    lotus_search_criteria_frame.pack(side = TOP, fill=BOTH, expand=1)
    
    # Create button to chose which type of research you want to do
    but_search_on_all_criteria = tk.Button(lotus_search_criteria_frame, text='Get all categories', command= ginfo.get_lotus_add)
    but_search_on_all_criteria.pack(side= TOP,  fill=BOTH, expand=1)
    
    but_combined_search = tk.Button(lotus_search_criteria_frame, text='Get chemical class in family', command=ginfo.get_lotus_or )
    but_combined_search.pack(side= TOP,  fill=BOTH, expand=1)
    
    but_clean_lotus_search_selected_criteria = Button(lotus_search_criteria_frame, text = "Clean selection", command=action.clear_selected_search_criteria)
    but_clean_lotus_search_selected_criteria.pack(side= TOP,  fill=BOTH, expand=1)
    
    but_clean_lotus_search_all_criteria = Button(lotus_search_criteria_frame, text = "Clean all selection", command= action.clear_all_search_criteria)
    but_clean_lotus_search_all_criteria.pack(side= TOP,  fill=BOTH, expand=1)


    # Create Action Frame for prediction of NMR and MSMS spectra
    prediction_main_frame = Frame(action_main_frame, borderwidth=2, relief=GROOVE, width = int((1/3)*w), height=int(((1/4)*h)))
    prediction_main_frame.pack(side = TOP,   fill=BOTH, expand=1)
    #Label(prediction_main_frame, text="What do you want to do ?").pack()
    
    # Create a Frame for MSMS spectra prediction
    prediction_mass_main_frame = Frame(prediction_main_frame, borderwidth=0, relief=GROOVE, width =  int((1/3)*w), height=int(((1/8)*h)))
    prediction_mass_main_frame.pack(side = TOP,  fill=BOTH,expand=1)
    
    global prediction_mass_mode_var
    prediction_mass_mode_var=StringVar()
    prediction_mass_mode_var.set("[M+H]+")
    
    #Create a Frame to chose the Ionization mode (ESI+/ESI-)
    prediction_mass_mode_frame = Frame(prediction_mass_main_frame, borderwidth=0, relief=GROOVE,  width = int((1/3)*w), height=int(((1/8)*h)))
    prediction_mass_mode_frame.pack(side = TOP,   fill=BOTH,expand=1)
    
    # Create the buttons for the action you want to execute
    but_prediction_mass = Button(prediction_mass_main_frame, text = "Predict MS/MS spectra", command= prediction.predict_MSMS_spectra)
    but_prediction_mass.pack(side= TOP, fill=BOTH, expand=1)
    
    #Create Radiobutton to chose the mode
    but_prediction_mass_positive=Radiobutton(prediction_mass_mode_frame, variable=prediction_mass_mode_var, text="[M+H]+", value="[M+H]+").pack(side='left', fill=BOTH, expand=1)
    but_prediction_mass_negative=Radiobutton(prediction_mass_mode_frame, variable=prediction_mass_mode_var, text="[M-H]-", value="[M-H]-").pack(side='left', fill=BOTH, expand=1)
    
    but_prediction_nmr = Button(prediction_main_frame, text = "Predict 13C NMR Chemical Shifts", command = prediction.predict_13C_nmr_chemical_shifts)
    but_prediction_nmr.pack(side = TOP,  fill=BOTH, expand=1)
    
    but_preiction_both_properties = Button(prediction_main_frame, text = "Predict both properties", command= prediction.predict_both_properties)
    but_preiction_both_properties.pack(side = TOP, fill=BOTH, expand=1) 
    
    but_draw_sunburst = Button(prediction_main_frame, text = "Chemical distribution", command= action.draw_db_chemical_space_sunburst)
    but_draw_sunburst.pack(side = TOP, fill=BOTH, expand=1) 




def create_lotus_id_frame():
    global lotus_id_main_frame

    
    # Create LOTUS_ID searchable Frame
    lotus_id_main_frame = Frame(action_main_frame, borderwidth=2, relief=GROOVE,width = int((1/3)*w), height = int((1/8)*h))
    lotus_id_main_frame.pack(side = TOP, fill=BOTH,expand=1)
    Label(lotus_id_main_frame, text="Enter LOTUS ID (ex : LTS0193685)").pack()
    
    
    # TextVariable to write a LOTUS_ID to search in LOTUS
    lotus_id_var = StringVar(lotus_id_main_frame, value='')
    global lotus_id_entry
    lotus_id_entry = Text(lotus_id_main_frame) #### Entry(lotus_id_main_frame, textvariable=lotus_id_var)
    lotus_id_entry.pack(side =TOP, fill=BOTH, expand=1)
    
    # Create Button for LOTUS_ID single search
    but_search_lotus_id = Button(lotus_id_main_frame, text = "Get LOTUS ID input", command= action.put_lotus_id_criteria_to_search_criteria)
    but_search_lotus_id.pack(side =TOP, fill=BOTH, expand=1)  

def create_molecular_formula_frame():
    global molecular_formula_main_frame

    
    # Create a Formula searchabel Frame
    molecular_formula_main_frame = Frame(action_main_frame, borderwidth=2, relief=GROOVE, width = int((1/3)*w), height =int((1/8)*h))
    molecular_formula_main_frame.pack(side = TOP, fill=BOTH,expand=1)
    Label(molecular_formula_main_frame, text="Enter Chemical formula (ex : C6H12O6)").pack()

    molecular_formula_var = StringVar(molecular_formula_main_frame, value='')
    global molecular_formula_entry
    molecular_formula_entry = Entry(molecular_formula_main_frame, textvariable=molecular_formula_var)
    molecular_formula_entry.pack(side =TOP, fill=BOTH, expand=1)
    
    # Create a button for the Formula research
    b_formula = Button(molecular_formula_main_frame, text = "Add to the input", command= action.put_molecular_formula_criteria_to_search_criteria)
    b_formula.pack(side =TOP, fill=BOTH, expand=1) 

def get_taxonomy_db_var():
    choice_taxonomy_db_var  = taxonomy_db_var.get()
    return choice_taxonomy_db_var
    
def get_prediction_mass_mode_var():
    choice_prediction_mass_mode_var = prediction_mass_mode_var.get()
    return choice_prediction_mass_mode_var

