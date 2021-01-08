#include <rclcpp/rclcpp.hpp>
#include <chrono>
#include <string>
#include <functional>

using namespace std::chrono_literals;

class ParametersClass: public rclcpp::Node {
 public:
  ParametersClass()
      : Node("parameter_node") {

    this->declare_parameter<std::string>("my_parameter", "The default value in C++ code");

    timer_ = this->create_wall_timer(
        1000ms, std::bind(&ParametersClass::respond, this));
  }
  void respond() {
    std::string parameter_string;
    this->get_parameter("my_parameter", parameter_string);
    RCLCPP_INFO(this->get_logger(), "my_parameter: %s", parameter_string.c_str());
  }

 private:
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ParametersClass>());
  rclcpp::shutdown();
  return 0;
}
