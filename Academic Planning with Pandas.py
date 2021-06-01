import pandas as pd
import numpy as np



def file_scraper(file):
    open_file = open(file, 'r')
    lst = []
    for line in open_file:
        lst.append(line.strip())
    
    
    return lst


def dict_maker(lst):
    dict = {}
    comp_sci = []
    finance = []
    other = []
    electives = []
    bounds = []
    header = []
    
    
    for i in range(len(lst) - 1):
        if lst[i][-1] == ':':
            header.append(lst[i])
            beta = lst.index(lst[i])
            bounds.append(beta)
      
    for i in range(bounds[0] + 1, bounds[1]):
        comp_sci.append(lst[i])
    
    dict[header[0]] = comp_sci

    for i in range(bounds[1] + 1, bounds[2]):
        finance.append(lst[i])       
    
    dict[header[1]] = finance
    
    for i in range(bounds[2] + 1, bounds[3]):
        other.append(lst[i])
    
    dict[header[2]] = other
    
    for i in range(bounds[3] + 1, len(lst)):
        electives.append(lst[i])
    
    dict[header[3]] = electives
        
    while len(comp_sci) != len(electives):
        comp_sci.append(np.NAN)
    
    while len(finance) != len(electives):
        finance.append(np.NAN)
    
    while len(other) != len(electives):
        other.append(np.NAN)
    

    return dict
    

def data_vis(dict):
    data = pd.DataFrame(dict)
    print(data)

def schedule():
    bool = True
    
    term_classes = []
    credit = 0
    
    while bool:
        alpha = input("Please enter a valid class:")
        term_classes.append(alpha)
        for char in alpha:
            try:
                credit += int(char)
            except ValueError:
                continue
                
        if alpha == 'done':
            term_classes[-1] = credit
            bool = False
            
    dict = {'Spring21': term_classes,}
    
    data = pd.DataFrame(dict)
    print(data)    
        

def main():
    file = '/Users/shashankasharma/cs_stuff/projects/classes.txt'
    lst = file_scraper(file)
    alpha = dict_maker(lst)
    data_vis(alpha)
    schedule()
    print("This is the end of the code!")
    
main()

