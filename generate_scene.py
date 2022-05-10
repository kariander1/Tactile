import numpy as np

c=0


import bpy, math

for obj in bpy.data.objects:
    print(obj.name)

knob = bpy.data.objects["MyBlenderKnob"]
knob.rotation_mode = 'XYZ'

rotate_by = 4.21875   #How many degrees to rotate the knob for every step
start_angle = 45      #What angle to start from

for x in range(1,65):
    angle = (start_angle * (math.pi/180)) + (x*-1) * (rotate_by * (math.pi/180))
    knob.rotation_euler = ( 0, 0, angle )

    bpy.context.scene.render.filepath = "/Users/myfolder/KnobFrame%d.png" % (x)
    bpy.ops.render.render(write_still=True, use_viewport=True)