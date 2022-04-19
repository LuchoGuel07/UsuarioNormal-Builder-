from usuarioNormal import usuarioNormal

class UsuarioBuilder:
    def __init__(self):
        self.nombre = ""
        self.cedula = ""
        self.genero = ""
        self.estadoCivil = ""
        self.direccion = ""
        self.deportes = []
        self.entretenimiemto = {}
        self.vehiculo = {"tipo":None,"marca":None,"modelo":None,"placa":None}
    @staticmethod
    def usuario():
        return UsuarioBuilder()
    def conNombre(self,nombre):
        self.nombre = nombre
        return self
    def conCedula(self,cedula):
        self.cedula = cedula
        return self
    def conGenero(self,genero):
        self.genero = genero
        return self
    def conEstadoCivil(self,estadoCivil):
        self.estadoCivil = estadoCivil
        return self
    def conDireccion(self,direccion):
        self.direccion = direccion
        return self
    def conDeportes(self,deportes):
        self.deportes = deportes.copy()
        return self
    def conEntretenimiento (self,entretenimiemto):
        self.entretenimiemto = entretenimiemto.copy()
        return self
    def conVehiculo(self,vehiculo):
        self.vehiculo = vehiculo.copy()
        return self
    def builder(self):
        return Usuario(self.nombre, self.cedula,self.genero,self.estadoCivil,self.direccion,self.deportes,self.entretenimiemto,self.vehiculo)
    
usuario = UsuarioBuilder.usuario()
x = usuario.conNombre("Pepito Perez").conCedula("123456789").conGenero('M').conEstadoCivil("S").conDireccion("CALLE C").builder()
x = verUsuario()