"""Device handler for Trust ZCTS-808 Contact sensors."""
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Identify,
    OnOff,
    PowerConfiguration,
)
from zigpy.zcl.clusters.security import IasZone

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)

MANUFACTURER_SPECIFIC_CLUSTER_ID = 0xFFFF


class ZCTS808(CustomDevice):
    """Trust ZCTS-808."""

    signature = {
        #  <SimpleDescriptor endpoint=1 profile=260 device_type=1026
        #  device_version=1
        #  input_clusters=[0, 3, 1280, 65535, 1]
        #  output_clusters=[]>
        MODELS_INFO: [("ADUROLIGHT", "CSW_ADUROLIGHT")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.IAS_ZONE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    IasZone.cluster_id,
                    MANUFACTURER_SPECIFIC_CLUSTER_ID,
                    PowerConfiguration.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            }
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    IasZone.cluster_id,
                    MANUFACTURER_SPECIFIC_CLUSTER_ID,
                    PowerConfiguration.cluster_id,
                ],
            }
        }
    }
