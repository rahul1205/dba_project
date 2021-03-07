from main.models import *

def load_data(values):
    """
    A utility to create object(load a record in a table)
    This will be used in API
    """
    stud, boolean = StudentData.objects.get_or_create(
        idn=values[3],
        first_name=values[5],
        last_name=values[4],
        applied_to_graduate=values[10],
        gpa=values[9],
        cgpa=values[8]
    )
    Subject_1.objects.create(
        student=stud,
        cpst_3030=values[14]
    )

    Subject_2.objects.create(
        student=stud,
        csci_1110=values[15]
    )

    Subject_3.objects.create(
        student=stud,
        csci_1120=values[16]
    )

    Subject_4.objects.create(
        student=stud,
        csci_1170=values[17]
    )

    Subject_5.objects.create(
        student=stud,
        csci_3110=values[18]
    )

    Subject_6.objects.create(
        student=stud,
        csci_3120=values[19]
    )

    Subject_7.objects.create(
        student=stud,
        csci_3130=values[20]
    )

    Subject_8.objects.create(
        student=stud,
        csci_3160=values[21]
    )

    Subject_9.objects.create(
        student=stud,
        csci_3171=values[22]
    )

    Subject_10.objects.create(
        student=stud,
        csci_4155=values[23]
    )

    Subject_11.objects.create(
        student=stud,
        csci_4176=values[24]
    )

    Subject_12.objects.create(
        student=stud,
        eced_3003=values[25]
    )

    Subject_13.objects.create(
        student=stud,
        eced_3102=values[26]
    )

    Subject_14.objects.create(
        student=stud,
        eced_3201=values[27]
    )

    Subject_15.objects.create(
        student=stud,
        eced_3204=values[28]
    )

    Subject_16.objects.create(
        student=stud,
        eced_3300=values[29]
    )

    Subject_17.objects.create(
        student=stud,
        eced_3401=values[30]
    )

    Subject_18.objects.create(
        student=stud,
        eced_3500=values[31]
    )

    Subject_19.objects.create(
        student=stud,
        eced_4102=values[32]
    )

    Subject_20.objects.create(
        student=stud,
        eced_4130=values[33]
    )

    Subject_21.objects.create(
        student=stud,
        eced_4260=values[34]
    )

    Subject_22.objects.create(
        student=stud,
        eced_4402=values[35]
    )

    Subject_23.objects.create(
        student=stud,
        eced_4504=values[36]
    )

    Subject_24.objects.create(
        student=stud,
        eced_4601=values[37]
    )

    Subject_25.objects.create(
        student=stud,
        eced_4900=values[38]
    )

    Subject_26.objects.create(
        student=stud,
        eced_4901=values[39]
    )

    Subject_27.objects.create(
        student=stud,
        eced_8891=values[40]
    )

    Subject_28.objects.create(
        student=stud,
        eced_8892=values[41]
    )

    Subject_29.objects.create(
    student=stud,
    econ_1101=values[42]
   )

    Subject_30.objects.create(
    student=stud,
    econ_1102=values[43]
   )

    Subject_31.objects.create(
    student=stud,
    engi_8890=values[44]
   )

    Subject_32.objects.create(
    student=stud,
    hist_2205=values[45]
   )

    Subject_33.objects.create(
    student=stud,
    hpro_2255=values[46]
   )

    Subject_34.objects.create(
    student=stud,
    hpro_4412=values[47]
   )

    Subject_35.objects.create(
    student=stud,
    hstc_2500=values[48]
   )

    Subject_36.objects.create(
    student=stud,
    hstc_3001=values[49]
   )

    Subject_37.objects.create(
    student=stud,
    hstc_3415=values[50]
   )

    Subject_38.objects.create(
    student=stud,
    ieng_4558=values[51]
   )

    Subject_39.objects.create(
    student=stud,
    jour_3660=values[52]
   )

    Subject_40.objects.create(
    student=stud,
    math_2112=values[53]
   )

    Subject_41.objects.create(
    student=stud,
    musc_2204=values[54]
   )

    Subject_42.objects.create(
    student=stud,
    phil_2130=values[55]
   )

    Subject_43.objects.create(
    student=stud,
    phil_2475=values[56]
   )

    Subject_44.objects.create(
    student=stud,
    phil_2805=values[57]
   )

    Subject_45.objects.create(
    student=stud,
    phyc_2515=values[58]
   )

    Subject_46.objects.create(
    student=stud,
    phyc_3200=values[59]
   )

    Subject_47.objects.create(
    student=stud,
    phyl_1101=values[60]
   )

    Subject_48.objects.create(
    student=stud,
    rusn_1020=values[61]
   )

    Subject_49.objects.create(
    student=stud,
    span_1021=values[62]
   )

    Subject_50.objects.create(
    student=stud,
    stat_2080=values[63]
   )

    Subject_51.objects.create(
    student=stud,
    stat_3340=values[64]
   )
