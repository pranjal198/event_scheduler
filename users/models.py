from django.db import models
from django.contrib.auth.models import User  # 200101017
from tasks import models as task_model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    roll = models.CharField(max_length=9,default='0')
    batch = models.CharField(max_length=13,default='0')
    programme = models.CharField(max_length=13,default='0')
    department = models.CharField(max_length=50,default='0')

    def __str__(self):
        return f'{self.user.first_name} profile'
    
class Rsvp_Task(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='Taskyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='Taskmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='Taskno')
    event = models.OneToOneField(task_model.Task,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_BT(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='BTyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='BTmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='BTno')
    event = models.OneToOneField(task_model.BT,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CH(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CHyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CHmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CHno')
    event = models.OneToOneField(task_model.CH,on_delete=models.CASCADE)
       
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CL(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CLyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CLmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CLno')
    event = models.OneToOneField(task_model.CL,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CE(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CEyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CEmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CEno')
    event = models.OneToOneField(task_model.CE,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CSE(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CSEyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CSEmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CSEno')
    event = models.OneToOneField(task_model.CSE,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_DES(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='DESyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='DESmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='DESno')
    event = models.OneToOneField(task_model.DES,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_ECE(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='ECEyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='ECEmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='ECEno')
    event = models.OneToOneField(task_model.ECE,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_EEE(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='EEEyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='EEEmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='EEEno')
    event = models.OneToOneField(task_model.EEE,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_MA(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='MAyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='MAmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='MAno')
    event = models.OneToOneField(task_model.MA,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_ME(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='MEyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='MEmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='MEno')
    event = models.OneToOneField(task_model.ME,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_PH(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='PHyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='PHmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='PHno')
    event = models.OneToOneField(task_model.PH,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_SWC(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='SWCyes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='SWCmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='SWCno')
    event = models.OneToOneField(task_model.SWC,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CODINGCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CODINGCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CODINGCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CODINGCLUBno')
    event = models.OneToOneField(task_model.CODINGCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_AEROCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='AEROCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='AEROCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='AEROCLUBno')
    event = models.OneToOneField(task_model.AEROCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_ASTROCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='ASTROCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='ASTROCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='ASTROCLUBno')
    event = models.OneToOneField(task_model.ASTROCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CACLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CACLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CACLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CACLUBno')
    event = models.OneToOneField(task_model.CACLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_EECLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='EECLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='EECLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='EECLUBno')
    event = models.OneToOneField(task_model.EECLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_PRAKRITICLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='PRAKRITICLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='PRAKRITICLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='PRAKRITICLUBno')
    event = models.OneToOneField(task_model.PRAKRITICLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_FNCCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='FNCCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='FNCCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='FNCCLUBno')
    event = models.OneToOneField(task_model.FNCCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_ROBOTICSCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='ROBOTICSCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='ROBOTICSCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='ROBOTICSCLUBno')
    event = models.OneToOneField(task_model.ROBOTICSCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_EDCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='EDCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='EDCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='EDCLUBno')
    event = models.OneToOneField(task_model.EDCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_UGCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='UGCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='UGCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='UGCLUBno')
    event = models.OneToOneField(task_model.UGCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_ALCHERCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='ALCERCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='ALCERCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='ALCERCLUBno')
    event = models.OneToOneField(task_model.ALCHERCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_TechnicheCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='TechnicheCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='TechnicheCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='TechnicheCLUBno')
    event = models.OneToOneField(task_model.TechnicheCLUB,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_OTHERCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='OTHERCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='OTHERCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='OTHERCLUBno')
    event = models.OneToOneField(task_model.OTHERCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_SAILCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='SAILCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='SAILCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='SAILCLUBno')
    event = models.OneToOneField(task_model.SAILCLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_AICLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='AICLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='AICLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='AICLUBno')
    event = models.OneToOneField(task_model.AICLUB,on_delete=models.CASCADE)    
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()

class Rsvp_CCDCLUB(models.Model):
    yes = models.ManyToManyField(Profile,blank=True,related_name='CCDCLUByes')
    maybe = models.ManyToManyField(Profile,blank=True,related_name='CCDCLUBmaybe')
    no = models.ManyToManyField(Profile,blank=True,related_name='CCDCLUBno')
    event = models.OneToOneField(task_model.CCDCLUB,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.event.title}'

    def get_all_yes(self):
        return self.yes.all()
        
    def get_all_maybe(self):
        return self.maybe.all()

    def get_all_yes(self):
        return self.no.all()

    def get_all_yes_count(self):
        return self.yes.all().count()

    def get_all_maybe_count(self):
        return self.maybe.all().count()

    def get_all_no_count(self):
        return self.no.all().count()
