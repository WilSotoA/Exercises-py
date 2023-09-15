class notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(notificador):
    def notificar(self):
        print(f"Enviando mensaje por mail a {self.usuario.email}")


class NotificadorSMS(notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")
