import bpy

# Clear all mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Define the 5 vertices of the pyramid
verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0.5, 0.5, 1)]

# Define the 5 faces of the pyramid
faces = [(0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4), (0, 1, 2, 3)]

# Create the mesh and object
mesh = bpy.data.meshes.new(name="PyramidMesh")
obj = bpy.data.objects.new("Pyramid", mesh)

# Link the object to the scene
bpy.context.collection.objects.link(obj)

# Create the pyramid
mesh.from_pydata(verts, [], faces)
