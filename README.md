# zenoh-issue-718

Install all dependencies
```
rosdep install --from-paths src --ignore-src --rosdistro rolling -y
```

Build the project and source it
```
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
```

Source the environment
```
source install/setup.bash
```

Start the node
```
ros2 run issue718 service
```

Start a zenoh router (enable debugging with envvar `RUST_LOG='zenoh=info,zenoh_transport=debug'`)
```
ros2 run rmw_zenoh_cpp rmw_zenohd
```

Try to call the 3 services. The unpatched version of `rmw_zenoh` will only work with `/issue718_test`. Others will hang on `waiting for service to become available...`
```
ros2 service call /issue718_test issue718_interfaces/srv/Test
ros2 service call /issue718_request issue718_interfaces/srv/TestRequest
ros2 service call /issue718_response issue718_interfaces/srv/TestResponse
```