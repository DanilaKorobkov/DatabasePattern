# Internal
from tries.mappers.mapper_registry import mapperRegistry


def mapperFor(domainClass):

    def impl(mapperClass):

        mapperRegistry.setMapperFor(domainClass, mapperClass)
        return mapperClass

    return impl



class IMapper:

    def find(self, primaryKey):
        raise NotImplementedError