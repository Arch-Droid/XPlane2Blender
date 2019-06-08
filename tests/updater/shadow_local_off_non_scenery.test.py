import inspect

from typing import Tuple

import os
import sys

import bpy
from io_xplane2blender import xplane_config
from io_xplane2blender.tests import *

__dirname__ = os.path.dirname(__file__)

def filterLines(line:Tuple[str])->bool:
    return (isinstance(line[0],str)
            and ("GLOBAL_no_shadow" in line[0]
                 or "ATTR_shadow" in line[0]
                 or "ATTR_no_shadow"))

class TestShadowLocalOffNonScenery(XPlaneTestCase):
    def test_properties_correct(self):
        for mat in [bpy.data.materials["Material_shadow_should_be_on_1_shared"],
                    bpy.data.materials["Material_shadow_should_be_on_2_shared"],]:
            self.assertTrue(mat.xplane.shadow_local)

        for layer_idx in range(4):
            self.assertIsNone(bpy.context.scene.xplane.layers[layer_idx].get("shadow"))

    def test_01_aircraft_force_global_shadows(self):
        filename = inspect.stack()[0].function
        self.assertLayerExportEqualsFixture(
            0,
            os.path.join(__dirname__, "fixtures", filename + ".obj"),
            filename,
            filterLines
        )

    def test_02_cockpit_force_global_shadows(self):
        filename = inspect.stack()[0].function
        self.assertLayerExportEqualsFixture(
            1,
            os.path.join(__dirname__, "fixtures", filename + ".obj"),
            filename,
            filterLines
        )


runTestCases([TestShadowLocalOffNonScenery])
