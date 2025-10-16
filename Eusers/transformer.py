from typing import Any, List, Optional, Tuple
from Eusers.schema import UserResponseSchema,UserRequestSchemaByUserID


def get_euser_data_transformer(modelData: Tuple[List[Any], int]) -> dict:
    details, total = modelData

    def transform(body: UserRequestSchemaByUserID):
        return UserResponseSchema.model_validate(body, from_attributes=True).model_dump()

    response = list(map(transform, details))
    return {"total": total, "data": response}
