import unittest
from context import hcvb_lab

class HcvbLabTest(unittest.TestCase):
    def test_is_bcr_01(self):
        return(hcvb_lab.is_bcr('105_a_110_a_CSF_UNS_NA_BCR_IgM'))

    def test_is_bcr_02(self):
        return(hcvb_lab.is_bcr('10311_c_UNS_1000000_IGG_IGVH'))

    def test_is_bcr_03(self):
        self.assertFalse(hcvb_lab.is_bcr('10311_c_PB_T_CD8_817944_TCR_vb'))



if __name__ == '__main__':
    unittest.main()
