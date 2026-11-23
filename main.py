from cliente import Cliente
from servicio import Servicio, ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import ErrorSistemaFJ
import logging
#---------------------------------------#
#--|configuracion_del_sistema_de_logs|--#
#---------------------------------------#
logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)
clientes = []
servicios = []
reservas = []
#-----------------------#
#--|mostrar_el_titulo|--#
#-----------------------#
def mostrar_titulo():
    print("\n" + "=" * 55)
    print(" software fj - Sistema integral")
    print(" gestion de clientes, servicios y reservas")
    print("=" * 55)
#--------------------------#
#--|leer_datos_numericos|--#
#--------------------------#
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un numero entero.")
def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un numero valido.")
#------------------------#
#--|registrar_clientes|--#
#------------------------#
def registrar_cliente(nombre, correo, telefono):
    try:
        cliente = Cliente(nombre, correo, telefono)
        for cliente_existente in clientes:
            if cliente_existente.correo.lower() == cliente.correo.lower():
                raise ErrorSistemaFJ("Ya existe un cliente con ese correo electronico.")
        clientes.append(cliente)
    except ErrorSistemaFJ as error:
        logger.error("Error al registrar cliente: %s", error)
        print("Error:", error)
        return None
    except (ValueError, TypeError) as error:
        logger.error("Datos invalidos del cliente: %s", error)
        print("Error:", error)
        return None
    else:
        logger.info("Cliente registrado correctamente: %s", cliente.id)
        print("Cliente registrado correctamente.")
        return cliente
    finally:
        print("Proceso de registro de cliente finalizado.")
#----------------------#
#--|mostrar_clientes|--#
#----------------------#
def mostrar_clientes():
    print("\nla lista de clientes")
    if not clientes:
        print("No hay clientes registrados.")
        return
    for cliente in clientes:
        print(cliente)
#------------------------#
#--|modificar_clientes|--#
#------------------------#
def modificar_cliente(id_cliente):
    cliente = next((c for c in clientes if c.id == id_cliente), None)
    if cliente is None:
        print("No se encontro el cliente.")
        return
    print("\n Deja el campo vacio si no deseas modificarlo.")
    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")
    telefono = input("Nuevo telefono: ")
    try:
        nuevo_correo = correo if correo else cliente.correo
        for cliente_existente in clientes:
            if (cliente_existente.id != cliente.id and cliente_existente.correo.lower() == nuevo_correo.lower()):
                raise ErrorSistemaFJ("Ya existe otro cliente con ese correo electronico.")
        cliente.actualizar_datos(nombre if nombre else None, correo if correo else None, telefono if telefono else None)
        logger.info("Cliente %s actualizado.", cliente.id)
        print("Cliente actualizado correctamente.")
    except ErrorSistemaFJ as error:
        logger.error("Error al actualizar cliente: %s", error)
        print("Error:", error)
    except (ValueError, TypeError) as error:
        logger.error("Datos invalidos al modificar cliente: %s", error)
        print("Error:", error)
#--------------------------------#
#--|cambiar_estado_del_cliente|--#
#--------------------------------#
def cambiar_estado_cliente(id_cliente):
    cliente = next((c for c in clientes if c.id == id_cliente), None)
    if cliente is None:
        print("No se encontro el cliente.")
        return
    if cliente.estado == "Activo":
        cliente.desactivar()
        print("Cliente desactivado correctamente.")
    else:
        cliente.activar()
        print("Cliente activado correctamente.")
    logger.info("Estado del cliente %s actualizado.", cliente.id)
#-------------------------#
#--|registrar_servicios|--#
#-------------------------#
def registrar_servicio(servicio):
    try:
        if not isinstance(servicio, Servicio):
            raise ErrorSistemaFJ("El servicio proporcionado no es valido.")
        servicios.append(servicio)
    except ErrorSistemaFJ as error:
        logger.error("Error al registrar servicio: %s", error)
        print("Error:", error)
        return None
    else:
        logger.info("Servicio registrado correctamente: %s", servicio.id)
        print("Servicio registrado correctamente.")
        return servicio
    finally:
        print("Proceso de registro de servicio finalizado.")
#-----------------------#
#--|mostrar_servicios|--#
#-----------------------#
def mostrar_servicios():
    print("\n la lista de servicios")
    if not servicios:
        print("No hay servicios registrados.")
        return
    for servicio in servicios:
        print(servicio.mostrar_informacion())
