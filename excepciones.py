#-------------------------------------------#
#--|clase_base_de_excepciones_del_sistema|--#
#-------------------------------------------#
class ErrorSistemaFJ(Exception):
    """Excepcion base para los errores del sistema software jf."""
    pass
class ErrorCliente(ErrorSistemaFJ):
    """Excepcion relacionada con la gestion de clientes."""
    pass
class ErrorServicio(ErrorSistemaFJ):
    """Excepcion relacionada con la gestion de servicios."""
    pass
class ErrorReserva(ErrorSistemaFJ):
    """Excepcion relacionada con la gestion de reservas."""
    pass
class ErrorDatoDuplicado(ErrorSistemaFJ):
    """Excepcion cuando se intenta registrar un dato duplicado."""
    pass
class ErrorDatoNoEncontrado(ErrorSistemaFJ):
    """Excepcion cuando no se encuentra un registro."""
    pass