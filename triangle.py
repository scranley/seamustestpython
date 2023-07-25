import bpy

# Enable the MB-Lab add-on
bpy.ops.preferences.addon_enable(module="MB-Lab")

# Clear all mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create a human shape
bpy.ops.mbast.init_character()

# Select the human object
human = bpy.context.object
bpy.context.view_layer.objects.active = human
human.select_set(True)

# Export to FBX
bpy.ops.export_scene.fbx(filepath="human.fbx")
