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
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from packages import gui, ginfo, tool_path



def get_delected_taxonomy_db():
    selected_taxonomy_db  = gui.get_taxonomy_db_var()
    print(str(datetime.now()) +" The Taxonomy you have chosen is: " + selected_taxonomy_db +".")
    global taxonomy_family_list
    taxonomy_family_list = []
    global taxonomy_dataframe_1
    if selected_taxonomy_db != "All_Taxonomy_DB":    # if All_Taxonomy_DB not chosen, get Family_list from chosen Taxonomy criteria
        taxonomy_dataframe_1 = ginfo.get_taxonomy_file()[0].loc[ginfo.get_taxonomy_file()[0]['Taxonomy_DB'] == selected_taxonomy_db]
        
        for family in taxonomy_dataframe_1['family'].to_list():
            if family not in taxonomy_family_list:
                taxonomy_family_list.append(str(family))
     
    else : 
        for family in ginfo.get_taxonomy_file()[1]['family'].to_list(): # if All_Taxonomy_DB has been chosen, get Family_list for general 
            if family not in taxonomy_family_list:
                taxonomy_family_list.append(str(family))
    taxonomy_family_sorted_list = sorted(taxonomy_family_list)
    clear_taxonomy()
    
    for unique_family in taxonomy_family_sorted_list:
        gui.taxonomy_family_listbox.insert('end', unique_family)
    gui.taxonomy_family_listbox.pack()
    
# Get Genus_list from corresponding family and Taxonomy
def get_genus(family):
    taxonomy_unique_genus_list = []
    global taxonomy_dataframe_2
    selected_taxonomy_family  = gui.get_taxonomy_db_var()
    if selected_taxonomy_family != "All_Taxonomy_DB":
        taxonomy_dataframe_2 = taxonomy_dataframe_1.loc[taxonomy_dataframe_1['family'] == family]
    else :
        taxonomy_dataframe_2 = ginfo.get_taxonomy_file()[1].loc[ginfo.get_taxonomy_file()[1]['family'] == family]
    for genus in taxonomy_dataframe_2['genus'].to_list():
        
        if genus not in taxonomy_unique_genus_list:
            taxonomy_unique_genus_list.append(genus)
    return sorted(taxonomy_unique_genus_list)
    

# Get Species_list from corresponding genus and Taxonomy
def get_species(genus):
    taxonomy_species_list = []
    taxonomy_dataframe_3 = taxonomy_dataframe_2.loc[taxonomy_dataframe_2['genus'] == genus]
    for species in taxonomy_dataframe_3['species'].to_list():
        if species not in taxonomy_species_list:
            taxonomy_species_list.append(species)
    return sorted(taxonomy_species_list)

#Function to clean Genus and Species ListBox
def clear_taxonomy():
    gui.taxonomy_family_listbox.delete(0, END)
    gui.taxonomy_genus_listbox.delete(0, END)
    gui.taxonomy_species_listbox.delete(0, END)
    

# Put Genus list in ListBox 
def callback_genus(event):
    taxonomy_selected_family_event = event.widget.curselection()
    
    
    if taxonomy_selected_family_event:
        gui.taxonomy_genus_listbox.delete(0, END)
        taxonomy_selected_family_index = taxonomy_selected_family_event[0]
        taxonomy_selected_family = event.widget.get(taxonomy_selected_family_index)
        print(str(datetime.now()) + " The Family you have chosen is: " + str(taxonomy_selected_family) + ".")
        taxonomy_corresponding_genus_list = get_genus(taxonomy_selected_family)
        
        gui.taxonomy_genus_listbox.delete(0, END)
        for genus in taxonomy_corresponding_genus_list:
            gui.taxonomy_genus_listbox.insert('end', genus)
        gui.taxonomy_genus_listbox.pack()
        gui.taxonomy_species_listbox.delete(0, END)

# Put Species list in ListBox
def callback_species(event):
    taxonomy_selected_genus_event = event.widget.curselection()
    
    if taxonomy_selected_genus_event:
        gui.taxonomy_species_listbox.delete(0, END)
        taxonomy_selected_genus_index = taxonomy_selected_genus_event[0]
        taxonomy_selected_genus = event.widget.get(taxonomy_selected_genus_index)
        print(str(datetime.now()) + " The Genus you have chosen is: " + str(taxonomy_selected_genus) + ".")
        taxonomy_corresponding_species_list= get_species(taxonomy_selected_genus)
        for species in taxonomy_corresponding_species_list:
            gui.taxonomy_species_listbox.insert('end', species)
        gui.taxonomy_species_listbox.pack()
        