#---------------------------------#
#--|cambiar_estado_del_servicio|--#
#---------------------------------#
def cambiar_estado_servicio(id_servicio):
    servicio = next(
        (s for s in servicios if s.id == id_servicio),
        None
    )
    if servicio is None:
        print("No se encontro el servicio.")
        return
    if servicio.estado == "Disponible":
        servicio.desactivar()
        print("Servicio desactivado correctamente.")
    else:
        servicio.activar()
        print("Servicio activado correctamente.")
    logger.info("Estado del servicio %s actualizado.", servicio.id)
#-------------------#
#--|crear_reserva|--#
#-------------------#
def crear_reserva(cliente, servicio, duracion):
    try:
        reserva = Reserva(cliente, servicio, duracion)
        reservas.append(reserva)
    except ErrorSistemaFJ as error:
        logger.error("Error al crear reserva: %s", error)
        print("Error:", error)
        return None
    except (ValueError, TypeError) as error:
        logger.error("Datos invalidos para la reserva: %s", error)
        print("Error:", error)
        return None
    else:
        logger.info("Reserva creada correctamente: %s", reserva.id)
        print("Reserva creada correctamente.")
        return reserva
    finally:
        print("Proceso de creacion de reserva finalizado.")
#----------------------#
#--|mostrar_reservas|--#
#----------------------#
def mostrar_reservas():
    print("\n la lista de reservas")
    if not reservas:
        print("No hay reservas registradas.")
        return
    for reserva in reservas:
        print(reserva)
#--------------------------------------#
#--|confirmar_y_cancelar_una_reserva|--#
#--------------------------------------#
def buscar_reserva(id_reserva):
    return next((r for r in reservas if r.id == id_reserva), None)
def confirmar_reserva(id_reserva):
    reserva = buscar_reserva(id_reserva)
    if reserva is None:
        print("No se encontro la reserva.")
        return
    try:
        print(reserva.confirmar())
    except ErrorSistemaFJ as error:
        logger.error("Error al confirmar reserva: %s", error)
        print("Error:", error)
def cancelar_reserva(id_reserva):
    reserva = buscar_reserva(id_reserva)
    if reserva is None:
        print("No se encontro la reserva.")
        return
    try:
        print(reserva.cancelar())
    except ErrorSistemaFJ as error:
        logger.error("Error al cancelar reserva: %s", error)
        print("Error:", error)
#--------------------------#
#--|procesar_una_reserva|--#
#--------------------------#
def procesar_reserva(id_reserva, descuento=0):
    reserva = buscar_reserva(id_reserva)
    if reserva is None:
        print("No se encontro la reserva.")
        return
    try:
        costo = reserva.procesar(descuento)
        print(f"Reserva procesada correctamente. Costo: ${costo:.2f}")
    except ErrorSistemaFJ as error:
        logger.error("Error al procesar reserva: %s", error)
        print("Error:", error)
#------------------------------#
#--|menu_de_gestion_clientes|--#
#------------------------------#
def menu_clientes():
    while True:
        print("\n gestion de clientes")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Modificar cliente")
        print("4. Activar o desactivar cliente")
        print("5. Regresar al menu principal")
        opcion = leer_entero("Selecciona una opcion: ")
        if opcion == 1:
            nombre = input("Nombre: ")
            correo = input("Correo electronico: ")
            telefono = input("Telefono: ")
            registrar_cliente(nombre, correo, telefono)
        elif opcion == 2:
            mostrar_clientes()
        elif opcion == 3:
            mostrar_clientes()
            id_cliente = leer_entero("Id del cliente: ")
            modificar_cliente(id_cliente)
        elif opcion == 4:
            mostrar_clientes()
            id_cliente = leer_entero("Id del cliente: ")
            cambiar_estado_cliente(id_cliente)
        elif opcion == 5:
            break
        else:
            print("Opcion no valida.")
