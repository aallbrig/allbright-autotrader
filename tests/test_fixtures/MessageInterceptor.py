class MessageInterceptor:
    _intercepted_message: str = ""

    def get_intercepted_message(self):
        return self._intercepted_message

    def set_intercepted_message(self, message: str):
        self._intercepted_message = message