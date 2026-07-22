import time
import smbus
from gpiozero import Motor, Servo, DistanceSensor
#PID CONTROLER VARUABLES
KI = 0.0005
KP = 0.10
KD = 0.02
error = 0 
last_error = 0 
current_error = 0
errorsum = 0 
#MPU6050 VARUABLES
gyro_read = 0
is_runing = 1
angle = 0
anglez = 0
#ULTRASONIC VARUABLES
frontdis = 0 
left_dist = 0
right_dist = 0
# SYSTEM VARUABLES
angle_counter = 0 
last_time = time.time()
last_turn_time = 0 
turning_in_progress = False
mtr = Motor(forward=20, backward=12)
srv = Servo(17) 
last_time = time.time()
#MPU6050 I2C PATH
MPU_ADDR = 0x68
bus = smbus.SMBus(1)
PWR_MGMT_1 = 0x6B
GYRO_ZOUT_H = 0x47
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)
#MAIN FUNCTIONS
def stop():
    mtr.stop()
    srv.value = 0 
def dist(TRIG19 = 99999, ECHO19 = 999999):
    try:
        ultrasonc = DistanceSensor(echo = ECHO19 , trigger = TRIG19 )
        dst = ultrasonc.distance
        distcm = int( dst * 100 )
        return distcm
    except Exception:
        return 0
def get_sensor_cm(sensor, fallback_val):
    try:
        return int(sensor.distance * 100)
    except Exception:
        return fallback_val
def read_word(reg):
    try:
        high = bus.read_byte_data(MPU_ADDR, reg)
        low  = bus.read_byte_data(MPU_ADDR, reg+1)
        val = (high << 8) | low
        if val & 0x8000:
            val = -((65535 - val) + 1)
        return val
    except OSError:
        return 0
def read_gyro_z():
    gz = read_word(GYRO_ZOUT_H)
    return gz / 131.0   
def update_angle():
    global angle, last_time
    now = time.time()
    dt = now - last_time
    last_time = now
    gz = read_gyro_z()
    angle += gz * dt
    return angle
front_sensor = DistanceSensor(trigger=5, echo=6)
left_sensor  = DistanceSensor(trigger=23, echo=24)
right_sensor = DistanceSensor(trigger=27, echo=22)
# MAIN LOGIC :
while is_runing:
    mtr.forward(0.5)
    frontdis   = get_sensor_cm(front_sensor, frontdis)
    left_dist  = get_sensor_cm(left_sensor, left_dist)
    right_dist = get_sensor_cm(right_sensor, right_dist)
    gyro_read = update_angle()
    error = anglez - int(gyro_read)
    current_error = error
    errorsum += error
    errorsum = max(min(errorsum, 100), -100)
    kpampount = KP * error
    kiamount = KI * errorsum
    kdamount = KD * (current_error - last_error)
    last_error = current_error
    finalamount = kpampount + kiamount + kdamount
    finalcorrection = max(min(finalamount, 0.9), -0.9)
    current_time = time.time()

    if  not angle_counter == 12 and frontdis <= 99 and (current_time - last_turn_time >= 3.0) and not turning_in_progress:
        if left_dist == 100:
            anglez += 90
            print("turning 90 to the left")
            angle_counter+=1
            last_turn_time = current_time
            turning_in_progress = True   
        elif right_dist == 100:
            anglez -= 90
            print("turning 90 to the right ")
            last_turn_time = current_time
            angle_counter+=1
            turning_in_progress = True   
        else:
            print("none is 100 no changes are done")

    if turning_in_progress :
        turning_in_progress = False

    srv.value = -finalcorrection
    if angle_counter == 12:
        is_runing = 0

    time.sleep(0.002)   
stop()
time_right_now = time.time()
while True:
    mtr.forward(0.5)
    frontdis   = get_sensor_cm(front_sensor, frontdis)
    left_dist  = get_sensor_cm(left_sensor, left_dist)
    right_dist = get_sensor_cm(right_sensor, right_dist)
    gyro_read = update_angle()
    error = anglez - int(gyro_read)
    current_error = error
    errorsum += error
    errorsum = max(min(errorsum, 100), -100)
    kpampount = KP * error
    kiamount = KI * errorsum
    kdamount = KD * (current_error - last_error)
    last_error = current_error
    finalamount = kpampount + kiamount + kdamount
    finalcorrection = max(min(finalamount, 0.9), -0.9)
    current_time = time.time()

    srv.value = -finalcorrection
    if angle_counter == 12:
        is_runing = 0

    time.sleep(0.002)  
    if time.time() - time_right_now >= 5:
        break
stop()