from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

BAT_CHOICE = (
    ("0", "Select"),
    #
    ("All Batches", "All Batches"),
    ("B.Tech", "B.Tech"),
    ("B.Tech 20", "B.Tech 20"),
    ("B.Tech 19", "B.Tech 19"),
    ("B.Tech 18", "B.Tech 18"),
    ("B.Tech 17", "B.Tech 17"),
    ("B.Tech 16", "B.Tech 16"),
    ("B.Des", "B.Des"),
    ("B.Des 20", "B.Des 20"),
    ("B.Des 19", "B.Des 19"),
    ("B.Des 18", "B.Des 18"),
    ("B.Des 17", "B.Des 17"),
    ("B.Des 16", "B.Des 16"),
    ("M.Tech", "M.Tech"),
    ("M.Tech 20", "M.Tech 20"),
    ("M.Tech 19", "M.Tech 19"),
    ("M.Tech 18", "M.Tech 18"),
    ("M.Tech 17", "M.Tech 17"),
    ("M.Tech 16", "M.Tech 16"),
    ("PhD", "PhD"),
    ("PhD 20", "PhD 20"),
    ("PhD 19", "PhD 19"),
    ("PhD 18", "PhD 18"),
    ("PhD 17", "PhD 17"),
    ("PhD 16", "PhD 16"),
)
DEP_CHOICE = (
    ("0", "Select"),
    #
    ("All Branches", "All Branches"),
    ("Computer Science and Engineering", "Computer Science and Engineering"),
    ("Biosciences and Bioengineering", "Biosciences and Bioengineering"),
    ("Chemical Engineering", "Chemical Engineering"),
    ("Civil Engineering", "Civil Engineering"),
    ("Chemistry", "Chemistry"),
    ("Design", "Design"),
    ("Electronics and Electrical Engineering", "Electronics and Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
    ("Electronics and Communications Engineering", "Electronics and Communications Engineering"),
    ("Mathematics and Computing", "Mathematics and Computing"),
    ("Engineering Physics", "Engineering Physics"),
    ("Humanities and Social Sciences", "Humanities and Social Sciences"),
)
REM_CHOICE = (
    ("0", "Select"),
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Week before", "Week before"),
    ("Custom", "Custom"),
)

# Create your models here.
# class Cleanup(models.Model):
#     task = models.ManyToManyField(Task,blank=True,related_name = 'task')
#     bt = models.ManyToManyField(BT,blank=True,related_name = 'bt')
#     ch = models.ManyToManyField(CH,blank=True,related_name = 'ch')
#     cl = models.ManyToManyField(CL,blank=True,related_name = 'cl')
#     ce = models.ManyToManyField(CE,blank=True,related_name = 'ce')
#     cse = models.ManyToManyField(CSE,blank=True,related_name = 'cse')
#     des = models.ManyToManyField(DES,blank=True,related_name = 'des')
#     ece = models.ManyToManyField(ECE,blank=True,related_name = 'ece')
#     eee = models.ManyToManyField(EEE,blank=True,related_name = 'eee')
#     ma = models.ManyToManyField(MA,blank=True,related_name = 'ma')
#     me = models.ManyToManyField(ME,blank=True,related_name = 'me')
#     ph = models.ManyToManyField(PH,blank=True,related_name = 'ph')
#     swc = models.ManyToManyField(SWC,blank=True,related_name = 'swc')
#     codingclub = models.ManyToManyField(CODINGCLUB,blank=True,related_name = 'codingclub')
#     aeroclub = models.ManyToManyField(AEROCLUB,blank=True,related_name = 'aeroclub')
#     astroclub = models.ManyToManyField(ASTROCLUB,blank=True,related_name = 'astroclub')
#     caclub = models.ManyToManyField(CACLUB,blank=True,related_name = 'caclub')
#     eeclub = models.ManyToManyField(EECLUB,blank=True,related_name = 'eeclub')
#     prakriticlub = models.ManyToManyField(PRAKRITICLUB,blank=True,related_name = 'prakriticlub')
#     fncclub = models.ManyToManyField(FNCCLUB,blank=True,related_name = 'fncclub')
#     roboticsclub = models.ManyToManyField(ROBOTICSCLUB,blank=True,related_name = 'roboticsclub')
#     edclub = models.ManyToManyField(EDCLUB,blank=True,related_name = 'edclub')
#     ugclub = models.ManyToManyField(UGCLUB,blank=True,related_name = 'ugclub')
#     alcherclub = models.ManyToManyField(ALCHERCLUB,blank=True,related_name = 'alcherclub')
#     technicheclub = models.ManyToManyField(TechnicheCLUB,blank=True,related_name = 'technicheclub')
#     otherclub = models.ManyToManyField(OTHERCLUB,blank=True,related_name = 'otherclub')
#     sailclub = models.ManyToManyField(SAILCLUB,blank=True,related_name = 'sailclub')
#     aiclub = models.ManyToManyField(AICLUB,blank=True,related_name = 'aiclub')
#     ccdclub = models.ManyToManyField(CCDCLUB,blank=True,related_name = 'ccdclub')


# Create your models here.
class Task(models.Model):
    CAT_CHOICE = (
        ("0", "Academic Activities"),
    )
    EVENT_TYPE=(
        ("0", "Select"),
        ("Assignments","Assignments"),
        ("Quizzes","Quizzes"),
        ("Exam","Exam"),
        ("Viva","Viva"),
        ("Lab Report","Lab Report"),
    )
    COURSENAME = (
        ("0", "Select"),
        ("BT101", "BT101"),
        ("BT201", "BT201"),
        ("BT202", "BT202"),
        ("BT203", 'BT203'),
        ("BT204", 'BT204'),
        ("BT205", 'BT205'),
        ("BT206", 'BT206'),
        ("BT207", 'BT207'),
        ('BT208', 'BT208'),
        ('BT209', 'BT209'),
        ('BT211', 'BT211'),
        ("BT301", "BT301"),
        ("BT302", "BT302"),
        ("BT303", 'BT303'),
        ("BT304", 'BT304'),
        ("BT305", 'BT305'),
        ("BT306", 'BT306'),
        ("BT307", 'BT307'),
        ('BT308', 'BT308'),
        ('BT311', 'BT311'),
        ('BT312', 'BT312'),
        ('BT3xx', 'BT3xx'),
        ('BT401', 'BT401'),
        ('BT402', 'BT402'),

        ("CH101", "CH101"),
        ("CH110", 'CH110'),
        ('CH211', 'CH211'),
        ("CH212", "CH212"),
        ("CH221", "CH221"),
        ("CH222", 'CH222'),
        ('CH2xx', 'CH2xx'),
        ("CH231", 'CH231'),
        ("CH223", 'CH223'),
        ("CH233", 'CH233'),
        ("CH301", 'CH301'),
        ('CH302', 'CH302'),
        ('CH314', 'CH314'),
        ('CH316', 'CH316'),
        ('CH323', 'CH323'),
        ("CH331", "CH331"),
        ("CH332", "CH332"),
        ('CH334', 'CH334'),
        ("CH335", 'CH335'),
        ("CH401", 'CH401'),
        ("CH498", 'CH498'),
        ("CH499", 'CH499'),
        ('CH4xx', 'CH4xx'),
        ('CH4xxx', 'CH4xxx'),

        ("CL101", "CL101"),
        ("CL201", "CL201"),
        ("CL202", "CL202"),
        ("CL203", 'CL203'),
        ("CL204", 'CL204'),
        ("CL205", 'CL205'),
        ("CL206", 'CL206'),
        ("CL207", 'CL207'),
        ('CL208', 'CL208'),
        ('CL209', 'CL209'),
        ('CL210H', 'CL210H'),
        ('CL211H', 'CL211H'),
        ("CL301", "CL301"),
        ("CL302", "CL302"),
        ("CL303", 'CL303'),
        ("CL304", 'CL304'),
        ("CL305", 'CL305'),
        ("CL306", 'CL306'),
        ("CL310", 'CL310'),
        ('CL311', 'CL311'),
        ('CL312', 'CL312'),
        ('CL313', 'CL313'),
        ('CL314H', 'CL314H'),
        ('CL315H', 'CL315H'),
        ('CL3xx', 'CL3xx'),
        ('CLxxx', 'CLxxx'),
        ('CL4xx', 'CL4xx'),

        ("CE201", "CE201"),
        ("CE202", "CE202"),
        ("CE203", 'CE203'),
        ("CE205", 'CE205'),
        ("CE206", 'CE206'),
        ("CE207", 'CE207'),
        ('CE208', 'CE208'),
        ('CE211', 'CE211'),
        ('CE212', 'CE212'),
        ('CE213', 'CE213'),
        ('CE214', 'CE214'),
        ('CE215', 'CE215'),
        ('CE220', 'CE220'),
        ('CE221', 'CE221'),
        ('CE222', 'CE222'),
        ('CE223', 'CE223'),
        ("CE302", "CE302"),
        ("CE303", 'CE303'),
        ("CE304", 'CE304'),
        ("CE305", 'CE305'),
        ('CE308', 'CE308'),
        ('CE309', 'CE309'),
        ('CE313', 'CE313'),
        ('CE314', 'CE314'),
        ('CE316', 'CE316'),
        ('CE320', 'CE320'),
        ('CE321', 'CE321'),
        ('CE322', 'CE322'),
        ('CE323', 'CE323'),
        ('CE324', 'CE324'),
        ('CE402', 'CE402'),
        ('CE498', 'CE498'),
        ('CE499', 'CE499'),
        ('CExxx', 'CExxx'),
        ('CE4xx', 'CE4xx'),

        ('CS101', 'CS110'),
        ('CS110', 'CS110'),
        ("CS201", "CS201"),
        ("CS203", 'CS203'),
        ("CS204", "CS204"),
        ("CS205", 'CS205'),
        ("CS207", 'CS207'),
        ('CS221', 'CS221'),
        ('CS223', 'CS223'),
        ('CS224', 'CS224'),
        ('CS242', 'CS242'),
        ('CS245', 'CS245'),
        ('CS246', 'CS246'),
        ("CS341", "CS341"),
        ("CS342", 'CS342'),
        ("CS343", 'CS343'),
        ("CS344", 'CS344'),
        ('CS345', 'CS345'),
        ('CS346', 'CS346'),
        ('CS348', 'CS348'),
        ('CSxxx', 'CSxxx'),
        ('CS498', 'CS498'),
        ('CS499', 'CS499'),
        ('CSxxx', 'CSxxx'),
        ('CS4xx', 'CS4xx'),

        ('DD101', 'DD101'),
        ('DD102', 'DD102'),
        ('DD103', 'DD103'),
        ('DD104', 'DD104'),
        ('DD105', 'DD105'),
        ('DD111', 'DD111'),
        ('DD112', 'DD112'),
        ('DD113', 'DD113'),
        ("DD201", "DD201"),
        ('DD202', 'DD202'),
        ('DD203', 'DD201'),
        ("DD203", 'DD203'),
        ("DD204", "DD204"),
        ("DD205", 'DD205'),
        ('DD206', 'DD206'),
        ('DD212', 'DD212'),
        ('DD213', 'DD213'),
        ('DD214', 'DD214'),
        ('DD215', 'DD215'),
        ('DD216', 'DD216'),
        ("DD301", "DD301"),
        ('DD302', 'DD302'),
        ('DD303', 'DD301'),
        ("DD303", 'DD303'),
        ("DD304", "DD304"),
        ('DD311', 'DD311'),
        ('DD312', 'DD312'),
        ('DD3xX', 'DD3xx'),
        ('DD398', 'DD398'),
        ('DD401', 'DD401'),
        ('DD402', 'DD402'),
        ('DD411', 'DD411'),
        ('DD498', 'DD498'),
        ('DD499', 'DD499'),
        ('DDxxx', 'DDxxx'),
        ('DD4xx', 'DD4xx'),

        ('EE101', 'EE101'),
        ('EE102', 'EE102'),
        ("EE203", "EE203"),
        ("EE204", 'EE204'),
        ('EE205', 'EE205'),
        ("EE206", "EE206"),
        ("EE207", 'EE207'),
        ("EE210", 'EE210'),
        ('EE211', 'EE211'),
        ('EE220', 'EE220'),
        ('EE230', 'EE230'),
        ('EE250', 'EE250'),
        ('EE252', 'EE252'),
        ('EE253', 'EE253'),
        ("EE312", "EE312"),
        ("EE313", 'EE313'),
        ("EE321", 'EE321'),
        ("EE331", 'EE331'),
        ('EE332', 'EE332'),
        ('EE333', 'EE333'),
        ('EE334', 'EE334'),
        ('EE340', 'EE340'),
        ('EE351', 'EE351'),
        ('EE360', 'EE360'),
        ('EE370', 'EE370'),
        ('EE371', 'EE371'),
        ('EE380', 'EE380'),
        ('EE381', 'EE381'),
        ('EE390', 'EE390'),
        ('EE396', 'EE396'),
        ('EE398', 'EE398'),
        ('EE399', 'EE399'),
        ('EE3xx', 'EE3xx'),
        ('EE498', 'EE498'),
        ('EE499', 'EE499'),
        ('EExxx', 'EExxx'),
        ('EE4xx', 'EE4xx'),

        ('MA101', 'MA101'),
        ('MA102', 'MA102'),
        ("MA201", "MA201"),
        ("MA221", 'MA221'),
        ("MA222", "MA222"),
        ("MA224", 'MA224'),
        ("MA225", 'MA225'),
        ('MA251', 'MA251'),
        ('MA252', 'MA252'),
        ('MA250', 'MA250'),
        ('MA252', 'MA252'),
        ('MA271', 'MA271'),
        ("MA321", "MA321"),
        ("MA322", 'MA322'),
        ("MA323", 'MA323'),
        ("MA324", 'MA324'),
        ('MA351', 'MA351'),
        ('MA372', 'MA372'),
        ('MA373', 'MA373'),
        ('MA374', 'MA374'),
        ('MA3xx', 'MA3xx'),
        ('MA423', 'MA423'),
        ('MA473', 'MA473'),
        ('MA498', 'MA498'),
        ('MA499', 'MA499'),
        ('MAxxx', 'MAxxx'),
        ('MA4xx', 'MA4xx'),

        ('ME101', 'ME100'),
        ('ME110', 'ME110'),
        ("ME211", "ME211"),
        ("ME212", 'ME212'),
        ("ME213", "ME213"),
        ("ME214", 'ME214'),
        ("ME215", 'ME215'),
        ('ME216', 'ME216'),
        ("ME221", "ME221"),
        ("ME222", 'ME222'),
        ("ME223", "ME223"),
        ("ME224", 'ME224'),
        ("ME225", 'ME225'),
        ('ME226', 'ME226'),
        ('ME311', 'ME311'),
        ("ME312", "ME312"),
        ("ME313", 'ME313'),
        ("ME314", 'ME314'),
        ("ME315", 'ME315'),
        ("ME321", 'ME321'),
        ("ME322", 'ME322'),
        ("ME323", 'ME323'),
        ("ME324", 'ME324'),
        ("ME325", 'ME325'),
        ("ME326", 'ME326'),
        ('ME398', 'ME398'),
        ('ME399', 'ME399'),
        ('ME3xx', 'ME3xx'),
        ('ME401', 'ME401'),
        ('ME498', 'ME498'),
        ('ME499', 'ME499'),
        ('MExxx', 'MExxx'),
        ('ME4xx', 'ME4xx'),

        ('PH101', 'PH101'),
        ('PH102', 'PH102'),
        ('PH110', 'PH110'),
        ("PH201", "PH201"),
        ('PH202', 'PH202'),
        ('PH203', 'PH201'),
        ("PH203", 'PH203'),
        ("PH204", "PH204"),
        ("PH205", 'PH205'),
        ('PH206', 'PH206'),
        ("PH207", 'PH207'),
        ('PH208', 'PH208'),
        ('PH209', 'PH209'),
        ('PH210', 'PH210'),
        ('PH211', 'PH211'),
        ("PH301", "PH301"),
        ('PH302', 'PH302'),
        ('PH303', 'PH301'),
        ("PH303", 'PH303'),
        ("PH304", "PH304"),
        ("PH305", 'PH305'),
        ('PH306', 'PH306'),
        ("PH307", 'PH307'),
        ('PH308', 'PH308'),
        ('PH309', 'PH309'),
        ('PH310', 'PH310'),
        ('PH312', 'PH312'),
        ('PH411', 'PH411'),
        ('PH413', 'PH413'),
        ('PH415', 'PH415'),
        ('PH421', 'PH421'),
        ('PH422', 'PH422'),
        ('PHxxx', 'PHxxx'),
        ('PH4xx', 'PH4xx'),
    )
    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40,choices = CAT_CHOICE,default="Academic Activities")
    sub_event= models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name=models.CharField(max_length=100,choices=COURSENAME,default='0')
    instructor_name=models.CharField(max_length=100,null=True)
    Credit=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0)
    Marks_Of_Task=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],default=0)
    target_batch = models.CharField(max_length=13,choices = BAT_CHOICE,default="Self")
    target_branch = models.CharField(max_length=45,choices = DEP_CHOICE,default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12,choices = REM_CHOICE,default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class BT(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )

    COURSENAME = (
        ("0", "Select"),
        ("BT101", "BT101"),
        ("BT201", "BT201"),
        ("BT202", "BT202"),
        ("BT203", 'BT203'),
        ("BT204", 'BT204'),
        ("BT205", 'BT205'),
        ("BT206", 'BT206'),
        ("BT207", 'BT207'),
        ('BT208', 'BT208'),
        ('BT209', 'BT209'),
        ('BT211', 'BT211'),
        ("BT301", "BT301"),
        ("BT302", "BT302"),
        ("BT303", 'BT303'),
        ("BT304", 'BT304'),
        ("BT305", 'BT305'),
        ("BT306", 'BT306'),
        ("BT307", 'BT307'),
        ('BT308', 'BT308'),
        ('BT311', 'BT311'),
        ('BT312', 'BT312'),
        ('BT3xx', 'BT3xx'),
        ('BT401', 'BT401'),
        ('BT402', 'BT402'),


    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CH(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ("CH101", "CH101"),
        ("CH110", 'CH110'),
        ('CH211', 'CH211'),
        ("CH212", "CH212"),
        ("CH221", "CH221"),
        ("CH222", 'CH222'),
        ('CH2xx', 'CH2xx'),
        ("CH231", 'CH231'),
        ("CH223", 'CH223'),
        ("CH233", 'CH233'),
        ("CH301", 'CH301'),
        ('CH302', 'CH302'),
        ('CH314', 'CH314'),
        ('CH316', 'CH316'),
        ('CH323', 'CH323'),
        ("CH331", "CH331"),
        ("CH332", "CH332"),
        ('CH334', 'CH334'),
        ("CH335", 'CH335'),
        ("CH401", 'CH401'),
        ("CH498", 'CH498'),
        ("CH499", 'CH499'),
        ('CH4xx', 'CH4xx'),
        ('CH4xxx', 'CH4xxx'),


    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CL(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ("CL101", "CL101"),
        ("CL201", "CL201"),
        ("CL202", "CL202"),
        ("CL203", 'CL203'),
        ("CL204", 'CL204'),
        ("CL205", 'CL205'),
        ("CL206", 'CL206'),
        ("CL207", 'CL207'),
        ('CL208', 'CL208'),
        ('CL209', 'CL209'),
        ('CL210H', 'CL210H'),
        ('CL211H', 'CL211H'),
        ("CL301", "CL301"),
        ("CL302", "CL302"),
        ("CL303", 'CL303'),
        ("CL304", 'CL304'),
        ("CL305", 'CL305'),
        ("CL306", 'CL306'),
        ("CL310", 'CL310'),
        ('CL311', 'CL311'),
        ('CL312', 'CL312'),
        ('CL313', 'CL313'),
        ('CL314H', 'CL314H'),
        ('CL315H', 'CL315H'),
        ('CL3xx', 'CL3xx'),
        ('CLxxx', 'CLxxx'),
        ('CL4xx', 'CL4xx'),


    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CE(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )

    COURSENAME = (
        ("0", "Select"),
        ("CE201", "CE201"),
        ("CE202", "CE202"),
        ("CE203", 'CE203'),
        ("CE205", 'CE205'),
        ("CE206", 'CE206'),
        ("CE207", 'CE207'),
        ('CE208', 'CE208'),
        ('CE211', 'CE211'),
        ('CE212', 'CE212'),
        ('CE213', 'CE213'),
        ('CE214', 'CE214'),
        ('CE215', 'CE215'),
        ('CE220', 'CE220'),
        ('CE221', 'CE221'),
        ('CE222', 'CE222'),
        ('CE223', 'CE223'),
        ("CE302", "CE302"),
        ("CE303", 'CE303'),
        ("CE304", 'CE304'),
        ("CE305", 'CE305'),
        ('CE308', 'CE308'),
        ('CE309', 'CE309'),
        ('CE313', 'CE313'),
        ('CE314', 'CE314'),
        ('CE316', 'CE316'),
        ('CE320', 'CE320'),
        ('CE321', 'CE321'),
        ('CE322', 'CE322'),
        ('CE323', 'CE323'),
        ('CE324', 'CE324'),
        ('CE402', 'CE402'),
        ('CE498', 'CE498'),
        ('CE499', 'CE499'),
        ('CExxx', 'CExxx'),
        ('CE4xx', 'CE4xx'),



    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CSE(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ('CS101', 'CS110'),
        ('CS110', 'CS110'),
        ("CS201", "CS201"),
        ("CS203", 'CS203'),
        ("CS204", "CS204"),
        ("CS205", 'CS205'),
        ("CS207", 'CS207'),
        ('CS221', 'CS221'),
        ('CS223', 'CS223'),
        ('CS224', 'CS224'),
        ('CS242', 'CS242'),
        ('CS245', 'CS245'),
        ('CS246', 'CS246'),
        ("CS341", "CS341"),
        ("CS342", 'CS342'),
        ("CS343", 'CS343'),
        ("CS344", 'CS344'),
        ('CS345', 'CS345'),
        ('CS346', 'CS346'),
        ('CS348', 'CS348'),
        ('CSxxx', 'CSxxx'),
        ('CS498', 'CS498'),
        ('CS499', 'CS499'),
        ('CSxxx', 'CSxxx'),
        ('CS4xx', 'CS4xx'),


    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class DES(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )

    COURSENAME = (
        ("0", "Select"),
        ('DD101', 'DD101'),
        ('DD102', 'DD102'),
        ('DD103', 'DD103'),
        ('DD104', 'DD104'),
        ('DD105', 'DD105'),
        ('DD111', 'DD111'),
        ('DD112', 'DD112'),
        ('DD113', 'DD113'),
        ("DD201", "DD201"),
        ('DD202', 'DD202'),
        ('DD203', 'DD201'),
        ("DD203", 'DD203'),
        ("DD204", "DD204"),
        ("DD205", 'DD205'),
        ('DD206', 'DD206'),
        ('DD212', 'DD212'),
        ('DD213', 'DD213'),
        ('DD214', 'DD214'),
        ('DD215', 'DD215'),
        ('DD216', 'DD216'),
        ("DD301", "DD301"),
        ('DD302', 'DD302'),
        ('DD303', 'DD301'),
        ("DD303", 'DD303'),
        ("DD304", "DD304"),
        ('DD311', 'DD311'),
        ('DD312', 'DD312'),
        ('DD3xX', 'DD3xx'),
        ('DD398', 'DD398'),
        ('DD401', 'DD401'),
        ('DD402', 'DD402'),
        ('DD411', 'DD411'),
        ('DD498', 'DD498'),
        ('DD499', 'DD499'),
        ('DDxxx', 'DDxxx'),
        ('DD4xx', 'DD4xx'),

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class ECE(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ('EE101', 'EE101'),
        ('EE102', 'EE102'),
        ("EE203", "EE203"),
        ("EE204", 'EE204'),
        ('EE205', 'EE205'),
        ("EE206", "EE206"),
        ("EE207", 'EE207'),
        ("EE210", 'EE210'),
        ('EE211', 'EE211'),
        ('EE220', 'EE220'),
        ('EE230', 'EE230'),
        ('EE250', 'EE250'),
        ('EE252', 'EE252'),
        ('EE253', 'EE253'),
        ("EE312", "EE312"),
        ("EE313", 'EE313'),
        ("EE321", 'EE321'),
        ("EE331", 'EE331'),
        ('EE332', 'EE332'),
        ('EE333', 'EE333'),
        ('EE334', 'EE334'),
        ('EE340', 'EE340'),
        ('EE351', 'EE351'),
        ('EE360', 'EE360'),
        ('EE370', 'EE370'),
        ('EE371', 'EE371'),
        ('EE380', 'EE380'),
        ('EE381', 'EE381'),
        ('EE390', 'EE390'),
        ('EE396', 'EE396'),
        ('EE398', 'EE398'),
        ('EE399', 'EE399'),
        ('EE3xx', 'EE3xx'),
        ('EE498', 'EE498'),
        ('EE499', 'EE499'),
        ('EExxx', 'EExxx'),
        ('EE4xx', 'EE4xx'),

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class EEE(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ('EE101', 'EE101'),
        ('EE102', 'EE102'),
        ("EE203", "EE203"),
        ("EE204", 'EE204'),
        ('EE205', 'EE205'),
        ("EE206", "EE206"),
        ("EE207", 'EE207'),
        ("EE210", 'EE210'),
        ('EE211', 'EE211'),
        ('EE220', 'EE220'),
        ('EE230', 'EE230'),
        ('EE250', 'EE250'),
        ('EE252', 'EE252'),
        ('EE253', 'EE253'),
        ("EE312", "EE312"),
        ("EE313", 'EE313'),
        ("EE321", 'EE321'),
        ("EE331", 'EE331'),
        ('EE332', 'EE332'),
        ('EE333', 'EE333'),
        ('EE334', 'EE334'),
        ('EE340', 'EE340'),
        ('EE351', 'EE351'),
        ('EE360', 'EE360'),
        ('EE370', 'EE370'),
        ('EE371', 'EE371'),
        ('EE380', 'EE380'),
        ('EE381', 'EE381'),
        ('EE390', 'EE390'),
        ('EE396', 'EE396'),
        ('EE398', 'EE398'),
        ('EE399', 'EE399'),
        ('EE3xx', 'EE3xx'),
        ('EE498', 'EE498'),
        ('EE499', 'EE499'),
        ('EExxx', 'EExxx'),
        ('EE4xx', 'EE4xx'),

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class MA(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )

    COURSENAME = (
        ("0", "Select"),
        ('MA101', 'MA101'),
        ('MA102', 'MA102'),
        ("MA201", "MA201"),
        ("MA221", 'MA221'),
        ("MA222", "MA222"),
        ("MA224", 'MA224'),
        ("MA225", 'MA225'),
        ('MA251', 'MA251'),
        ('MA252', 'MA252'),
        ('MA250', 'MA250'),
        ('MA252', 'MA252'),
        ('MA271', 'MA271'),
        ("MA321", "MA321"),
        ("MA322", 'MA322'),
        ("MA323", 'MA323'),
        ("MA324", 'MA324'),
        ('MA351', 'MA351'),
        ('MA372', 'MA372'),
        ('MA373', 'MA373'),
        ('MA374', 'MA374'),
        ('MA3xx', 'MA3xx'),
        ('MA423', 'MA423'),
        ('MA473', 'MA473'),
        ('MA498', 'MA498'),
        ('MA499', 'MA499'),
        ('MAxxx', 'MAxxx'),
        ('MA4xx', 'MA4xx'),

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class ME(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ('ME101', 'ME100'),
        ('ME110', 'ME110'),
        ("ME211", "ME211"),
        ("ME212", 'ME212'),
        ("ME213", "ME213"),
        ("ME214", 'ME214'),
        ("ME215", 'ME215'),
        ('ME216', 'ME216'),
        ("ME221", "ME221"),
        ("ME222", 'ME222'),
        ("ME223", "ME223"),
        ("ME224", 'ME224'),
        ("ME225", 'ME225'),
        ('ME226', 'ME226'),
        ('ME311', 'ME311'),
        ("ME312", "ME312"),
        ("ME313", 'ME313'),
        ("ME314", 'ME314'),
        ("ME315", 'ME315'),
        ("ME321", 'ME321'),
        ("ME322", 'ME322'),
        ("ME323", 'ME323'),
        ("ME324", 'ME324'),
        ("ME325", 'ME325'),
        ("ME326", 'ME326'),
        ('ME398', 'ME398'),
        ('ME399', 'ME399'),
        ('ME3xx', 'ME3xx'),
        ('ME401', 'ME401'),
        ('ME498', 'ME498'),
        ('ME499', 'ME499'),
        ('MExxx', 'MExxx'),
        ('ME4xx', 'ME4xx'),

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class PH(models.Model):
    CAT_CHOICE = (
        ("0", "Branch Related Activity"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("Assignments", "Assignments"),
        ("Quizzes", "Quizzes"),
        ("Exam", "Exam"),
        ("Viva", "Viva"),
        ("Lab Report", "Lab Report"),

    )


    COURSENAME = (
        ("0", "Select"),
        ('PH101', 'PH101'),
        ('PH102', 'PH102'),
        ('PH110', 'PH110'),
        ("PH201", "PH201"),
        ('PH202', 'PH202'),
        ('PH203', 'PH201'),
        ("PH203", 'PH203'),
        ("PH204", "PH204"),
        ("PH205", 'PH205'),
        ('PH206', 'PH206'),
        ("PH207", 'PH207'),
        ('PH208', 'PH208'),
        ('PH209', 'PH209'),
        ('PH210', 'PH210'),
        ('PH211', 'PH211'),
        ("PH301", "PH301"),
        ('PH302', 'PH302'),
        ('PH303', 'PH301'),
        ("PH303", 'PH303'),
        ("PH304", "PH304"),
        ("PH305", 'PH305'),
        ('PH306', 'PH306'),
        ("PH307", 'PH307'),
        ('PH308', 'PH308'),
        ('PH309', 'PH309'),
        ('PH310', 'PH310'),
        ('PH312', 'PH312'),
        ('PH411', 'PH411'),
        ('PH413', 'PH413'),
        ('PH415', 'PH415'),
        ('PH421', 'PH421'),
        ('PH422', 'PH422'),
        ('PHxxx', 'PHxxx'),
        ('PH4xx', 'PH4xx'),

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="Academic Activities")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    course_name = models.CharField(max_length=100, choices=COURSENAME, default='0')
    instructor_name = models.CharField(max_length=100, null=True)
    Credit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    Marks_Of_Task = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class SWC(models.Model):
    CAT_CHOICE = (
        ("0", "OCCASIONAL ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),
        ("PROJECTS","PROJECTS"),

    )


    CLUB_CHOICE = (
        ("0", "Students Web Committee"),
        #

    )



    title = models.CharField(max_length=20)
    description = models.TextField()
    ORGANISATION=models.CharField(max_length=40,choices=CLUB_CHOICE,default='0')
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CODINGCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )


    CLUB_CHOICE = (
        ("0", "CODING CLUB"),
        #

    )


    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class AEROCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )



    CLUB_CHOICE = (
        ("0", "AERO-MODELLING CLUB"),
        #

    )


    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class ASTROCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )


    CLUB_CHOICE = (
        ("0", "Astronomy CLUB"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club=models.CharField(max_length=40,choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CACLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )


    CLUB_CHOICE = (
        ("0", "Consulting and Analytics Club"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club=models.CharField(max_length=40,choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class EECLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )


    CLUB_CHOICE = (
        ("0", "Electronics Club"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club=models.CharField(max_length=40,choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.now())
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class PRAKRITICLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "Prakriti Club"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class FNCCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "Finance and Economics club"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class ROBOTICSCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "Robotics Club"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class EDCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "CLUB RELATED ACTIVITIES"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "Entrepreneurial Development Cell"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class UGCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Organisation Related Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "Udgam - IITG Entrepreneurship Summit"),
        #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class ALCHERCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Organisation Related Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "Alcheringa"),
        # #

    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class TechnicheCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Organisation Related Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("MEETINGS", "MEETINGS"),
        ("PARTIES", "PARTIES"),
        ("TUTORIALS", "TUTORIALS"),
        ("SHOWCASES", "SHOWCASES"),

    )

    CLUB_CHOICE = (
        ("0", "TECHNICHE"),


    )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class OTHERCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Other Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("INTERNSHIP", "INTERNSHIP"),
        ("PLACEMENT", "PLACEMENT"),
        ("HACKATHONS", "HACKATHONS"),
        ("SCHOLARSHIP PROGRAMS", "SCHOLARSHIP PROGRAMS"),
        ("TALK BY VISITING PROFESSORS",'TALK BY VISITING PROFESSORS'),
        ('TAKING MINOR','TAKING MINOR'),
        ('DROPPING MINOR','DROPPING MINOR'),
        ('COURSE FEEDBACK','COURSE FEEDBACK'),
        ('FEE PAYMENT','FEE PAYMENT'),
        ('FILLING ELECTIVES','FILLING ELECTIVES'),

    )

    # CLUB_CHOICE = (
    #     ("0", "Other "),
    #
    #
    # )  # CLUB_CHOICE = (
    #     ("0", "Other "),
    #
    #
    # )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    # club = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class SAILCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Organisation Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("INTERNSHIP", "INTERNSHIP"),
        ("PLACEMENT", "PLACEMENT"),
        ("HACKATHONS", "HACKATHONS"),
        ('PROJECTS','PROJECTS'),
        ('TALKS','TALKS'),
        ('OTHER','OTHER'),

    )

    CLUB_CHOICE = (
        ("0", "SAIL "),
    )
    #
    #
    # )  # CLUB_CHOICE = (
    #     ("0", "Other "),
    #
    #
    # )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    ORGANISATION = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class AICLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Organisation Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("INTERNSHIP", "INTERNSHIP"),
        ("PLACEMENT", "PLACEMENT"),
        ("HACKATHONS", "HACKATHONS"),
        ('PROJECTS','PROJECTS'),
        ('TALKS','TALKS'),
        ('OTHER','OTHER'),

    )

    CLUB_CHOICE = (
        ("0", "IITG.AI "),
    )
    #
    #
    # )  # CLUB_CHOICE = (
    #     ("0", "Other "),
    #
    #
    # )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    ORGANISATION = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})


class CCDCLUB(models.Model):
    CAT_CHOICE = (
        ("0", "Organisation Activities"),

    )
    EVENT_TYPE = (
        ("0", "Select"),
        ("INTERNSHIP", "INTERNSHIP"),
        ("PLACEMENT", "PLACEMENT"),
        ("HACKATHONS", "HACKATHONS"),
        ('PROJECTS','PROJECTS'),
        ('TALKS','TALKS'),
        ('OTHER','OTHER'),

    )

    CLUB_CHOICE = (
        ("0", "CCD "),
    )
    #
    #
    # )  # CLUB_CHOICE = (
    #     ("0", "Other "),
    #
    #
    # )

    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40, choices=CAT_CHOICE, default="0")
    sub_event = models.CharField(max_length=40, choices=EVENT_TYPE, default="0")
    ORGANISATION = models.CharField(max_length=40, choices=CLUB_CHOICE, default='0')
    target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()))
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})