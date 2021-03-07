from django.db import models

class StudentData(models.Model):
    """
    Model class to store basic student information
    """
    idn = models.CharField(
        max_length=100,
        unique=True
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )   
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    applied_to_graduate = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    gpa = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    cgpa = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


class Subject_1(models.Model):
    """
    Model classes for each of the 52 courses separately
    """
    student = models.ForeignKey(
        StudentData,
        related_name="subject_1_student_data",
        on_delete=models.CASCADE,
    )
    cpst_3030 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_2(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_2_student_data",
        on_delete=models.CASCADE,
    )
    csci_1110 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_3(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_3_student_data",
        on_delete=models.CASCADE,
    )
    csci_1120 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_4(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_4_student_data",
        on_delete=models.CASCADE,
    )
    csci_1170 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


class Subject_5(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_5_student_data",
        on_delete=models.CASCADE,
    )
    csci_3110 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


class Subject_6(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_6_student_data",
        on_delete=models.CASCADE,
    )
    csci_3120 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_7(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_7_student_data",
        on_delete=models.CASCADE,
    )
    csci_3130 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_8(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_8_student_data",
        on_delete=models.CASCADE,
    )
    csci_3160 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_9(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_9_student_data",
        on_delete=models.CASCADE,
    )
    csci_3171 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_10(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_10_student_data",
        on_delete=models.CASCADE,
    )
    csci_4155 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_11(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_11_student_data",
        on_delete=models.CASCADE,
    )
    csci_4176 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )



class Subject_12(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_12_student_data",
        on_delete=models.CASCADE,
    )
    eced_3003 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_13(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_13_student_data",
        on_delete=models.CASCADE,
    )
    eced_3102 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_14(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_14_student_data",
        on_delete=models.CASCADE,
    )
    eced_3201 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_15(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_15_student_data",
        on_delete=models.CASCADE,
    )
    eced_3204 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_16(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_16_student_data",
        on_delete=models.CASCADE,
    )
    eced_3300 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_17(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_17_student_data",
        on_delete=models.CASCADE,
    )
    eced_3401 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_18(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_18_student_data",
        on_delete=models.CASCADE,
    )
    eced_3500 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_19(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_19_student_data",
        on_delete=models.CASCADE,
    )
    eced_4102 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_20(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_20_student_data",
        on_delete=models.CASCADE,
    )
    eced_4130 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_21(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_21_student_data",
        on_delete=models.CASCADE,
    )
    eced_4260 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_22(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_22_student_data",
        on_delete=models.CASCADE,
    )
    eced_4402 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_23(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_23_student_data",
        on_delete=models.CASCADE,
    )
    eced_4504 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_24(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_24_student_data",
        on_delete=models.CASCADE,
    )
    eced_4601 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_25(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_25_student_data",
        on_delete=models.CASCADE,
    )
    eced_4900 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_26(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_26_student_data",
        on_delete=models.CASCADE,
    )
    eced_4901 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_27(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_27_student_data",
        on_delete=models.CASCADE,
    )
    eced_8891 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_28(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_28_student_data",
        on_delete=models.CASCADE,
    )
    eced_8892 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_29(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_29_student_data",
        on_delete=models.CASCADE,
    )
    econ_1101 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_30(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_30_student_data",
        on_delete=models.CASCADE,
    )
    econ_1102 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_31(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_31_student_data",
        on_delete=models.CASCADE,
    )
    engi_8890 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_32(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_32_student_data",
        on_delete=models.CASCADE,
    )
    hist_2205 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_33(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_33_student_data",
        on_delete=models.CASCADE,
    )
    hpro_2255 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_34(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_34_student_data",
        on_delete=models.CASCADE,
    )
    hpro_4412 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_35(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_35_student_data",
        on_delete=models.CASCADE,
    )
    hstc_2500 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_36(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_36_student_data",
        on_delete=models.CASCADE,
    )
    hstc_3001 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_37(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_37_student_data",
        on_delete=models.CASCADE,
    )
    hstc_3415 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_38(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_38_student_data",
        on_delete=models.CASCADE,
    )
    ieng_4558 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_39(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_39_student_data",
        on_delete=models.CASCADE,
    )
    jour_3660 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_40(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_40_student_data",
        on_delete=models.CASCADE,
    )
    math_2112 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_41(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_41_student_data",
        on_delete=models.CASCADE,
    )
    musc_2204 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_42(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_42_student_data",
        on_delete=models.CASCADE,
    )
    phil_2130 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_43(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_43_student_data",
        on_delete=models.CASCADE,
    )
    phil_2475 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_44(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_44_student_data",
        on_delete=models.CASCADE,
    )
    phil_2805 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_45(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_45_student_data",
        on_delete=models.CASCADE,
    )
    phyc_2515 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_46(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_46_student_data",
        on_delete=models.CASCADE,
    )
    phyc_3200 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_47(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_47_student_data",
        on_delete=models.CASCADE,
    )
    phyl_1101 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_48(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_48_student_data",
        on_delete=models.CASCADE,
    )
    rusn_1020 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_49(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_49_student_data",
        on_delete=models.CASCADE,
    )
    span_1021 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_50(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_50_student_data",
        on_delete=models.CASCADE,
    )
    stat_2080 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

class Subject_51(models.Model):
    student = models.ForeignKey(
        StudentData,
        related_name="subject_51_student_data",
        on_delete=models.CASCADE,
    )
    stat_3340 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )