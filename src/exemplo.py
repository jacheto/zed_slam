import pyzed.sl as sl


def main():
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.RESOLUTION_HD720  # Use HD720 video mode (default fps: 60)
    # Use a right-handed Y-up coordinate system
    init_params.coordinate_system = sl.COORDINATE_SYSTEM.COORDINATE_SYSTEM_RIGHT_HANDED_Y_UP
    init_params.coordinate_units = sl.UNIT.UNIT_METER  # Set units in meters

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    area_path = "area/teste.area"

    # Enable positional tracking with default parameters
    py_transform = sl.Transform()  # First create a Transform object for TrackingParameters object
    tracking_parameters = sl.TrackingParameters(init_pos=py_transform)

    tracking_parameters.area_file_path = area_path

    err = zed.enable_tracking(tracking_parameters)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Track the camera position during 1000 frames
    i = 0
    zed_pose = sl.Pose()
    zed_imu = sl.IMUData()
    runtime_parameters = sl.RuntimeParameters()

    while i < 1000:
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:

            print(zed.get_position(zed_pose, sl.REFERENCE_FRAME.REFERENCE_FRAME_WORLD))
            print(i)
            i = i + 1
    zed.disable_tracking(area_path)
    zed.get_area_export_state()
    sl.AREA_EXPORT_STATE.AREA_EXPORT_STATE_SUCCESS
    # Close the camera
    zed.close()


if __name__ == "__main__":
    main()
