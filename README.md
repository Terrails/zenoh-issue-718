# zenoh-issue-718

Build the project and source it
```
colcon build && source install/setup.bash
```

Start the node
```
ros2 run issue718 service
```

Start a zenoh router
```
ros2 run rmw_zenoh_cpp rmw_zenohd
```

Try to call the 3 services. The unpatched version of `rmw_zenoh` will only work with `/issue718_test`. Others will hang on `waiting for service to become available...`
```
ros2 service call /issue718_test issue718_interfaces/srv/Test
ros2 service call /issue718_request issue718_interfaces/srv/TestRequest
ros2 service call /issue718_response issue718_interfaces/srv/TestResponse
```