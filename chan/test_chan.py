import unittest

from chan import *

class TestChan(unittest.TestCase):
    def test_chan(self):
        # pyramid point cloud
        test_points = [
            (0.09964782850167017, 0.46903571101375924, 0.012097950134946217),
            (-0.1755456491170128, 0.5456326040668025, 0.20478850115406594),
            (-0.21830065947676314, 0.7209408956737615, -0.13513941138262817),
            (-0.044629166881916316, 0.5348308556270078, -0.15079826891715226),
            (0.45229166746139526, 0.847848653793335, 0.24407055974006653),
            (-0.4783439636230469, 0.5599833726882935, 0.470014750957489),
            (-0.2732780873775482, 0.9194132089614868, -0.440346896648407),
            (0.07073074579238892, 0.020669907331466675, -0.1684664785861969)
        ]

        hull_points = [
            (-0.2732780873775482, 0.9194132089614868, -0.440346896648407),
            (-0.4783439636230469, 0.5599833726882935, 0.470014750957489),
            (0.07073074579238892, 0.020669907331466675, -0.1684664785861969),
            (0.45229166746139526, 0.847848653793335, 0.24407055974006653)
        ]

        # generate a mesh
        test_mesh = chan(test_points, "test_chan_mesh.obj")

        # check face count, should be 4
        self.assertEqual(len(test_mesh.get_faces()), 4)

        # check face contents, all should be in the hull points list
        faces = test_mesh.get_faces()
        for this_face in faces:
            for this_vert in this_face:
                self.assertTrue(test_mesh.get_verts()[this_vert-1] in hull_points)


if __name__ == "__main__":
    unittest.main()
