import strawberry
from strawberry import auto
from circuits import models, filtersets

__all__ = (
    'CircuitTerminationFilter',
    'CircuitFilter',
    'CircuitTypeFilter',
    'ProviderFilter',
    'ProviderAccountFilter',
    'ProviderNetworkFilter',
)


@strawberry.django.filter(models.CircuitTermination, lookups=True)
class CircuitTerminationFilter(filtersets.CircuitTerminationFilterSet):
    id: auto
    term_side: auto
    port_speed: auto
    upstream_speed: auto
    xconnect_id: auto
    description: auto
    cable_end: auto
    # q: auto
    circuit_id: auto
    site_id: auto
    site: auto
    # provider_network_id: auto


@strawberry.django.filter(models.Circuit, lookups=True)
class CircuitFilter(filtersets.CircuitFilterSet):
    id: auto
    cid: auto
    description: auto
    install_date: auto
    termination_date: auto
    commit_rate: auto
    provider_id: auto
    provider: auto
    provider_account_id: auto
    # provider_network_id: auto
    type_id: auto
    type: auto
    status: auto
    # region_id: auto
    # region: auto
    # site_group_id: auto
    # site_group: auto
    # site_id: auto
    # site: auto


@strawberry.django.filter(models.CircuitType, lookups=True)
class CircuitTypeFilter(filtersets.CircuitTypeFilterSet):
    id: auto
    name: auto
    slug: auto
    description: auto


@strawberry.django.filter(models.Provider, lookups=True)
class ProviderFilter(filtersets.ProviderFilterSet):
    id: auto
    name: auto
    slug: auto
    # region_id: auto
    # region: auto
    # site_group_id: auto
    # site_group: auto
    # site_id: auto
    # site: auto
    # asn_id: auto


@strawberry.django.filter(models.ProviderAccount, lookups=True)
class ProviderAccountFilter(filtersets.ProviderAccountFilterSet):
    id: auto
    name: auto
    account: auto
    description: auto
    # provider_id: auto
    # provider: auto


@strawberry.django.filter(models.ProviderNetwork, lookups=True)
class ProviderNetworkFilter(filtersets.ProviderNetworkFilterSet):
    id: auto
    name: auto
    service_id: auto
    description: auto
    # provider_id: auto
    # provider: auto
