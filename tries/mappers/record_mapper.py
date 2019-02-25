from tries.mappers.i_mapper import *
# Internal
from tries.domain.record import Record


@mapperFor(Record)
class RecordMapper(IMapper):
    pass