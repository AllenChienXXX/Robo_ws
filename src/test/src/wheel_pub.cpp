#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"
#include "geometry_msgs/msg/twist.hpp"

using namespace std::chrono_literals;


class WheelControlPublisher : public rclcpp::Node {
public:

    int index = 0;
    const int size = 4;
    double linear_list[4] = {1.0,0,1.0,0};
    double angular_list[4] = {0,1.57,0,1.57};

    WheelControlPublisher() : Node("wheel_control_publisher") {
        const std::string topic_name = "sen_vel";
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>(topic_name, 10);

        timer_ = this->create_wall_timer(
            1000ms, std::bind(&WheelControlPublisher::publishMessage, this));
    }

private:
    void publishMessage() {
        auto twist_msg = geometry_msgs::msg::Twist();

        twist_msg.linear.x = linear_list[index]; // Linear velocity (m/s)
        twist_msg.angular.z = angular_list[index]; // Angular velocity (rad/s)

        std::string log_msg = "Publishing: linear: "+std::to_string(linear_list[index])+",angular: " + std::to_string(angular_list[index]);
        index = index + 1;
        if(index>=4) index = 0;

        RCLCPP_INFO(this->get_logger(), log_msg.c_str());

        publisher_->publish(twist_msg);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<WheelControlPublisher>());
    rclcpp::shutdown();
    return 0;
}
