"""
Created on Feb 26, 2021

@author: laurentmichel
"""
import os

from astropy.io.votable import parse
from astropy.io.votable.tree import VOTableFile, Resource, ModelMapping

data_path = os.path.dirname(os.path.realpath(__file__))
vpath = os.path.join(data_path, "test.7.xml")
votable = parse(vpath)
for resource in votable.resources:
    print(f"Resource type: {resource.type}  Mapping block: {resource.model_mapping}")

    for resource_meta in resource.resources:
        print(f"Resource type: {resource_meta.type} Mapping block:")
        print(resource_meta.model_mapping)
        
vpath = os.path.join(data_path, "test.7.ko.xml")
votable = parse(vpath)
for resource in votable.resources:
    print(f"Resource type: {resource.type}  Mapping block: {resource.model_mapping}")

    for resource_meta in resource.resources:
        print(f"Resource type: {resource_meta.type} Mapping block:")
        print(resource_meta.model_mapping)
 
 
        
vpath = os.path.join(data_path, "test.7.out.xml")

votable = VOTableFile()
resource = Resource()
resource.type = "results"
meta_resource = Resource()
meta_resource.type = "meta"

resource.resources.append(meta_resource)
model_mapping = ModelMapping("""
<VODML>
  <REPORT/>
  <GLOBALS/>
</VODML>
"""
)

try:
    resource.model_mapping = model_mapping
except Exception as e:
    print(e)

meta_resource.model_mapping = model_mapping
votable.resources.append(resource)

votable.to_xml(vpath)
with open(vpath) as result:
    print(result.read())