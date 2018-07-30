1. Copy files/SAI_Opennsl_patch/sonic-buildimage/*.mk to your_sonic-buildimage/platform/broadcom/
2. Untar brcm-sai and opennsl source code tarball to your_sonic-buildimage/src, and rename them into brcm-sai and opennsl
3. Apply brcm-sai_3.2.0.1 patches to brcm-sai
4. Apply opennsl_3.5.0.3 patches to opennsl
5. Done!

Patch tree:

```
files/SAI_Opennsl_patch/README.md
files/SAI_Opennsl_patch/sonic-buildimage/
files/SAI_Opennsl_patch/sonic-buildimage/sai.mk
files/SAI_Opennsl_patch/sonic-buildimage/sdk.mk
files/SAI_Opennsl_patch/opennsl_3.5.0.3/
files/SAI_Opennsl_patch/opennsl_3.5.0.3/0005-support-kernel-3.16.0-5.patch
files/SAI_Opennsl_patch/opennsl_3.5.0.3/0003-try-to-fix-platform-cannot-support-bcm56873.patch
files/SAI_Opennsl_patch/opennsl_3.5.0.3/0001-adpat-platform.patch
files/SAI_Opennsl_patch/opennsl_3.5.0.3/0002-adapt-to-debian8.0.patch
files/SAI_Opennsl_patch/opennsl_3.5.0.3/0004-support-build-to-debian-packages.patch
files/SAI_Opennsl_patch/opennsl_3.5.0.3/0006-support-led-enable.patch
files/SAI_Opennsl_patch/brcm-sai_3.2.0.1/
files/SAI_Opennsl_patch/brcm-sai_3.2.0.1/0003-merge-sai-1.2.4.patch
files/SAI_Opennsl_patch/brcm-sai_3.2.0.1/0002-add-data-config.bcm.patch
files/SAI_Opennsl_patch/brcm-sai_3.2.0.1/0004-support-dev-0x873.patch
files/SAI_Opennsl_patch/brcm-sai_3.2.0.1/0001-adapt-to-compile-opennsl-locally.patch
files/SAI_Opennsl_patch/brcm-sai_3.2.0.1/0005-support-initialization.patch
```
