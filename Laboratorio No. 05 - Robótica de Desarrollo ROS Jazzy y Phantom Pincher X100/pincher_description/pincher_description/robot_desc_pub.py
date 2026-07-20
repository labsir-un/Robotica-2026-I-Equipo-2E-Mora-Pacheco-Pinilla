#!/usr/bin/env python3
"""Publish robot_description on /robot_description topic once for RViz."""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotDescPublisher(Node):
    def __init__(self):
        super().__init__('robot_desc_publisher')
        urdf = self.get_parameter('robot_description').get_parameter_value().string_value
        self.pub = self.create_publisher(String, 'robot_description', 1)
        self.timer = self.create_timer(1.0, lambda: self._publish(urdf))

    def _publish(self, urdf):
        msg = String(data=urdf)
        self.pub.publish(msg)
        self.get_logger().info('robot_description published (%d bytes)', len(urdf))
        self.timer.cancel()
        self.timer.destroy()


def main():
    rclpy.init()
    node = RobotDescPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
