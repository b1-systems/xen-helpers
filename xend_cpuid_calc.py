#!/usr/bin/env python
# extracted from linux/arch/x86/include/asm/cpufeature.h


FLAGS = {
 "X86_FEATURE_FPU": (0*32+ 0)
,"X86_FEATURE_VME": (0*32+ 1)
,"X86_FEATURE_DE":  (0*32+ 2)
,"X86_FEATURE_PSE": (0*32+ 3)
,"X86_FEATURE_TSC": (0*32+ 4)
,"X86_FEATURE_MSR": (0*32+ 5)
,"X86_FEATURE_PAE": (0*32+ 6)
,"X86_FEATURE_MCE": (0*32+ 7)
,"X86_FEATURE_CX8": (0*32+ 8)
,"X86_FEATURE_APIC":    (0*32+ 9)
,"X86_FEATURE_SEP": (0*32+11)
,"X86_FEATURE_MTRR":    (0*32+12)
,"X86_FEATURE_PGE": (0*32+13)
,"X86_FEATURE_MCA": (0*32+14)
,"X86_FEATURE_CMOV":    (0*32+15)

,"X86_FEATURE_PAT": (0*32+16)
,"X86_FEATURE_PSE36":   (0*32+17)
,"X86_FEATURE_PN":  (0*32+18)
,"X86_FEATURE_CLFLSH":  (0*32+19)
,"X86_FEATURE_DS":  (0*32+21)
,"X86_FEATURE_ACPI":    (0*32+22)
,"X86_FEATURE_MMX": (0*32+23)
,"X86_FEATURE_FXSR":    (0*32+24)
,"X86_FEATURE_XMM": (0*32+25)
,"X86_FEATURE_XMM2":    (0*32+26)
,"X86_FEATURE_SELFSNOOP":   (0*32+27)
,"X86_FEATURE_HT":  (0*32+28)
,"X86_FEATURE_ACC": (0*32+29)
,"X86_FEATURE_IA64":    (0*32+30)
,"X86_FEATURE_PBE": (0*32+31)



,"X86_FEATURE_SYSCALL": (1*32+11)
,"X86_FEATURE_MP":  (1*32+19)
,"X86_FEATURE_NX":  (1*32+20)
,"X86_FEATURE_MMXEXT":  (1*32+22)
,"X86_FEATURE_FXSR_OPT":    (1*32+25)
,"X86_FEATURE_GBPAGES": (1*32+26)
,"X86_FEATURE_RDTSCP":  (1*32+27)
,"X86_FEATURE_LM":  (1*32+29)
,"X86_FEATURE_3DNOWEXT":    (1*32+30)
,"X86_FEATURE_3DNOW":   (1*32+31)


,"X86_FEATURE_RECOVERY":    (2*32+ 0)
,"X86_FEATURE_LONGRUN": (2*32+ 1)
,"X86_FEATURE_LRTI":    (2*32+ 3)



,"X86_FEATURE_CXMMX":   (3*32+ 0)
,"X86_FEATURE_K6_MTRR": (3*32+ 1)
,"X86_FEATURE_CYRIX_ARR":   (3*32+ 2)
,"X86_FEATURE_CENTAUR_MCR": (3*32+ 3)

,"X86_FEATURE_K8":  (3*32+ 4)
,"X86_FEATURE_K7":  (3*32+ 5)
,"X86_FEATURE_P3":  (3*32+ 6)
,"X86_FEATURE_P4":  (3*32+ 7)
,"X86_FEATURE_CONSTANT_TSC":    (3*32+ 8)
,"X86_FEATURE_UP":  (3*32+ 9)
,"X86_FEATURE_FXSAVE_LEAK": (3*32+10)
,"X86_FEATURE_ARCH_PERFMON":    (3*32+11)
,"X86_FEATURE_PEBS":    (3*32+12)
,"X86_FEATURE_BTS": (3*32+13)
,"X86_FEATURE_SYSCALL32":   (3*32+14)
,"X86_FEATURE_SYSENTER32":  (3*32+15)
,"X86_FEATURE_REP_GOOD":    (3*32+16)
,"X86_FEATURE_MFENCE_RDTSC":    (3*32+17)
,"X86_FEATURE_LFENCE_RDTSC":    (3*32+18)
,"X86_FEATURE_11AP":    (3*32+19)
,"X86_FEATURE_NOPL":    (3*32+20)
,"X86_FEATURE_ALWAYS":  (3*32+21)
,"X86_FEATURE_XTOPOLOGY":   (3*32+22)
,"X86_FEATURE_TSC_RELIABLE":    (3*32+23)
,"X86_FEATURE_NONSTOP_TSC": (3*32+24)
,"X86_FEATURE_CLFLUSH_MONITOR": (3*32+25)
,"X86_FEATURE_EXTD_APICID": (3*32+26)
,"X86_FEATURE_AMD_DCM": (3*32+27)
,"X86_FEATURE_APERFMPERF":  (3*32+28)
,"X86_FEATURE_EAGER_FPU":   (3*32+29)
,"X86_FEATURE_NONSTOP_TSC_S3":  (3*32+30)


,"X86_FEATURE_XMM3":    (4*32+ 0)
,"X86_FEATURE_PCLMULQDQ":   (4*32+ 1)
,"X86_FEATURE_DTES64":  (4*32+ 2)
,"X86_FEATURE_MWAIT":   (4*32+ 3)
,"X86_FEATURE_DSCPL":   (4*32+ 4)
,"X86_FEATURE_VMX": (4*32+ 5)
,"X86_FEATURE_SMX": (4*32+ 6)
,"X86_FEATURE_EST": (4*32+ 7)
,"X86_FEATURE_TM2": (4*32+ 8)
,"X86_FEATURE_SSSE3":   (4*32+ 9)
,"X86_FEATURE_CID": (4*32+10)
,"X86_FEATURE_FMA": (4*32+12)
,"X86_FEATURE_CX16":    (4*32+13)
,"X86_FEATURE_XTPR":    (4*32+14)
,"X86_FEATURE_PDCM":    (4*32+15)
,"X86_FEATURE_PCID":    (4*32+17)
,"X86_FEATURE_DCA": (4*32+18)
,"X86_FEATURE_XMM4_1":  (4*32+19)
,"X86_FEATURE_XMM4_2":  (4*32+20)
,"X86_FEATURE_X2APIC":  (4*32+21)
,"X86_FEATURE_MOVBE":   (4*32+22)
,"X86_FEATURE_POPCNT":  (4*32+23)
,"X86_FEATURE_TSC_DEADLINE_TIMER":  (4*32+24)
,"X86_FEATURE_AES": (4*32+25)
,"X86_FEATURE_XSAVE":   (4*32+26)
,"X86_FEATURE_OSXSAVE": (4*32+27)
,"X86_FEATURE_AVX": (4*32+28)
,"X86_FEATURE_F16C":    (4*32+29)
,"X86_FEATURE_RDRAND":  (4*32+30)
,"X86_FEATURE_HYPERVISOR":  (4*32+31)


,"X86_FEATURE_XSTORE":  (5*32+ 2)
,"X86_FEATURE_XSTORE_EN":   (5*32+ 3)
,"X86_FEATURE_XCRYPT":  (5*32+ 6)
,"X86_FEATURE_XCRYPT_EN":   (5*32+ 7)
,"X86_FEATURE_ACE2":    (5*32+ 8)
,"X86_FEATURE_ACE2_EN": (5*32+ 9)
,"X86_FEATURE_PHE": (5*32+10)
,"X86_FEATURE_PHE_EN":  (5*32+11)
,"X86_FEATURE_PMM": (5*32+12)
,"X86_FEATURE_PMM_EN":  (5*32+13)


,"X86_FEATURE_LAHF_LM": (6*32+ 0)
,"X86_FEATURE_CMP_LEGACY":  (6*32+ 1)
,"X86_FEATURE_SVM": (6*32+ 2)
,"X86_FEATURE_EXTAPIC": (6*32+ 3)
,"X86_FEATURE_CR8_LEGACY":  (6*32+ 4)
,"X86_FEATURE_ABM": (6*32+ 5)
,"X86_FEATURE_SSE4A":   (6*32+ 6)
,"X86_FEATURE_MISALIGNSSE": (6*32+ 7)
,"X86_FEATURE_3DNOWPREFETCH":   (6*32+ 8)
,"X86_FEATURE_OSVW":    (6*32+ 9)
,"X86_FEATURE_IBS": (6*32+10)
,"X86_FEATURE_XOP": (6*32+11)
,"X86_FEATURE_SKINIT":  (6*32+12)
,"X86_FEATURE_WDT": (6*32+13)
,"X86_FEATURE_LWP": (6*32+15)
,"X86_FEATURE_FMA4":    (6*32+16)
,"X86_FEATURE_TCE": (6*32+17)
,"X86_FEATURE_NODEID_MSR":  (6*32+19)
,"X86_FEATURE_TBM": (6*32+21)
,"X86_FEATURE_TOPOEXT": (6*32+22)
,"X86_FEATURE_PERFCTR_CORE":    (6*32+23)
,"X86_FEATURE_PERFCTR_NB":  (6*32+24)
,"X86_FEATURE_PERFCTR_L2":  (6*32+28)

,"X86_FEATURE_IDA": (7*32+ 0)
,"X86_FEATURE_ARAT":    (7*32+ 1)
,"X86_FEATURE_CPB": (7*32+ 2)
,"X86_FEATURE_EPB": (7*32+ 3)
,"X86_FEATURE_XSAVEOPT":    (7*32+ 4)
,"X86_FEATURE_PLN": (7*32+ 5)
,"X86_FEATURE_PTS": (7*32+ 6)
,"X86_FEATURE_DTHERM":  (7*32+ 7)
,"X86_FEATURE_HW_PSTATE":   (7*32+ 8)
,"X86_FEATURE_PROC_FEEDBACK":   (7*32+ 9)


,"X86_FEATURE_TPR_SHADOW":  (8*32+ 0)
,"X86_FEATURE_VNMI":    (8*32+ 1)
,"X86_FEATURE_FLEXPRIORITY":    (8*32+ 2)
,"X86_FEATURE_EPT": (8*32+ 3)
,"X86_FEATURE_VPID":    (8*32+ 4)
,"X86_FEATURE_NPT": (8*32+ 5)
,"X86_FEATURE_LBRV":    (8*32+ 6)
,"X86_FEATURE_SVML":    (8*32+ 7)
,"X86_FEATURE_NRIPS":   (8*32+ 8)
,"X86_FEATURE_TSCRATEMSR":  (8*32+ 9)
,"X86_FEATURE_VMCBCLEAN":   (8*32+10)
,"X86_FEATURE_FLUSHBYASID": (8*32+11)
,"X86_FEATURE_DECODEASSISTS":   (8*32+12)
,"X86_FEATURE_PAUSEFILTER": (8*32+13)
,"X86_FEATURE_PFTHRESHOLD": (8*32+14)



,"X86_FEATURE_FSGSBASE":    (9*32+ 0)
,"X86_FEATURE_TSC_ADJUST":  (9*32+ 1)
,"X86_FEATURE_BMI1":    (9*32+ 3)
,"X86_FEATURE_HLE": (9*32+ 4)
,"X86_FEATURE_AVX2":    (9*32+ 5)
,"X86_FEATURE_SMEP":    (9*32+ 7)
,"X86_FEATURE_BMI2":    (9*32+ 8)
,"X86_FEATURE_ERMS":    (9*32+ 9)
,"X86_FEATURE_INVPCID": (9*32+10)
,"X86_FEATURE_RTM": (9*32+11)
,"X86_FEATURE_RDSEED":  (9*32+18)
,"X86_FEATURE_ADX": (9*32+19)
,"X86_FEATURE_SMAP":    (9*32+20)
}


