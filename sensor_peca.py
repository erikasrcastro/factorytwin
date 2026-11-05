import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class SensorPeca(Node):

    def __init__(self):
        super().__init__('sensor_peca')

        self.publicador = self.create_publisher(
            Bool,
            '/sensor/peca',
            10
        )

        self.peca_detectada = False
        self.timer = self.create_timer(1.0, self.verificar_peca)

    def verificar_peca(self):
        self.peca_detectada = not self.peca_detectada

        mensagem = Bool()
        mensagem.data = self.peca_detectada

        self.publicador.publish(mensagem)

        self.get_logger().info(
            f'Peça detectada: {mensagem.data}'
        )


def main():
    rclpy.init()
    sensor = SensorPeca()

    try:
        rclpy.spin(sensor)
    except KeyboardInterrupt:
        pass
    finally:
        sensor.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
