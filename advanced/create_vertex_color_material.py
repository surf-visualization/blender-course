import bpy

mat = bpy.data.materials.new(name="mymat")   
mat.use_nodes = True

nodes = mat.node_tree.nodes
nodes.clear()
links = mat.node_tree.links

a = mat.node_tree.nodes.new(type='ShaderNodeAttribute')
a.location = (0, 0)
a.attribute_name = "Col"

b = mat.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')  
b.location = (300, 0)

o = nodes.new(type='ShaderNodeOutputMaterial')
o.location = (600, 0)

links.new(a.outputs['Color'], b.inputs['Base Color'])
links.new(b.outputs['BSDF'], o.inputs['Surface'])