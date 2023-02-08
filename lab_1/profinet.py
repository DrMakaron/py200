class ProfinetIO:

    def __init__(self, pipe_connection):
        """
        Класс описывает взаимодействие через PROFINET
        :param: pipe_connection: Экземпляр класса подключения по именованному каналу
        """
        self.pipe_connection = pipe_connection

    def read_named_data(self, module_id: int, submodule_id: int) -> dict:
        """
        Чтение буфера данных
        :param: module_id: id модуля внутри сети PROFINET
        :param: submodule_id: id подмодуля в сети PROFINET
        :return: словарь со считанными данными
        """
        request_msg = {"jsonrpc": "2.0",
                       "method": "readCyclicIoDataNamed",
                       "params": [{"module_id": module_id, "submodule_id": submodule_id}],
                       "id": 0}

        answer = self.pipe_connection.send(request_msg)
        return answer['result'][0]

    def write_named_data(self, module_id: int, submodule_id: int, parameter_name: str, parameter_value: float):
        """
        Запись значения в буфер
        :param: module_id: id модуля внутри сети PROFINET
        :param: submodule_id: id подмодуля в сети PROFINET
        :param: parameter_name: имя параметра
        :param: parameter_value: новое значение
        :return: словарь со считанными данными
        """
        request_msg = {"jsonrpc": "2.0",
                       "method": "writeCyclicIoDataNamed",
                       "params": [{"module_id": module_id,
                                   "submodule_id": submodule_id,
                                   "data": {parameter_name: parameter_value}}],
                       "id": 0}

        self.pipe_connection.send(request_msg)
