# Internal
from tries.mappers.session_mapper import SessionMapper


result = SessionMapper().find(1)
print(result[0].__dict__)