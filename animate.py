import bpy
import math

def animate(scene):
    armature = bpy.data.objects['Armature']
    bones = armature.pose.bones

    t = scene.frame_current * 0.1

    spine_bones = sorted(
        [b for b in bones if "Bone" in b.name],
        key=lambda b: b.name
    )

    for i, bone in enumerate(spine_bones):
        bone.rotation_mode = 'XYZ'

        amplitude = -0.1 + i * 0.05
        phase = i * 0.5

        angle = math.sin(t + phase) * amplitude

        bone.rotation_euler[0] = angle


bpy.app.handlers.frame_change_pre.clear()

bpy.app.handlers.frame_change_pre.append(animate)

scene = bpy.context.scene
scene.frame_start = 0
scene.frame_end = 120