#include <memory>
#include <string>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include "geometry_msgs/msg/twist.hpp"


using std::placeholders::_1;

class LidarProcesser : public rclcpp::Node{
public:
    LidarProcesser():Node("lidar_subscriber"){
        sub_name = "lidar";
        pub_name = "sen_vel";

        sen_pub = this->create_publisher<geometry_msgs::msg::Twist>(pub_name, 10);

        sen_sub = this->create_subscription<sensor_msgs::msg::LaserScan>(
            // sub_name,10,std::bind(&LidarProcesser::topic_callback, this, _1)
            sub_name,10,std::bind(&LidarProcesser::process, this, _1)
        );

        if(sen_pub){
            RCLCPP_INFO(this->get_logger(), "Subscribed to topic: %s", sub_name.c_str());
        }else{
            RCLCPP_INFO(this->get_logger(), "Failed to subscribe to topic: %s", sub_name.c_str());
        }
    }

private:
    void topic_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg){
        // RCLCPP_INFO(rclcpp::get_logger("lidar_subscriber"), "I heard: '%f', '%f'", msg->ranges[0], msg->ranges[100]);
        process(*msg);
    }

    void process(const sensor_msgs::msg::LaserScan _msg){
        
        auto twist_msg = geometry_msgs::msg::Twist();
        bool allMore = true;
        RCLCPP_INFO(rclcpp::get_logger("lidar_subscriber"), "I heard: '%f', '%f'", _msg.ranges[0], _msg.ranges[10]);
        for (size_t i = 0; i < _msg.ranges.size(); i++){
            if (_msg.ranges[i] < 1.0){
                allMore = false;
                break;
            }else{
                // RCLCPP_INFO(rclcpp::get_logger("lidar_subscriber"), "I heard: '%f', '%f'", _msg->ranges[0], _msg->ranges[10]);
            }
        }
        if (allMore) {
            twist_msg.linear.x = 0.5;
            twist_msg.angular.z = 0.0;
        }
        else{
            twist_msg.linear.x = 0.0;
            twist_msg.angular.z = 0.5;
        }
        sen_pub->publish(twist_msg);
    }
    std::string sub_name;
    std::string pub_name;
    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr sen_sub;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr sen_pub;
};

int main(int argc, char * argv[]){
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<LidarProcesser>());
    rclcpp::shutdown();
    return 0;
}