# Get the NP_Pathway
def get_NPclassifierPathway():
    chemontology_NPclassifierPathway_list = []
    
    for pathway in ginfo.get_chemontology_file()['chemicalTaxonomyNPclassifierPathway'].to_list():
        if pathway not in chemontology_NPclassifierPathway_list:
            chemontology_NPclassifierPathway_list.append(str(pathway))
    chemontology_NPclassifierPathway_sorted_list =  sorted(chemontology_NPclassifierPathway_list)
    clear_chemontology()
    for NPclassifierPathway in chemontology_NPclassifierPathway_sorted_list:
        gui.chemontology_pathway_listbox.insert('end', NPclassifierPathway)
    gui.chemontology_pathway_listbox.pack()
    

# Get the NP_Superclass corresponding to the chosen NP_Pathway
def get_NPclassifierSuperclass(chemicalTaxonomyNPclassifierPathway):
    chemontology_NPclassifieSuperclass_list = []
    global chemontology_dataframe_1
    chemontology_dataframe_1 = ginfo.get_chemontology_file().loc[ginfo.get_chemontology_file()['chemicalTaxonomyNPclassifierPathway'] == chemicalTaxonomyNPclassifierPathway]
    for NPclassifierSuperclass in chemontology_dataframe_1['chemicalTaxonomyNPclassifierSuperclass'].to_list():
        if NPclassifierSuperclass not in chemontology_NPclassifieSuperclass_list:
            chemontology_NPclassifieSuperclass_list.append(str(NPclassifierSuperclass))
    return sorted(chemontology_NPclassifieSuperclass_list)

# Get the NP_Superclass corresponding to the chosen NP_Class
def get_NPclassifierClass(chemicalTaxonomyNPSuperclass):
    chemontology_NPclassifierClass_list = []
    chemontology_dataframe_2 = chemontology_dataframe_1.loc[chemontology_dataframe_1['chemicalTaxonomyNPclassifierSuperclass'] == chemicalTaxonomyNPSuperclass]
    for NPclassifierClass in chemontology_dataframe_2['chemicalTaxonomyNPclassifierClass'].to_list():
        if NPclassifierClass not in chemontology_NPclassifierClass_list:
            chemontology_NPclassifierClass_list.append(str(NPclassifierClass))
    return sorted(chemontology_NPclassifierClass_list)
    
# Clean Chemontology Criteria
def clear_chemontology():
    gui.chemontology_superclass_listbox.delete(0, END)
    gui.chemontology_class_listbox.delete(0, END)

# Get NP_Superclass in ListBox
def callback_Superclass(event):
    chemontology_selected_NPclassifierPathway_event = event.widget.curselection()
    if chemontology_selected_NPclassifierPathway_event:
        gui.chemontology_superclass_listbox.delete(0, END)
        chemontology_selected_NPclassifierPathway_index = chemontology_selected_NPclassifierPathway_event[0]
        chemontology_selected_NPclassifierPathway = event.widget.get(chemontology_selected_NPclassifierPathway_index)
        print(str(datetime.now()) + " The NP_Pathway you have chosen is: " + chemontology_selected_NPclassifierPathway +".")
        chemontology_corresponding_NPclassifierSuperclass_list = get_NPclassifierSuperclass(chemontology_selected_NPclassifierPathway)
        for NPclassifierSuperclass in chemontology_corresponding_NPclassifierSuperclass_list:
            gui.chemontology_superclass_listbox.insert('end', NPclassifierSuperclass)
        
        gui.chemontology_superclass_listbox.pack()
        gui.chemontology_class_listbox.delete(0, END)


