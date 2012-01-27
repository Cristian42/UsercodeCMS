import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_100_1_3aD.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_10_1_GKq.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_11_1_5v9.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_12_1_LBm.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_13_1_n5l.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_14_1_XTU.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_15_1_B7b.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_16_1_HTx.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_17_1_Hai.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_18_1_zkH.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_19_1_mYl.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_1_1_MdW.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_20_1_u52.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_21_1_w7K.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_22_1_HhT.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_23_1_TB6.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_24_1_dDY.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_25_1_D9E.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_26_1_5iZ.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_27_1_NFA.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_28_1_UvW.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_29_1_R16.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_2_1_TlR.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_30_1_t4G.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_31_1_ItL.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_32_1_6lk.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_33_1_SNt.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_34_1_8D9.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_35_1_WWh.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_36_1_KJN.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_37_1_6RO.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_38_1_xC0.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_39_1_jZ5.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_3_1_B38.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_40_1_m6H.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_41_1_mHv.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_42_1_kzE.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_43_1_c9J.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_44_1_261.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_45_1_m9g.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_46_1_OnJ.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_47_1_l6O.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_48_1_JDx.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_49_1_DRJ.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_4_1_yHL.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_50_1_a1n.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_51_1_Yt5.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_52_1_9cO.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_53_1_glY.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_54_1_MDG.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_55_1_0Mf.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_56_1_oDH.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_57_1_DrM.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_58_1_Mkk.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_59_1_g2x.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_5_1_l2r.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_60_1_tzF.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_61_1_fvl.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_62_1_LaS.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_63_1_fdr.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_64_1_wiK.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_65_1_RR0.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_66_1_lcg.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_67_1_cDU.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_68_1_MCf.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_69_1_Rte.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_6_1_20f.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_70_1_5qJ.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_71_1_EOO.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_72_1_CWB.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_73_1_igx.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_74_1_1P5.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_75_1_25k.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_76_1_YD9.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_77_1_sUT.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_78_1_2Vi.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_79_1_Sz3.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_7_1_ZVt.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_80_1_Lg7.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_81_1_KDY.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_82_1_Tq2.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_83_1_kKv.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_84_1_M2p.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_85_1_d6W.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_86_1_sk6.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_87_1_Q9B.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_88_1_u7X.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_89_1_wOi.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_8_1_Y9B.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_90_1_Opx.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_91_1_msr.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_92_1_Ktb.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_93_1_DRu.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_94_1_BUR.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_95_1_FFN.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_96_1_r3U.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_97_1_fhJ.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_98_1_tKV.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_99_1_u6K.root',
       '/store/user/zuranski/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/MH_200_MFF_20_CTau70_7TeVGEN_SIM_RAWDEBUG/cd4c914f57f2d8cc290fde369820ecf4/GEN-SIM-RAWDEBUG_9_1_ohk.root' ] );


secFiles.extend( [
               ] )