# extracted from linux/arch/x86/kernel/cpu/capflags.c
DISPLAY = {
    "X86_FEATURE_FPU"        : "fpu",
    "X86_FEATURE_VME"        : "vme",
    "X86_FEATURE_DE"         : "de",
    "X86_FEATURE_PSE"        : "pse",
    "X86_FEATURE_TSC"        : "tsc",
    "X86_FEATURE_MSR"        : "msr",
    "X86_FEATURE_PAE"        : "pae",
    "X86_FEATURE_MCE"        : "mce",
    "X86_FEATURE_CX8"        : "cx8",
    "X86_FEATURE_APIC"       : "apic",
    "X86_FEATURE_SEP"        : "sep",
    "X86_FEATURE_MTRR"       : "mtrr",
    "X86_FEATURE_PGE"        : "pge",
    "X86_FEATURE_MCA"        : "mca",
    "X86_FEATURE_CMOV"       : "cmov",
    "X86_FEATURE_PAT"        : "pat",
    "X86_FEATURE_PSE36"      : "pse36",
    "X86_FEATURE_PN"         : "pn",
    "X86_FEATURE_CLFLSH"         : "clflush",
    "X86_FEATURE_DS"         : "dts",
    "X86_FEATURE_ACPI"       : "acpi",
    "X86_FEATURE_MMX"        : "mmx",
    "X86_FEATURE_FXSR"       : "fxsr",
    "X86_FEATURE_XMM"        : "sse",
    "X86_FEATURE_XMM2"       : "sse2",
    "X86_FEATURE_SELFSNOOP"      : "ss",
    "X86_FEATURE_HT"         : "ht",
    "X86_FEATURE_ACC"        : "tm",
    "X86_FEATURE_IA64"       : "ia64",
    "X86_FEATURE_PBE"        : "pbe",
    "X86_FEATURE_SYSCALL"        : "syscall",
    "X86_FEATURE_MP"         : "mp",
    "X86_FEATURE_NX"         : "nx",
    "X86_FEATURE_MMXEXT"         : "mmxext",
    "X86_FEATURE_FXSR_OPT"       : "fxsr_opt",
    "X86_FEATURE_GBPAGES"        : "pdpe1gb",
    "X86_FEATURE_RDTSCP"         : "rdtscp",
    "X86_FEATURE_LM"         : "lm",
    "X86_FEATURE_3DNOWEXT"       : "3dnowext",
    "X86_FEATURE_3DNOW"      : "3dnow",
    "X86_FEATURE_RECOVERY"       : "recovery",
    "X86_FEATURE_LONGRUN"        : "longrun",
    "X86_FEATURE_LRTI"       : "lrti",
    "X86_FEATURE_CXMMX"      : "cxmmx",
    "X86_FEATURE_K6_MTRR"        : "k6_mtrr",
    "X86_FEATURE_CYRIX_ARR"      : "cyrix_arr",
    "X86_FEATURE_CENTAUR_MCR"    : "centaur_mcr",
    "X86_FEATURE_CONSTANT_TSC"   : "constant_tsc",
    "X86_FEATURE_UP"         : "up",
    "X86_FEATURE_ARCH_PERFMON"   : "arch_perfmon",
    "X86_FEATURE_PEBS"       : "pebs",
    "X86_FEATURE_BTS"        : "bts",
    "X86_FEATURE_REP_GOOD"       : "rep_good",
    "X86_FEATURE_NOPL"       : "nopl",
    "X86_FEATURE_XTOPOLOGY"      : "xtopology",
    "X86_FEATURE_TSC_RELIABLE"   : "tsc_reliable",
    "X86_FEATURE_NONSTOP_TSC"    : "nonstop_tsc",
    "X86_FEATURE_EXTD_APICID"    : "extd_apicid",
    "X86_FEATURE_AMD_DCM"        : "amd_dcm",
    "X86_FEATURE_APERFMPERF"     : "aperfmperf",
    "X86_FEATURE_EAGER_FPU"      : "eagerfpu",
    "X86_FEATURE_NONSTOP_TSC_S3"     : "nonstop_tsc_s3",
    "X86_FEATURE_XMM3"       : "pni",
    "X86_FEATURE_PCLMULQDQ"      : "pclmulqdq",
    "X86_FEATURE_DTES64"         : "dtes64",
    "X86_FEATURE_MWAIT"      : "monitor",
    "X86_FEATURE_DSCPL"      : "ds_cpl",
    "X86_FEATURE_VMX"        : "vmx",
    "X86_FEATURE_SMX"        : "smx",
    "X86_FEATURE_EST"        : "est",
    "X86_FEATURE_TM2"        : "tm2",
    "X86_FEATURE_SSSE3"      : "ssse3",
    "X86_FEATURE_CID"        : "cid",
    "X86_FEATURE_FMA"        : "fma",
    "X86_FEATURE_CX16"       : "cx16",
    "X86_FEATURE_XTPR"       : "xtpr",
    "X86_FEATURE_PDCM"       : "pdcm",
    "X86_FEATURE_PCID"       : "pcid",
    "X86_FEATURE_DCA"        : "dca",
    "X86_FEATURE_XMM4_1"         : "sse4_1",
    "X86_FEATURE_XMM4_2"         : "sse4_2",
    "X86_FEATURE_X2APIC"         : "x2apic",
    "X86_FEATURE_MOVBE"      : "movbe",
    "X86_FEATURE_POPCNT"         : "popcnt",
    "X86_FEATURE_TSC_DEADLINE_TIMER" : "tsc_deadline_timer",
    "X86_FEATURE_AES"        : "aes",
    "X86_FEATURE_XSAVE"      : "xsave",
    "X86_FEATURE_AVX"        : "avx",
    "X86_FEATURE_F16C"       : "f16c",
    "X86_FEATURE_RDRAND"         : "rdrand",
    "X86_FEATURE_HYPERVISOR"     : "hypervisor",
    "X86_FEATURE_XSTORE"         : "rng",
    "X86_FEATURE_XSTORE_EN"      : "rng_en",
    "X86_FEATURE_XCRYPT"         : "ace",
    "X86_FEATURE_XCRYPT_EN"      : "ace_en",
    "X86_FEATURE_ACE2"       : "ace2",
    "X86_FEATURE_ACE2_EN"        : "ace2_en",
    "X86_FEATURE_PHE"        : "phe",
    "X86_FEATURE_PHE_EN"         : "phe_en",
    "X86_FEATURE_PMM"        : "pmm",
    "X86_FEATURE_PMM_EN"         : "pmm_en",
    "X86_FEATURE_LAHF_LM"        : "lahf_lm",
    "X86_FEATURE_CMP_LEGACY"     : "cmp_legacy",
    "X86_FEATURE_SVM"        : "svm",
    "X86_FEATURE_EXTAPIC"        : "extapic",
    "X86_FEATURE_CR8_LEGACY"     : "cr8_legacy",
    "X86_FEATURE_ABM"        : "abm",
    "X86_FEATURE_SSE4A"      : "sse4a",
    "X86_FEATURE_MISALIGNSSE"    : "misalignsse",
    "X86_FEATURE_3DNOWPREFETCH"  : "3dnowprefetch",
    "X86_FEATURE_OSVW"       : "osvw",
    "X86_FEATURE_IBS"        : "ibs",
    "X86_FEATURE_XOP"        : "xop",
    "X86_FEATURE_SKINIT"         : "skinit",
    "X86_FEATURE_WDT"        : "wdt",
    "X86_FEATURE_LWP"        : "lwp",
    "X86_FEATURE_FMA4"       : "fma4",
    "X86_FEATURE_TCE"        : "tce",
    "X86_FEATURE_NODEID_MSR"     : "nodeid_msr",
    "X86_FEATURE_TBM"        : "tbm",
    "X86_FEATURE_TOPOEXT"        : "topoext",
    "X86_FEATURE_PERFCTR_CORE"   : "perfctr_core",
    "X86_FEATURE_PERFCTR_NB"     : "perfctr_nb",
    "X86_FEATURE_PERFCTR_L2"     : "perfctr_l2",
    "X86_FEATURE_IDA"        : "ida",
    "X86_FEATURE_ARAT"       : "arat",
    "X86_FEATURE_CPB"        : "cpb",
    "X86_FEATURE_EPB"        : "epb",
    "X86_FEATURE_XSAVEOPT"       : "xsaveopt",
    "X86_FEATURE_PLN"        : "pln",
    "X86_FEATURE_PTS"        : "pts",
    "X86_FEATURE_DTHERM"         : "dtherm",
    "X86_FEATURE_HW_PSTATE"      : "hw_pstate",
    "X86_FEATURE_PROC_FEEDBACK"  : "proc_feedback",
    "X86_FEATURE_TPR_SHADOW"     : "tpr_shadow",
    "X86_FEATURE_VNMI"       : "vnmi",
    "X86_FEATURE_FLEXPRIORITY"   : "flexpriority",
    "X86_FEATURE_EPT"        : "ept",
    "X86_FEATURE_VPID"       : "vpid",
    "X86_FEATURE_NPT"        : "npt",
    "X86_FEATURE_LBRV"       : "lbrv",
    "X86_FEATURE_SVML"       : "svm_lock",
    "X86_FEATURE_NRIPS"      : "nrip_save",
    "X86_FEATURE_TSCRATEMSR"     : "tsc_scale",
    "X86_FEATURE_VMCBCLEAN"      : "vmcb_clean",
    "X86_FEATURE_FLUSHBYASID"    : "flushbyasid",
    "X86_FEATURE_DECODEASSISTS"  : "decodeassists",
    "X86_FEATURE_PAUSEFILTER"    : "pausefilter",
    "X86_FEATURE_PFTHRESHOLD"    : "pfthreshold",
    "X86_FEATURE_FSGSBASE"       : "fsgsbase",
    "X86_FEATURE_TSC_ADJUST"     : "tsc_adjust",
    "X86_FEATURE_BMI1"       : "bmi1",
    "X86_FEATURE_HLE"        : "hle",
    "X86_FEATURE_AVX2"       : "avx2",
    "X86_FEATURE_SMEP"       : "smep",
    "X86_FEATURE_BMI2"       : "bmi2",
    "X86_FEATURE_ERMS"       : "erms",
    "X86_FEATURE_INVPCID"        : "invpcid",
    "X86_FEATURE_RTM"        : "rtm",
    "X86_FEATURE_RDSEED"         : "rdseed",
    "X86_FEATURE_ADX"        : "adx",
}

