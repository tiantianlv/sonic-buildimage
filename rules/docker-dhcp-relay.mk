# Docker image for DHCP relay

DOCKER_DHCP_RELAY = docker-dhcp-relay.gz
$(DOCKER_DHCP_RELAY)_PATH = $(DOCKERS_PATH)/docker-dhcp-relay
$(DOCKER_DHCP_RELAY)_DEPENDS += $(ISC_DHCP_COMMON) $(ISC_DHCP_RELAY) $(ISC_DHCP_CLIENT)
$(DOCKER_DHCP_RELAY)_LOAD_DOCKERS = $(DOCKER_CONFIG_ENGINE)
SONIC_DOCKER_IMAGES += $(DOCKER_DHCP_RELAY)
SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_DHCP_RELAY)


$(DOCKER_DHCP_RELAY)_CONTAINER_NAME = dhcp_relay
$(DOCKER_DHCP_RELAY)_RUN_OPT += --net=host --privileged -t
$(DOCKER_DHCP_RELAY)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
