# Celestica DX010 and AS5820 Platform modules

CEL_DX010_PLATFORM_MODULE_VERSION = 0.9
CEL_AS5820_PLATFORM_MODULE_VERSION = 0.9

export CEL_DX010_PLATFORM_MODULE_VERSION
export CEL_AS5820_PLATFORM_MODULE_VERSION

CEL_DX010_PLATFORM_MODULE = platform-modules-dx010_$(CEL_DX010_PLATFORM_MODULE_VERSION)_amd64.deb
$(CEL_DX010_PLATFORM_MODULE)_SRC_PATH = $(PLATFORM_PATH)/sonic-platform-modules-cel
$(CEL_DX010_PLATFORM_MODULE)_DEPENDS += $(LINUX_HEADERS) $(LINUX_HEADERS_COMMON)
$(CEL_DX010_PLATFORM_MODULE)_PLATFORM = x86_64-cel_seastone-r0
SONIC_DPKG_DEBS += $(CEL_DX010_PLATFORM_MODULE)

CEL_AS5820_PLATFORM_MODULE = platform-modules-as5820_$(CEL_AS5820_PLATFORM_MODULE_VERSION)_amd64.deb
$(CEL_AS5820_PLATFORM_MODULE)_PLATFORM = x86_64-cel_as5820-r0
$(eval $(call add_extra_package,$(CEL_DX010_PLATFORM_MODULE),$(CEL_AS5820_PLATFORM_MODULE)))
