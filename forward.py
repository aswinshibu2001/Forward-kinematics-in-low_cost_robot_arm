import mujoco
import mujoco.viewer

m = mujoco.MjModel.from_xml_path('simulation/low_cost_robot/scene.xml')
d = mujoco.MjData(m)

# angle=[1,0,-1,2,2]
angle=[0.434,-0.345,-0.473,0.0404,-0.25]
for i in range(len(angle)):
  d.ctrl[i]=angle[i]
mujoco.mj_forward(m,d)

with mujoco.viewer.launch_passive(m, d) as viewer:
  
  while viewer.is_running():
    
    endeff=m.geom("end_effector").id
    end_effector_pos = d.geom_xpos[endeff]
    print(f"End-Effector Cartesian Coordinates: {end_effector_pos}") 
    
    mujoco.mj_step(m, d)
    viewer.sync()
    