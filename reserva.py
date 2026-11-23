import logging
from cliente import Entidad, Cliente
from servicio import Servicio
from excepciones import ErrorSistemaFJ
logger = logging.getLogger(__name__)
#----------------------#
#--|la_clase_reserva|--#
#----------------------#
class Reserva(Entidad):
    def __init__(self, cliente, servicio, duracion):
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0
        super().__init__()
        self.validar_datos()
    #-----------------#
    #--|propiedades|--#
    #-----------------#
    @property
    def cliente(self):
        return self.__cliente
    @property
    def servicio(self):
        return self.__servicio
    @property
    def duracion(self):
        return self.__duracion
    @property
    def estado(self):
        return self.__estado
    @property
    def costo(self):
        return self.__costo
    #----------------#
    #--|validacion|--#
    #----------------#
    def validar_datos(self):
        if not isinstance(self.__cliente, Cliente):
            raise TypeError("La reserva debe tener un cliente valido.")
        if not isinstance(self.__servicio, Servicio):
            raise TypeError("La reserva debe tener un servicio valido.")
        if not isinstance(self.__duracion, (int, float)) or isinstance(self.__duracion, bool):
            raise TypeError("La duracion debe ser un numero.")
        if self.__duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")
        if self.__cliente.estado != "Activo":
            raise ErrorSistemaFJ("No se puede reservar con un cliente inactivo.")
        if self.__servicio.estado != "Disponible":
            raise ErrorSistemaFJ("El servicio seleccionado no esta disponible.")
    #-------------------------------------------#
    #--|confirmacion_y_cancelacion_de_reserva|--#
    #-------------------------------------------#
    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ErrorSistemaFJ("Solamente se pueden confirmar reservas pendientes.")
        self.__estado = "Confirmada"
        logger.info("Reserva %s confirmada.", self.id)
        return "La reserva ha sido confirmada correctamente."
    def cancelar(self):
        if self.__estado in ("Cancelada", "Procesada"):
            raise ErrorSistemaFJ("No se puede cancelar una reserva cancelada o procesada.")
        self.__estado = "Cancelada"
        logger.info("Reserva %s cancelada.", self.id)
        return "La reserva ha sido cancelada correctamente."
    #------------------------------#
    #--|procesamiento_de_reserva|--#
    #------------------------------#
    def procesar(self, descuento=0):
        try:
            if self.__estado != "Confirmada":
                raise ErrorSistemaFJ("La reserva debe estar confirmada antes de procesarse.")
            self.validar_datos()
            self.__costo = self.__servicio.calcular_costo(self.__duracion, descuento)
        except ErrorSistemaFJ:
            logger.error("No se pudo procesar la reserva %s.", self.id)
            raise
        except (ValueError, TypeError) as error:
            logger.error("Error al calcular el costo de la reserva %s: %s", self.id, error)
            raise ErrorSistemaFJ("Ocurrio un error durante el procesamiento de la reserva.") from error
        else:
            self.__estado = "Procesada"
            logger.info("Reserva %s procesada correctamente. Costo: %.2f", self.id, self.__costo)
            return self.__costo
        finally:
            logger.info("Finalizo el intento de procesamiento de la reserva %s.", self.id)
    #--------------------------#
    #--|mostrar_informacion_|--#
    #--------------------------#
    def mostrar_informacion(self):
        return (
            f"Id de reserva: {self.id}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:.2f}"
        )
    #----------------------------------#
    #--|representacion_de_la_reserva|--#
    #----------------------------------#
    def __str__(self):
        return (
            f"Id: {self.id} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} | "
            f"Estado: {self.__estado} | "
            f"Costo: ${self.__costo:.2f}"
        )