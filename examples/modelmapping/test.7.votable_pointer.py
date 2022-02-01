"""
Created on Feb 26, 2021

@author: laurentmichel
"""
import os

from astropy.io.votable import parse
from astropy.io.votable.tree import VOTableFile, Resource, ModelMapping

data_path = os.path.dirname(os.path.realpath(__file__))

"""
Read out Test
"""

# Read a valid VOTable
# No invalid element detected,
# The block is returned as an XML String
vpath = os.path.join(data_path, "test.7.xml")
votable = parse(vpath)
for resource in votable.resources:
    print(f"Resource type: {resource.type}  Mapping block: {resource.model_mapping}")

    for resource_meta in resource.resources:
        print(f"Resource type: {resource_meta.type} Mapping block:")
        print(resource_meta.model_mapping)

# Read an invalid VOTable   
# An unexpected element has been found in the mappin block
# The mapping block pointer returns a block with just REPORT in error     
vpath = os.path.join(data_path, "test.7.ko.xml")
votable = parse(vpath)
for resource in votable.resources:
    print(f"Resource type: {resource.type}  Mapping block: {resource.model_mapping}")

    for resource_meta in resource.resources:
        print(f"Resource type: {resource_meta.type} Mapping block:")
        print(resource_meta.model_mapping)
 
 
"""
Write Test
"""       
vpath = os.path.join(data_path, "test.7.out.xml")

# Create am empty VOTable
votable = VOTableFile()
# Create the resource that will host both data table and mapping resource.
resource = Resource()
resource.type = "results"
# Create the resource that will host the mapping.
meta_resource = Resource()
meta_resource.type = "meta"
# A dummy mapping block for the test.
resource.resources.append(meta_resource)
model_mapping = ModelMapping("""
<dm-mapping:VODML xmlns:dm-mapping="http://www.ivoa.net/xml/merged-syntax" >
  <dm-mapping:REPORT/>
  <dm-mapping:GLOBALS/>
</dm-mapping:VODML>
"""
)
# Add the mapping resource
meta_resource.model_mapping = model_mapping
votable.resources.append(resource)
# Save the VOTable
votable.to_xml(vpath)
# and read it again to retrieve the mapping 
with open(vpath) as result:
    print(result.read())