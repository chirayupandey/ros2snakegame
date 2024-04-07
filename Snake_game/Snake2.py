#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from turtlesim.msg import Pose
from turtlesim.srv import Spawn, SetPen
import random
import math


class TurtSnake(Node):
    def __init__(self):
        super().__init__("Turt_Snake")
        self.get_logger().info("Node Has started")
        self.pose1_sub = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.pose2_sub = self.create_subscription(Pose,"/turtle2/pose",self.pose2_callback,10)
        self.vel2_pub= self.create_publisher(Twist,"/turtle2/cmd_vel",10)
    def pose_callback(self):
        global msg1
        msg1 = Pose()
    def pose2_callback(self,msg2:Pose):
        cmd = Twist()
        if msg1==msg2:
            cmd.linear.x = 2.0
            cmd.angular.z = 1.0
        else:
            pass        
def main(args=None):
    rclpy.init(args=args)
    node = TurtSnake()
    rclpy.spin(node)