import sys, StringIO
OUTPUT = [0 for n in xrange(9)]

if len(sys.argv) < 2:
    print "usage: xend_cpuid_calc.py flag [flag...]"
    print "\nflags can be extracted from /proc/cpuinfo"
    sys.exit(1)

for arg in sys.argv[1:]:
    for k,v in DISPLAY.iteritems():
        if v == arg.lower():
            bank = FLAGS[k]/32
            pos = FLAGS[k]%32
            OUTPUT[bank] = OUTPUT[bank] | (1 << pos)
            #print FLAGS[k]

def genstr(mask):
    rv = ""
    for bit in xrange(32, -1, -1):
        if (1 << bit) & mask:
            rv += "x"
        else:
            rv += "0"
    return rv

def output():
    buf = StringIO.StringIO()
    """
    (cpuid
     ( (1
        (
            (eax xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
            (edx xx0xxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
            (ebx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
            (ecx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx0)
            )
        )
        ) )
    """
    #buf.write("cpuid = [ '1:edx=" + genstr(OUTPUT[0]) + ",ecx=" + genstr(OUTPUT[4]) + "',\n"
    #          #"          '2:',\n" 
    #          " '0x80000001:edx=" + genstr(OUTPUT[1]) + ",ecx=" + genstr(OUTPUT[6]) + "',\n"
    #          "]"
    #          )
    buf.write("""
(cpuid
    ( (1
        (
        (edx """ + genstr(OUTPUT[0]) + """)
        (ecx """ + genstr(OUTPUT[4]) + """)
        )
    )
    (0x80000001
        (
        (edx """ + genstr(OUTPUT[1]) + """)
        (ecx """ + genstr(OUTPUT[6]) + """)
        )
    )
  )
)
               """)
    
    print buf.getvalue()

#print OUTPUT
output()
