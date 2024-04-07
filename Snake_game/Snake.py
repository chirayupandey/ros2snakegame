#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn,Kill
import random
import math
msg3 = Pose()
j=0
class Myspawner(Node):
    def __init__(self):
        super().__init__("Spawner_client")
        self.client = self.create_client(Spawn,"/spawn")
        while not self.client.wait_for_service(1.0):
            self.get_logger().info("Waiting for service")
        self.Spawn_Turtle()
    def Spawn_Turtle(self):
        request = Spawn.Request()
        request.x = random.uniform(1,10)
        request.y = random.uniform(1,10)
        request.theta = random.uniform(1,3.14)
        request.name = "turtle2"
        future = self.client.call_async(request)
        self.get_logger().info("Calling the service")
        rclpy.spin_once(self)
        if future.done():
            try:
                self.get_logger().info("Turtle spawned succesfully")
            except Exception as e:
                self.get_logger().error("Turtle failed to spawn")

class Killturt(Node):
    def __init__(self):
        super().__init__("Killing_turtle")
        self.client2 = self.create_client(Kill,"/kill")
        while not self.client2.wait_for_service(1.0):
            self.get_logger().info("Waiting for service ....")
        self.Kill_Turtle()
    def Kill_Turtle(self):
        request = Kill.Request()
        request.name = "turtle2"
        future = self.client2.call_async(request)
        self.get_logger().info("Killing Turtle")
        rclpy.spin_once(self)
        if future.done():
            try:
                self.get_logger().info("Turtle killed succesfully")
            except Exception as e:
                self.get_logger().info("Turtle is too powerful")
class TurtSnake(Node):
    def __init__(self):
        super().__init__("Turt_Snake")
        self.get_logger().info("Node Has started")
        self.pose2_sub = self.create_subscription(Pose,"/turtle2/pose",self.pose2_callback,10)
        self.pose1_sub = self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
    def pose2_callback(self,msg2:Pose):
        global msg3 
        msg3 = msg2
    def pose_callback(self,msg1:Pose):
        global j
        x= msg1.x-msg3.x
        y = msg1.y-msg3.y
        distance = math.sqrt(math.pow(x,2)+math.pow(y,2))
        if distance<=0.5:
            kilturt2 = Killturt()
            turt = Myspawner()
        else:
            pass
def main(args=None):
    rclpy.init(args=args)
    node = Myspawner()
    node2 = TurtSnake()
    rclpy.spin(node2)
    rclpy.shutdown()

    




    
