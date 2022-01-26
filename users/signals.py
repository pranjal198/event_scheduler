# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile
# from users import models as user_model
# from tasks import models as task_model


# @receiver(post_save,sender = User)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         w = instance.first_name
#         x = instance.last_name
#         u = x[2:4]
#         y = x[0:4]
#         z = x[4:6]
#         DEP_CHOICE ={
#             1:"Computer Science and Engineering",
#             2:"Electronics and Communications Engineering",
#             3:"Mechanical Engineering",
#             4:"Civil Engineering",
#             5:"Design",
#             6:"Biosciences and Bioengineering",
#             7:"Chemical Engineering",
#             8:"Electronics and Electrical Engineering",
#             21:"Engineering Physics",
#             22:"Chemimal Science and Technology",
#             23:"Mathematics and Computing",
#             25:"Humanities and Social Sciences",
#         }
#         BAT_CHOICE = {
#             2001: "B.Tech 20",
#             1901: "B.Tech 19",
#             1801: "B.Tech 18",
#             1701: "B.Tech 17",
#             1601: "B.Tech 16",
#             2002: "B.Des 20",
#             1902: "B.Des 19",
#             1802: "B.Des 18",
#             1702: "B.Des 17",
#             1602: "B.Des 16",
#             2041: "M.Tech 20",
#             1941: "M.Tech 19",
#             1841: "M.Tech 18",
#             1741: "M.Tech 17",
#             1641: "M.Tech 16",
#             2061: "PhD 20",
#             1961: "PhD 19",
#             1861: "PhD 18",
#             1761: "PhD 17",
#             1661: "PhD 16",
#         }
#         PRG_CHOICE = {
#             1: "B.Tech",
#             2: "B.Des",
#             41: "M.Tech",
#             61: "PhD",
#         }
#         Profile.objects.create(user = instance,name = str(w),roll = str(x),batch = BAT_CHOICE[int(y)],programme = PRG_CHOICE[int(u)],department = DEP_CHOICE[int(z)])


# @receiver(post_save,sender = User)
# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()

# # @receiver(post_save,sender = task_model.AEROCLUB)
# # def create_rsvp_AEROCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_AEROCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.AICLUB)
# # def create_rsvp_AICLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_AICLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.Task)
# # def create_rsvp_Task(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_Task.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.BT)
# # def create_rsvp_BT(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_BT.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CH)
# # def create_rsvp_CH(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CH.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CL)
# # def create_rsvp_CL(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CL.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CE)
# # def create_rsvp_CE(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CE.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CSE)
# # def create_rsvp_CSE(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CSE.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.DES)
# # def create_rsvp_DES(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_DES.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.ECE)
# # def create_rsvp_ECE(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_ECE.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.EEE)
# # def create_rsvp_EEE(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_EEE.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.MA)
# # def create_rsvp_MA(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_MA.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.ME)
# # def create_rsvp_ME(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_ME.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.PH)
# # def create_rsvp_PH(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_PH.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.SWC)
# # def create_rsvp_SWC(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_SWC.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CODINGCLUB)
# # def create_rsvp_CODINGCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CODINGCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.ASTROCLUB)
# # def create_rsvp_ASTROCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_ASTROCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CACLUB)
# # def create_rsvp_CACLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CACLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.EECLUB)
# # def create_rsvp_EECLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_EECLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.PRAKRITICLUB)
# # def create_rsvp_PRAKRITICLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_PRAKRITICLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.FNCCLUB)
# # def create_rsvp_FNCCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_FNCCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.ROBOTICSCLUB)
# # def create_rsvp_ROBOTICSCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_ROBOTICSCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.EDCLUB)
# # def create_rsvp_EDCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_EDCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.UGCLUB)
# # def create_rsvp_UGCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_UGCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.ALCHERCLUB)
# # def create_rsvp_ALCHERCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_ALCHERCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.TechnicheCLUB)
# # def create_rsvp_TechnicheCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_TechnicheCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.OTHERCLUB)
# # def create_rsvp_OTHERCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_OTHERCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.SAILCLUB)
# # def create_rsvp_SAILCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_SAILCLUB.objects.create(event = instance)

# # @receiver(post_save,sender = task_model.CCDCLUB)
# # def create_rsvp_CCDCLUB(sender,instance,created,**kwargs):
# #     if created:
# #         user_model.Rsvp_CCDCLUB.objects.create(event = instance)

