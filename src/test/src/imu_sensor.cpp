#include <memory>
#include <string>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/imu.hpp"
#include "geometry_msgs/msg/twist.hpp"


using std::placeholders::_1;

class IMUProcesser : public rclcpp::Node{
public:
    IMUProcesser():Node("lidar_subscriber"){
        topic_name = "imu";

        sen_sub = this->create_subscription<sensor_msgs::msg::Imu>(
            topic_name,10,std::bind(&IMUProcesser::topic_callback, this, _1)
        );

        if(sen_pub){
            RCLCPP_INFO(this->get_logger(), "Subscribed to topic: %s", topic_name.c_str());
        }else{
            RCLCPP_INFO(this->get_logger(), "Failed to subscribe to topic: %s", topic_name.c_str());
        }
    }

private:
    void topic_callback(const sensor_msgs::msg::Imu::SharedPtr msg){
        // RCLCPP_INFO(this->get_logger(), "I heard: '%f' '%f'", msg->angular_velocity,msg->orientation);
        // geometry_msgs::msg::Pose line_pose;
        // RCLCPP_INFO_STREAM(get_logger(), "pose is " << line_pose);
        RCLCPP_INFO(rclcpp::get_logger("imu_subscriber"), "Received IMU data: [%f, %f, %f, %f]",
              msg->orientation.x, msg->orientation.y, msg->orientation.z, msg->orientation.w);
    }
    std::string topic_name;
    rclcpp::Subscription<sensor_msgs::msg::Imu>::SharedPtr sen_sub;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr sen_pub;
};

int main(int argc, char * argv[]){
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<IMUProcesser>());
    rclcpp::shutdown();
    return 0;
}