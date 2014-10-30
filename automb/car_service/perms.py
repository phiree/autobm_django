from permission.logics import AuthorPermissionLogic
from permission.logics import CollaboratorsPermissionLogic

PERMISSION_LOGICS = (
    ('car_service.ServiceType', AuthorPermissionLogic()),

    )