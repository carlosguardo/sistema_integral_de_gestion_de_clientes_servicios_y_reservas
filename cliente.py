from abc import ABC, abstractmethod
class Entidad(ABC):
    siguiente_id = 1
    def __init__(self):
        self.__id = Entidad.siguiente_id
        Entidad.siguiente_id += 1
    @property
    def id(self):
        return self.__id
    @abstractmethod
    def validar_datos(self):
        pass
    @abstractmethod
    def mostrar_informacion(self):
        pass
#----------------------#
#--|la_clase_cliente|--#
#----------------------#
class Cliente(Entidad):
    def __init__(self, nombre, correo, telefono):
        super().__init__()
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__estado = "Activo"
        self.validar_datos()
    #-----------------#
    #--|propiedades|--#
    #-----------------#
    @property
    def nombre(self):
        return self.__nombre
    @property
    def correo(self):
        return self.__correo
    @property
    def telefono(self):
        return self.__telefono
    @property
    def estado(self):
        return self.__estado
    #-------------------------#
    #--|validacion_de_datos|--#
    #-------------------------#
    def validar_datos(self):
        if not isinstance(self.__nombre, str):
            raise TypeError("El nombre debe ser un texto.")
        if not self.__nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if not all(
            caracter.isalpha() or caracter in " -'"
            for caracter in self.__nombre.strip()
        ):
            raise ValueError("El nombre contiene caracteres invalidos.")
        if not isinstance(self.__correo, str):
            raise TypeError("El correo debe ser un texto.")
        if (
            "@" not in self.__correo
            or self.__correo.count("@") != 1
            or " " in self.__correo
            or "." not in self.__correo.split("@")[1]
        ):
            raise ValueError("El correo electronico no es valido.")
        if not isinstance(self.__telefono, str):
            raise TypeError("El telefono debe ser un texto.")
        telefono_limpio = (
            self.__telefono
            .replace(" ", "")
            .replace("-", "")
            .replace("+", "")
            .replace("(", "")
            .replace(")", "")
        )
        if not telefono_limpio.isdigit():
            raise ValueError("El telefono contiene caracteres invalidos.")
        if not 7 <= len(telefono_limpio) <= 15:
            raise ValueError("El telefono debe tener entre 7 y 15 digitos.")
    #---------------------------#
    #--|modificacion_de_datos|--#
    #---------------------------#
    def actualizar_datos(self, nombre=None, correo=None, telefono=None):
        nombre_anterior = self.__nombre
        correo_anterior = self.__correo
        telefono_anterior = self.__telefono
        try:
            if nombre is not None:
                self.__nombre = nombre
            if correo is not None:
                self.__correo = correo
            if telefono is not None:
                self.__telefono = telefono
            self.validar_datos()
        except (ValueError, TypeError):
            self.__nombre = nombre_anterior
            self.__correo = correo_anterior
            self.__telefono = telefono_anterior
            raise
    #----------------------------------#
    #--|mostrar_detalles_del_cliente|--#
    #----------------------------------#
    def desactivar(self):
        self.__estado = "Inactivo"
    def activar(self):
        self.__estado = "Activo"
    def mostrar_informacion(self):
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}\n"
            f"Estado: {self.__estado}"
        )
    #--------------------------------#
    #--|representacion_del_cliente|--#
    #--------------------------------#
    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono} | "
            f"Estado: {self.__estado}"
        )