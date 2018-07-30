BRCM_SAI_VERSION = 3.2.0.1

BRCM_SAI = libsaibcm_$(BRCM_SAI_VERSION)_amd64.deb
$(BRCM_SAI)_SRC_PATH = $(SRC_PATH)/brcm-sai
$(BRCM_SAI)_DEPENDS += $(BRCM_LIBOPENNSL_DEV)
SONIC_DPKG_DEBS += $(BRCM_SAI)

BRCM_SAI_DEV = libsaibcm-dev_$(BRCM_SAI_VERSION)_amd64.deb
$(BRCM_SAI_DEV)_DEPENDS += $(BRCM_SAI)
#$(BRCM_SAI_DEV)_RDEPENDS += $(BRCM_SAI)
$(eval $(call add_derived_package,$(BRCM_SAI),$(BRCM_SAI_DEV)))

BRCM_SAI_DBG = libsaibcm-dbg_$(BRCM_SAI_VERSION)_amd64.deb
$(BRCM_SAI_DBG)_DEPENDS += $(BRCM_SAI)
$(eval $(call add_derived_package,$(BRCM_SAI),$(BRCM_SAI_DBG)))