# Get NP_Class in ListBox
def callback_Class(event):
    chemontology_selected_NPclassifierSuperclass_event = event.widget.curselection()
    if chemontology_selected_NPclassifierSuperclass_event:
        gui.chemontology_class_listbox.delete(0, END)
        chemontology_selected_NPclassifierSuperclass_index = chemontology_selected_NPclassifierSuperclass_event[0]
        chemontology_selected_NPclassifierSuperclass = event.widget.get(chemontology_selected_NPclassifierSuperclass_index)
        print(str(datetime.now()) + " The Taxonomy you have chosen is: " + chemontology_selected_NPclassifierSuperclass +".")
        chemontology_corresponding_NPclassifierClass_list = get_NPclassifierClass(chemontology_selected_NPclassifierSuperclass)
        for NPclassifierClass in chemontology_corresponding_NPclassifierClass_list:
            gui.chemontology_class_listbox.insert('end', NPclassifierClass)
        gui.chemontology_class_listbox.pack()
        
        
        
        
        
        
def put_lotus_id_criteria_to_search_criteria(): ########################################################230208
    selected_taxonomy_db  = gui.get_taxonomy_db_var()
    
    lotus_id_selected = str(gui.lotus_id_entry.get(1.0, "end-1c")) #####################################230208
    lotus_id_selected = lotus_id_selected.strip('\n').split('\n')
    for x in lotus_id_selected:
    
        if 'LTS' not in x : # Is the text correspondinf to a valid LOTUS_ID ?
            messagebox.showinfo("Info", "This is not a LOTUS ID (ex : LTS0193685), try again !")
            gui.lotus_id_entry.delete(1.0, "end-1c") ################################230208
            print(str(datetime.now()) + " Bad LOTUS_ID request.")
        else:
            value= str(x)
            code = 'LTS : ' + selected_taxonomy_db 
            gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + value))
           
            gui.lotus_search_criteria_listbox.pack()
            print(str(datetime.now()) + " You have added " + str(code + ' : ' + value) + " to the selection.")
    messagebox.showinfo("Info", "Lotus_ID added!")
    gui.lotus_id_entry.delete(1.0, "end-1c") #### END 230208

def put_molecular_formula_criteria_to_search_criteria():    
    selected_taxonomy_db  = gui.get_taxonomy_db_var()
    molecular_formula_selected = str(gui.molecular_formula_entry.get())
    molecular_formula_selected = molecular_formula_selected.upper()
    code = 'F : ' + selected_taxonomy_db + ' : '
    gui.lotus_search_criteria_listbox.insert('end', str( code + molecular_formula_selected))
    gui.lotus_search_criteria_listbox.pack()
    print(str( '(F) : ' + molecular_formula_selected + " has been added to the selection."))
    messagebox.showinfo("Info", "Formula added!")
    gui.molecular_formula_entry.delete(0, END)
    
# list the selected_criteria
def get_selected_search_criteria_list():
    global selected_criteria_list
    if not list(gui.lotus_search_criteria_listbox.get('@1,0', END)):
        selected_criteria_list = ['']
        return selected_criteria_list
    else:
        selected_criteria_list = list(gui.lotus_search_criteria_listbox.get('@1,0', END))
        #messagebox.showinfo("Info", ("You have chosen : " + str(selected_criteria_list) + " as input(s)."))
        print(str(datetime.now()) + " " + str(selected_criteria_list))
        return selected_criteria_list

# Clean all Criteria Frame
def clear_all_search_criteria():
    gui.taxonomy_family_listbox.delete(0, END)
    gui.taxonomy_family_listbox.pack()
        
    gui.taxonomy_genus_listbox.delete(0, END)
    gui.taxonomy_genus_listbox.pack()
    
    gui.taxonomy_species_listbox.delete(0, END)
    gui.taxonomy_species_listbox.pack()
      
    gui.chemontology_superclass_listbox.delete(0, END)
    gui.chemontology_superclass_listbox.pack()
    
    gui.chemontology_class_listbox.delete(0, END)
    gui.chemontology_class_listbox.pack()
    
    gui.lotus_search_criteria_listbox.delete(0, END)
    gui.lotus_search_criteria_listbox.pack()
    
    print(str(datetime.now()) + " All selection is clean.")

# Clean Selected Criteria Frame
def clear_selected_search_criteria():
    if not list(gui.lotus_search_criteria_listbox.get('@1,0', END)):
        print(str(datetime.now()) + " What do you want to delete ?")
    else:
        gui.lotus_search_criteria_listbox.delete(0, END)
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " All selection is clean.")

