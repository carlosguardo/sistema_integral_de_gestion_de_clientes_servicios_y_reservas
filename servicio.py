from abc import ABC, abstractmethod
from cliente import Entidad
class Servicio(Entidad, ABC):
    def __init__(self, nombre, descripcion):
        super().__init__()
        self._nombre = nombre
        self._descripcion = descripcion
        self._estado = "Disponible"
        self.validar_parametros()
    #------------------------------#
    #--|propiedades_del_servicio|--#
    #------------------------------#
    @property
    def nombre(self):
        return self._nombre
    @property
    def descripcion(self):
        return self._descripcion
    @property
    def estado(self):
        return self._estado
    #------------------------------------------------------#
    #--|validacion_y_modificacion_de_estado_del_servicio|--#
    #------------------------------------------------------#
    def validar_datos(self):
        self.validar_parametros()
    @abstractmethod
    def validar_parametros(self):
        pass
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass
    @abstractmethod
    def describir_servicio(self):
        pass
    #--------------------------------------#
    #--|mostrar_informacion_del_servicio|--#
    #--------------------------------------#
    def mostrar_informacion(self):
        return self.describir_servicio()
    def desactivar(self):
        self._estado = "No disponible"
    def activar(self):
        self._estado = "Disponible"
#-----------------------#
#--|la_clase_reserva_|--#
#-----------------------#
class ReservaSala(Servicio):
    def __init__(self, nombre, descripcion, capacidad, costo_hora):
        self.__capacidad = capacidad
        self.__costo_hora = costo_hora
        super().__init__(nombre, descripcion)
    def validar_parametros(self):
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ValueError("El nombre de la sala no es valido.")
        if not isinstance(self._descripcion, str) or not self._descripcion.strip():
            raise ValueError("La descripcion de la sala no es valida.")
        if not isinstance(self.__capacidad, int) or self.__capacidad <= 0:
            raise ValueError("La capacidad debe ser un numero entero positivo.")
        if not isinstance(self.__costo_hora, (int, float)) or self.__costo_hora <= 0:
            raise ValueError("El costo por hora debe ser mayor que cero.")
    #-----------------------#
    #--|calcular_el_costo|--#
    #-----------------------#
    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros()
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        costo = self.__costo_hora * duracion
        return costo - (costo * descuento / 100)
    #-----------------------------#
    #--|descripcion_de_servicio|--#
    #-----------------------------#
    def describir_servicio(self):
        return (
            f"ID: {self.id} | "
            f"Servicio: {self.nombre} | "
            f"Tipo: Reserva de sala | "
            f"Capacidad: {self.__capacidad} personas | "
            f"Costo por hora: ${self.__costo_hora} | "
            f"Estado: {self.estado}"
        )
#-----------------------#
#--|la_clase_alquiler|--#
#-----------------------#
class AlquilerEquipo(Servicio):
    def __init__(self, nombre, descripcion, tipo_equipo, costo_dia):
        self.__tipo_equipo = tipo_equipo
        self.__costo_dia = costo_dia
        super().__init__(nombre, descripcion)
    def validar_parametros(self):
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ValueError("El nombre del equipo no es valido.")
        if not isinstance(self._descripcion, str) or not self._descripcion.strip():
            raise ValueError("La descripcion del equipo no es valida.")
        if not isinstance(self.__tipo_equipo, str) or not self.__tipo_equipo.strip():
            raise ValueError("El tipo de equipo no es valido.")
        if not isinstance(self.__costo_dia, (int, float)) or self.__costo_dia <= 0:
            raise ValueError("El costo por dia debe ser mayor que cero.")
    #-----------------------#
    #--|calcular_el_costo|--#
    #-----------------------#
    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros()
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        costo = self.__costo_dia * duracion
        return costo - (costo * descuento / 100)
    #-----------------------------#
    #--|descripcion_de_servicio|--#
    #-----------------------------#
    def describir_servicio(self):
        return (
            f"ID: {self.id} | "
            f"Servicio: {self.nombre} | "
            f"Tipo: Alquiler de equipo | "
            f"Equipo: {self.__tipo_equipo} | "
            f"Costo por dia: ${self.__costo_dia} | "
            f"Estado: {self.estado}"
        )
#-----------------------#
#--|la_clase_asesoria|--#
#-----------------------#
class Asesoria(Servicio):
    def __init__(self, nombre, descripcion, especialidad, costo_hora):
        self.__especialidad = especialidad
        self.__costo_hora = costo_hora
        super().__init__(nombre, descripcion)
    def validar_parametros(self):
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ValueError("El nombre de la asesoria no es valido.")
        if not isinstance(self._descripcion, str) or not self._descripcion.strip():
            raise ValueError("La descripcion de la asesoria no es valida.")
        if not isinstance(self.__especialidad, str) or not self.__especialidad.strip():
            raise ValueError("La especialidad de la asesoria no es valida.")
        if not isinstance(self.__costo_hora, (int, float)) or self.__costo_hora <= 0:
            raise ValueError("El costo por hora debe ser mayor que cero.")
    #-----------------------#
    #--|calcular_el_costo|--#
    #-----------------------#
    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros()
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        costo = self.__costo_hora * duracion
        return costo - (costo * descuento / 100)
    #-----------------------------#
    #--|descripcion_de_servicio|--#
    #-----------------------------#
    def describir_servicio(self):
        return (
            f"ID: {self.id} | "
            f"Servicio: {self.nombre} | "
            f"Tipo: Asesoria | "
            f"Especialidad: {self.__especialidad} | "
            f"Costo por hora: ${self.__costo_hora} | "
            f"Estado: {self.estado}"
        )