import bpy

# Clear all mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Define the 3 vertices of the triangle
verts = [(0, 0, 0), (1, 0, 0), (0.5, 1, 0)]

# Define the single face of the triangle
faces = [(0, 1, 2)]

# Create the mesh and object
mesh = bpy.data.meshes.new(name="TriangleMesh")
obj = bpy.data.objects.new("Triangle", mesh)

# Link the object to the scene
bpy.context.collection.objects.link(obj)

# Create the triangle
mesh.from_pydata(verts, [], faces)

# Select the triangle object
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Export to FBX
bpy.ops.export_scene.fbx(filepath="triangle.fbx")
