from controller import Robot
def lfr_robot(robot):
    time_stp=32
    max_speed=6.28
    
    #initializing motor wheels
    left_wheel =robot.getDevice("wheel1")
    right_wheel =robot.getDevice("wheel2")
    left_wheel.setPosition(float('inf'))
    right_wheel.setPosition(float('inf'))
    left_wheel.setVelocity(0.0)
    right_wheel.setVelocity(0.0)
    
    #enabling  sensors and camera
    left_ir=robot.getDevice("left ir sensor")
    right_ir=robot.getDevice("Right ir sensor")
    left_ir.enable(time_stp)
    right_ir.enable(time_stp)
   
   
   
    #Simulation
    while robot.step(time_stp)!=-1:
        lir_value= left_ir.getValue()
        rir_value= right_ir.getValue()
        
        print("left: {} right: {}" .format(lir_value ,rir_value))
        left_speed =max_speed*0.5
        right_speed=max_speed*0.5
        if(lir_value>rir_value) and (800< lir_value< 1000):
           left_speed= -max_speed*0.5
        elif(rir_value> lir_value)and (800 < rir_value < 1000):
            right_speed= -max_speed*0.5
        left_wheel.setVelocity(left_speed)
        right_wheel.setVelocity(right_speed) 
    
        
if __name__ == "__main__":
    This_robot=Robot()
    lfr_robot(This_robot)