#-------------------------------#
#--|menu_de_gestion_servicios|--#
#-------------------------------#
def menu_servicios():
    while True:
        print("\n gestion de servicios")
        print("1. Registrar reserva de sala")
        print("2. Registrar alquiler de equipo")
        print("3. Registrar asesoria")
        print("4. Mostrar servicios")
        print("5. Activar o desactivar servicio")
        print("6. Regresar al menu principal")
        opcion = leer_entero("Selecciona una opcion: ")
        if opcion == 1:
            nombre = input("Nombre de la sala: ")
            descripcion = input("Descripcion: ")
            capacidad = leer_entero("Capacidad de personas: ")
            costo = leer_numero("Costo por hora: $")
            try:
                servicio = ReservaSala(nombre, descripcion, capacidad, costo)
                registrar_servicio(servicio)
            except (ValueError, TypeError) as error:
                logger.error("Error al crear sala: %s", error)
                print("Error:", error)
        elif opcion == 2:
            nombre = input("Nombre del equipo: ")
            descripcion = input("Descripcion: ")
            tipo = input("Tipo de equipo: ")
            costo = leer_numero("Costo por dia: $")
            try:
                servicio = AlquilerEquipo(nombre, descripcion, tipo, costo)
                registrar_servicio(servicio)
            except (ValueError, TypeError) as error:
                logger.error("Error al crear equipo: %s", error)
                print("Error:", error)
        elif opcion == 3:
            nombre = input("Nombre de la asesoria: ")
            descripcion = input("Descripcion: ")
            especialidad = input("Especialidad: ")
            costo = leer_numero("Costo por hora: $")
            try:
                servicio = Asesoria(nombre, descripcion, especialidad, costo)
                registrar_servicio(servicio)
            except (ValueError, TypeError) as error:
                logger.error("Error al crear asesoria: %s", error)
                print("Error:", error)
        elif opcion == 4:
            mostrar_servicios()
        elif opcion == 5:
            mostrar_servicios()
            id_servicio = leer_entero("Id del servicio: ")
            cambiar_estado_servicio(id_servicio)
        elif opcion == 6:
            break
        else:
            print("Opcion no valida.")
#------------------------------#
#--|menu_de_gestion_reservas|--#
#------------------------------#
def menu_reservas():
    while True:
        print("\n gestion de reservas")
        print("1. Crear reserva")
        print("2. Mostrar reservas")
        print("3. Confirmar reserva")
        print("4. Cancelar reserva")
        print("5. Procesar reserva")
        print("6. Regresar al menu principal")
        opcion = leer_entero("Selecciona una opcion: ")
        if opcion == 1:
            if not clientes or not servicios:
                print("Primero debes registrar clientes y servicios.")
                continue
            mostrar_clientes()
            id_cliente = leer_entero("Id del cliente: ")
            cliente = next((c for c in clientes if c.id == id_cliente), None)
            mostrar_servicios()
            id_servicio = leer_entero("Id del servicio: ")
            servicio = next((s for s in servicios if s.id == id_servicio), None)
            duracion = leer_numero("Duracion: ")
            if cliente is None or servicio is None:
                print("El cliente o el servicio seleccionado no existe.")
            else:
                crear_reserva(cliente, servicio, duracion)
        elif opcion == 2:
            mostrar_reservas()
        elif opcion == 3:
            mostrar_reservas()
            id_reserva = leer_entero("Id de la reserva: ")
            confirmar_reserva(id_reserva)
        elif opcion == 4:
            mostrar_reservas()
            id_reserva = leer_entero("Id de la reserva: ")
            cancelar_reserva(id_reserva)
        elif opcion == 5:
            mostrar_reservas()
            id_reserva = leer_entero("Id de la reserva: ")
            descuento = leer_numero("Descuento (0 a 100): ")
            procesar_reserva(id_reserva, descuento)
        elif opcion == 6:
            break
        else:
            print("Opcion no valida.")
#--------------------#
#--|menu_principal|--#
#--------------------#
def main():
    while True:
        try:
            mostrar_titulo()
            print("1. Gestionar clientes")
            print("2. Gestionar servicios")
            print("3. Gestionar reservas")
            print("4. Salir")
            opcion = leer_entero("\nSeleccione una opcion: ")
            if opcion == 1:
                menu_clientes()
            elif opcion == 2:
                menu_servicios()
            elif opcion == 3:
                menu_reservas()
            elif opcion == 4:
                print("\nGracias por utilizar el sistema Software FJ.")
                break
            else:
                print("\nError: Seleccione una opcion valida.")
        except Exception as error:
            logger.error("Error inesperado en el menu principal: %s", error)
            print(f"\nOcurrio un error inesperado: {error}")
        finally:
            logger.info("Finalizo una ejecucion del menu principal.")
if __name__ == "__main__":
    main()