# Function to add Taxonomy criteria to selected criteria to search in LOTUS_DB
def put_taxonomy_criteria_to_search_criteria():
    selected_taxonomy_db  = gui.get_taxonomy_db_var()
    if gui.taxonomy_family_listbox.curselection():
        taxonomy_selected_family = gui.taxonomy_family_listbox.get(gui.taxonomy_family_listbox.curselection())
        code = 'T : ' + selected_taxonomy_db +' : family'
        gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + taxonomy_selected_family))
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " You have added " + str(code + ' : ' + taxonomy_selected_family) + " to the selection.") 
        messagebox.showinfo("Info", "family added!")
    elif gui.taxonomy_genus_listbox.curselection():
        taxonomy_selected_genus = gui.taxonomy_genus_listbox.get(gui.taxonomy_genus_listbox.curselection())
        code = 'T : ' + selected_taxonomy_db +' : genus'
        gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + taxonomy_selected_genus))
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " You have added " + str(code + ' : ' + taxonomy_selected_genus) + " to the selection.")
        messagebox.showinfo("Info", "genus added!")
    elif gui.taxonomy_species_listbox.curselection():
        taxonomy_selected_species = gui.taxonomy_species_listbox.get(gui.taxonomy_species_listbox.curselection())
        code = 'T : ' + selected_taxonomy_db +' : species'
        gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + taxonomy_selected_species))
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " You have added " + str(code + ' : ' + taxonomy_selected_species) + " to the selection.")
        messagebox.showinfo("Info", "species added!")
        
# Function to add Chemontology criteria to selected criteria to search in LOTUS_DB
def put_chemontology_criteria_to_search_criteria():
    selected_taxonomy_db = gui.get_taxonomy_db_var()
    if gui.chemontology_pathway_listbox.curselection():
        chemontology_selected_NPclassifierPathway = gui.chemontology_pathway_listbox.get(gui.chemontology_pathway_listbox.curselection())
        code = 'C : ' + selected_taxonomy_db +' : NP : chemicalTaxonomyNPclassifierPathway'  
        gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + chemontology_selected_NPclassifierPathway))
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " You have added " + str(code +  ' : ' + chemontology_selected_NPclassifierPathway) + " to the selection.")
        messagebox.showinfo("Info", "NP_Pathway added!")
    elif gui.chemontology_superclass_listbox.curselection():
        chemontology_selected_NPclassifierSuperclass = gui.chemontology_superclass_listbox.get(gui.chemontology_superclass_listbox.curselection())
        code = 'C : '+ selected_taxonomy_db + ' : NP : chemicalTaxonomyNPclassifierSuperclass'
        gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + chemontology_selected_NPclassifierSuperclass))
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " You have added " + str(code + ' : ' + chemontology_selected_NPclassifierSuperclass) + " to the selection.")
        messagebox.showinfo("Info", "NP_Superclass added!")
    elif gui.chemontology_class_listbox.curselection():
        chemontology_selected_NPclassifierClass = gui.chemontology_class_listbox.get(gui.chemontology_class_listbox.curselection())
        code = 'C : ' + selected_taxonomy_db + ' : NP : chemicalTaxonomyNPclassifierClass'
        gui.lotus_search_criteria_listbox.insert('end', str(code + ' : ' + chemontology_selected_NPclassifierClass))
        gui.lotus_search_criteria_listbox.pack()
        print(str(datetime.now()) + " You have added " + str(code + ' : ' + chemontology_selected_NPclassifierClass) + " to the selection.")
        messagebox.showinfo("Info", "NP_Class added!")

# Function to delete selected criteria
def clear_selected_search_criteria():
    if not list(gui.lotus_search_criteria_listbox.get('@1,0', END)):
        print(str(datetime.now()) + " What do you want to delete ?")
    else:
        if gui.lotus_search_criteria_listbox.curselection():
            value = gui.lotus_search_criteria_listbox.curselection()
            gui.lotus_search_criteria_listbox.delete(value)
            gui.lotus_search_criteria_listbox.pack()
            print(str(datetime.now()) + " Selection clean.")

