'''
Created on 16 Mar 2023

@author: laurentmichel
'''
from astropy.io.votable.table import parse
from astropy.utils.data import get_pkg_data_filename

def squash_xml(data):
    return data.replace(' ', '').replace('\n', '').replace('"', '').replace("'", '')

if __name__ == '__main__':
    # test the mapping block extraction from a file
    votable = parse(get_pkg_data_filename('data/mivot_annnotated_table.xml'))
    ref_data = ""
    for resource in votable.resources:
        print(squash_xml(resource.mivot_block.content))
        with open(get_pkg_data_filename('data/mivot_block.xml')) as reference:
                ref_data = reference.read()
                print(squash_xml(ref_data))
    print(len(resource.tables))
    
    
    
    
    