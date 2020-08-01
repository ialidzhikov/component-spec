import dataclasses
import enum
import typing

dc = dataclasses.dataclass


class SchemaVersion(enum.Enum):
    V1 = 'v1'
    V2 = 'v2'


class ComponentType(enum.Enum):
    GARDENER_COMPONENT = 'gardenerComponent'
    OCI_COMPONENT = 'ociComponent'

    OCI_IMAGE = 'ociImage'
    WEB_DEPENDENCY = 'web'
    GENERIC = 'generic'


@dc(frozen=True)
class Metadata:
    schemaVersion: SchemaVersion


@dc(frozen=True)
class ComponentReference:
    name: str
    version: str
    type: ComponentType


@dc(frozen=True)
class ResolvableComponentReference(ComponentReference):
    pass


@dc(frozen=True)
class DependencyComponent(ComponentReference):
    pass


@dc(frozen=True)
class OciImage(DependencyComponent):
    imageReference: str


@dc(frozen=True)
class WebDependency(DependencyComponent):
    url: str


@dc(frozen=True)
class GenericDependency(DependencyComponent):
    pass


@dc
class ResolvableComponent:
    dependencies: typing.List[
        typing.Union[
            ComponentReference,
            DependencyComponent,
        ]
    ]


@dc
class GardenerComponent(ResolvableComponent):
    pass


@dc
class OciComponent(ResolvableComponent):
    pass

@dc
class ComponentDescriptor:
    meta: Metadata
    components: typing.List[
        typing.Union[
            GardenerComponent,
            OciComponent,
        ]
    ]