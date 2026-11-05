import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class ControladorEsteira(Node):

    def __init__(self):
        super().__init__('controlador_esteira')

        self.ultimo_sinal = time.monotonic()
        self.falha_ativa = False
        self.recebeu_mensagem = False

        self.assinatura = self.create_subscription(
            Bool,
            '/sensor/peca',
            self.receber_peca,
            10
        )

        self.watchdog = self.create_timer(
            0.5,
            self.verificar_sensor
        )

    def receber_peca(self, mensagem):
        self.ultimo_sinal = time.monotonic()
        self.recebeu_mensagem = True

        if self.falha_ativa:
            self.get_logger().info(
                'COMUNICAÇÃO RESTABELECIDA'
            )
            self.falha_ativa = False

        if mensagem.data:
            self.get_logger().info(
                'PEÇA DETECTADA: acionar braço virtual'
            )
        else:
            self.get_logger().info(
                'Esteira livre: aguardando peça'
            )

    def verificar_sensor(self):
        tempo_sem_sinal = (
            time.monotonic() - self.ultimo_sinal
        )

        if tempo_sem_sinal > 3.0 and not self.falha_ativa:
            self.falha_ativa = True
            self.get_logger().error(
                f'FALHA: sensor sem comunicação há '
                f'{tempo_sem_sinal:.1f} segundos'
            )


def main():
    rclpy.init()
    controlador = ControladorEsteira()

    try:
        rclpy.spin(controlador)
    except KeyboardInterrupt:
        pass
    finally:
        controlador.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
