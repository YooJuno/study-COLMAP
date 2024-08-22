import math
import cv2
def calc_dist(src, dst):
    return math.sqrt(math.pow(src[0]-dst[0],2) + math.pow(src[1]-dst[1],2) + math.pow(src[2]-dst[2],2))

if __name__ == '__main__':
    cap = cv2.VideoCapture("./video/R1.mp4")
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    print(video_fps)

    street_lamp_right_poses = [ 
        [-0.345908, -0.0760476, 4.5086], 
        [-0.656305, -0.78163, -1.20592]
    ]
    
    pixel_distance = calc_dist(street_lamp_right_poses[0], street_lamp_right_poses[1])
    real_distance = 80.3 # meter
    
    ratio_meter_to_pixel = real_distance / pixel_distance
    print("ratio ==", ratio_meter_to_pixel, "[m/pxls]")

    # tx, ty, tz
    camera_pos = [ 
        [-0.448946, -1.07781, -9.33733],
        [-0.378263, -0.95718, -8.13163],
        [-0.328783, -0.77419, -6.95877],
        [-0.288234, -0.704078, -5.77175],
        [-0.231324, -0.522584, -4.62204],
        [-0.189358, -0.400286, -3.5052],
        [-0.123751, -0.286023, -2.40328],
        [-0.0741185, -0.162833, -1.32466],
        [-0.024503, -0.0457251, -0.351633],
        [0.018204, 0.0563651, 0.499806],
        [0.0530542, 0.146527, 1.23751],
        [0.0815468, 0.202039, 1.81175],
        [0.105676, 0.250832, 2.26365],
        [0.121665, 0.283352, 2.59578]
    ]

    # index
    frame_number = [
        0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390
    ]
    
    # km/h
    gps_velocity =[
        63, 62, 61, 60, 59, 56, 55, 55, 51, 44, 39, 32, 25, 18
    ]
    
    for i in range(len(frame_number)-1):
        duration = ((frame_number[i+1] - frame_number[i])/video_fps) / (60 * 60) # hours
        estimated_velocity = (calc_dist(camera_pos[i+1], camera_pos[i]) * ratio_meter_to_pixel / 1000) / duration
        print("(%3d -> %3d) Estimation: %5.2f[km/h]"%(frame_number[i], frame_number[i+1], estimated_velocity), end='')
        print(",  GPS: %d[km/h]"%(gps_velocity[i]))