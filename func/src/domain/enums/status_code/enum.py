from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    INTERNAL_SERVER_ERROR = 100
    TRANSPORT_LAYER_ERROR = 69
    UNABLE_TO_UPDATE_IN_MONGO = 99
    INTERNAL_TRANSPORT_ERROR = 59
    FIELD_RECEIVED_IS_NOT_A_VALID_ENUM = 89

    def __repr__(self):
        return self.value
