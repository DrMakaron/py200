import serial


class BarScanner:
    def __init__(self, data_model):
        """
        Класс описывает взаимодействие со сканером bar-кодов
        :param: data_model: Экземпляр класса модели данных
        """
        self.data_model = data_model

        self.port = 'COM1'
        self.baud = 9600
        self.serial_port = None
        self.connection_flag = False

    def make_connection(self):
        """
        Выполнение подключения к последовательному порту, к которому подключен сканер
        """
        try:
            self.serial_port = serial.Serial(self.port, self.baud)
            self.connection_flag = True
            print('BAR scanner connected')
        except serial.serialutil.SerialException:
            self.connection_flag = False
            print('BAR scanner not connected')
        self.data_model.update_signal('scanner_online', self.connection_flag)

    def listen_port(self):
        """
        Прослушивает последовательный порт.
        Запускать в отдельном потоке
        """
        while True:
            raw_data = self.serial_port.read(40)
            data = raw_data.decode()
            print(f'Scanner info: {data}')
