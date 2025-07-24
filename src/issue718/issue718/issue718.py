import rclpy
from rclpy.node import Node
from issue718_interfaces.srv import Test, TestResponse, TestRequest

class Issue718Node(Node):
    def __init__(self):
        super().__init__('issue718_node')

        self.create_service(
            Test,
            'issue718_test',
            self._callback
        )

        self.create_service(
            TestResponse,
            'issue718_response',
            self._callback
        )

        self.create_service(
            TestRequest,
            'issue718_request',
            self._callback
        )

        self.get_logger().info('Issue 718 Node has been started.')

    def _callback(self, _, response):
        response.text = "Hello, world!"
        return response
    

def main():
    rclpy.init()
    node = Issue718Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
