#initailization
#libraries
import time
import rpi.gpiozero
#GPIO conifg
Altitude_state = 0
Altitude_reff = 500
Altitude_I = 0
Altitude_error = 0
Thrust_out = 0
dt =1


def PID_controller(reff,state,I,Past_error,Kp,Ki,Kd):
    Error = reff - state
    P = Kp * Error
    I = Ki * (I + Error) * dt
    D = Kd * (Error - Past_error) / dt
    Past_error = Error
    output = P + I + D
    return output,I,Past_error,D,P


#Mainloop--------------------------------------------------------------------------
while (True):

#State Estimator-------------------------------------------------------------------
                                                                #Sensor readings
    Altitude_state += float(Thrust_out)


#Controller-------------------------------------------------------------------------
                                                                #Altitude PID
    Alt_Error = Alt_Reff - Alt_State
    Alt_P = Alt_Kp * Alt_Error
    Alt_I = Alt_Ki * (Alt_I + Alt_Error) * dt
    Alt_D = Alt_Kd * (Alt_Error - Alt_Past_Error) / dt
    Alt_Past_Error = Alt_Error
    Alt_Output = Alt_P + Alt_I + Alt_D
                                                                #Roll PID
    Roll_Error = Roll_Reff - Roll_State
    Roll_P = Roll_Kp * Roll_Error
    Roll_I = Roll_Ki * (Roll_I + Roll_Error) * dt
    Roll_D = Roll_Kd * (Roll_Error - Roll_Past_Error) / dt
    Roll_Past_Error = Roll_Error
    Roll_Output = Roll_P + Roll_I + Roll_D
                                                                #Pitch PID
    Pitch_Error = Pitch_Reff - Pitch_State
    Pitch_P = Pitch_Kp * Pitch_Error
    Alt_I = Alt_Ki * (Alt_I + Alt_Error) * dt
    Alt_D = Alt_Kd * (Alt_Error - Alt_Past_Error) / dt
    Alt_Past_Error = Alt_Error
    Alt_Output = Alt_P + Alt_I + Alt_D
#Fault Protector--------------------------------------------------------------------




#Output----------------------------Range (0-1024)-----------------------------------
    MotorFL = Thrust_out - Roll_out - Yaw_out - Pitch_out
    MotorBR = Thrust_out + Roll_out - Yaw_out + Pitch_out
    MotorBL = Thrust_out - Roll_out + Yaw_out + Pitch_out
    MotorBL = Thrust_out - Roll_out + Yaw_out + Pitch_out
#Modeling----------------------------------------------------------------------------
   # Global_position =


#Data Logging----------------------------------------------------------------------