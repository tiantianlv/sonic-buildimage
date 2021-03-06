# isc-dhcp packages

ISC_DHCP_VERSION = 4.3.3-6

export ISC_DHCP_VERSION

ISC_DHCP_COMMON = isc-dhcp-common_$(ISC_DHCP_VERSION)_amd64.deb
$(ISC_DHCP_COMMON)_SRC_PATH = $(SRC_PATH)/isc-dhcp
SONIC_MAKE_DEBS += $(ISC_DHCP_COMMON)

ISC_DHCP_CLIENT = isc-dhcp-client_$(ISC_DHCP_VERSION)_amd64.deb
$(ISC_DHCP_CLIENT)_SRC_PATH = $(SRC_PATH)/isc-dhcp
SONIC_MAKE_DEBS += $(ISC_DHCP_CLIENT)

ISC_DHCP_RELAY = isc-dhcp-relay_$(ISC_DHCP_VERSION)_amd64.deb
$(eval $(call add_derived_package,$(ISC_DHCP_COMMON),$(ISC_DHCP_RELAY),$(ISC_DHCP_CLIENT)))