# Create a sunburst in order to show the chemodiversity of the generated database
def draw_db_chemical_space_sunburst():
    if not os.path.exists(tool_path.get_current_path()[0] + '/LOTUS_DB_input/cfmid_input.tsv'):
        messagebox.showinfo("Info", "You must have a cfmid_input file.tsv before making sunburst !") 
        print(tool_path.get_current_path()[0])
    else:
    
      

        input_metadata_dataframe=pd.read_csv(tool_path.get_current_path()[0] + '/LOTUS_DB_input/cfmid_input.tsv', sep='\t')
        input_metadata_dataframe['merged'] = ''
        for i in range(len(input_metadata_dataframe["chemicalTaxonomyNPclassifierClass"].to_list())):
            input_metadata_dataframe['merged'][i] = str(input_metadata_dataframe['chemicalTaxonomyNPclassifierPathway'][i])+str(input_metadata_dataframe['chemicalTaxonomyNPclassifierSuperclass'][i])+str(input_metadata_dataframe['chemicalTaxonomyNPclassifierClass'][i])
        #df from cfmid_input, chemical class annotation
        class_iterations= input_metadata_dataframe["merged"].value_counts()
        class_iterations_dataframe = pd.DataFrame(class_iterations)
        class_iterations_dataframe = class_iterations_dataframe.reset_index()
        class_iterations_dataframe.columns=["merged", "Number of molecules"]
        #merge df and counted df
        class_iterations_dataframe_merged = class_iterations_dataframe.merge(
            input_metadata_dataframe[['chemicalTaxonomyNPclassifierPathway','chemicalTaxonomyNPclassifierSuperclass','chemicalTaxonomyNPclassifierClass', 'merged']], how='inner', on='merged').drop_duplicates().reset_index(drop=True)
        #change name (add ' ' or '   ') to avoid duplicates 
        i = 0
        while i != len(class_iterations_dataframe_merged['chemicalTaxonomyNPclassifierClass']):
            class_iterations_dataframe_merged['chemicalTaxonomyNPclassifierClass'][i] = str(str(class_iterations_dataframe_merged['chemicalTaxonomyNPclassifierClass'][i]) + str('  '))
            i = i+1
        i = 0
        while i != len(class_iterations_dataframe_merged['chemicalTaxonomyNPclassifierSuperclass']):
            class_iterations_dataframe_merged['chemicalTaxonomyNPclassifierSuperclass'][i] = str(str(class_iterations_dataframe_merged['chemicalTaxonomyNPclassifierSuperclass'][i]) + str(' '))
            i = i+1
        #define levels
        levels = ['chemicalTaxonomyNPclassifierClass','chemicalTaxonomyNPclassifierSuperclass'] # levels used for the hierarchical chart
        value_column = 'Number of molecules'
        #Make Hierachy
        
        hierarchical_tree_dataframe = build_hierarchical_dataframe(class_iterations_dataframe_merged, levels, value_column)
        
        #create sunburst
        fig = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]],)

        fig.add_trace(go.Sunburst(
            labels=hierarchical_tree_dataframe['id'],
            parents=hierarchical_tree_dataframe['parent'],
            values=hierarchical_tree_dataframe['value'],
            branchvalues='total' ))

        fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
        fig.show()
        
        #export sunburst to html file
        fig.write_html(tool_path.get_current_path()[0] + '/sunburst/' + str(datetime.now()).replace(' ', '_').replace(':', '_').replace('.','_') + '_sunburst.html')
        
    
def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
        """
        Build a hierarchy of levels for Sunburst or Treemap charts.

        Levels are given starting from the bottom to the top of the hierarchy,
        ie the last level corresponds to the root.
        """
        
        hierarchical_tree_dataframe = pd.DataFrame(columns=['id', 'parent', 'value'])
        for i, level in enumerate(levels):
            df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
            dfg = df.groupby(levels[i:]).sum()
            dfg = dfg.reset_index()
            df_tree['id'] = dfg[level].copy()
            if i < len(levels) - 1:
                df_tree['parent'] = dfg[levels[i+1]].copy()
            else:
                df_tree['parent'] = 'Organic Compound'
            df_tree['value'] = dfg[value_column]
            hierarchical_tree_dataframe = hierarchical_tree_dataframe.append(df_tree, ignore_index=True)
        total = pd.Series(dict(id='Organic Compound', parent='', value=df[value_column].sum()))
    
        return hierarchical_tree_dataframe
