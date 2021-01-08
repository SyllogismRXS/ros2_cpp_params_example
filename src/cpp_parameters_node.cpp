#include <rclcpp/rclcpp.hpp>
#include <chrono>
#include <string>
#include <functional>

using namespace std::chrono_literals;

class ParametersClass: public rclcpp::Node {
 public:
  ParametersClass()
      : Node("parameter_node") {

    this->declare_parameter<std::string>("my_parameter", "The default string value in C++ code");
    this->declare_parameter<float>("my_float_number", 0.12345);

    timer_ = this->create_wall_timer(
        1000ms, std::bind(&ParametersClass::respond, this));
  }
  void respond() {
    std::string parameter_string;
    this->get_parameter("my_parameter", parameter_string);
    RCLCPP_INFO(this->get_logger(), "my_parameter: %s", parameter_string.c_str());

    float float_number;
    this->get_parameter("my_float_number", float_number);
    RCLCPP_INFO(this->get_logger(), "my_float_number: %f", float_number);
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
