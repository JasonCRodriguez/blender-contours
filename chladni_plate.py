import bpy
import math
import random


def create_chladni():
    
    try:
        bpy.ops.object.delete(use_global=False, confirm=False)
    except:
        print('No object to delete') 

    bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
    bpy.context.object.modifiers["Subdivision"].levels = 6
    bpy.ops.object.modifier_apply(modifier="Subdivision")


    # Define Chladni pattern parameters
    amplitude_a = 0.1
    amplitude_b = 0.1  # Adjust the amplitude of the Chladni pattern
    
    frequency_a = random.uniform(1.5,4.5)  # Adjust the frequency of the Chladni pattern
    frequency_b = random.uniform(1.5,4.5)  # Adjust the frequency of the Chladni pattern
    
    bpy.context.selected_objects[0].name = 'chladni_plate_{:.2f}_{:.2f}'.format(frequency_a, frequency_b)

    mode = bpy.context.active_object.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
    for v in selectedVerts:
        print(str(v) + " "  + str(v.co))
    bpy.ops.object.mode_set(mode=mode)

    for vert in selectedVerts:
        x, y, z = vert.co
        vert.co.z += amplitude_a * math.sin(frequency_a * x * math.pi) * math.sin(frequency_b * y * math.pi)\
                        + amplitude_b * math.sin(frequency_b * x * math.pi) * math.sin(frequency_a * y * math.pi)

    mode = bpy.context.active_object.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.shade_smooth()


create_chladni()