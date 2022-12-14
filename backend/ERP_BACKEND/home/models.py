from tkinter import N
from ERP_BACKEND.settings import POPPLER_PATH
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
import uuid
import os
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
# import base64
from PIL import Image
from pdf2image import convert_from_path
from django.db.models.signals import post_save
from django.dispatch import receiver
# Models
def changeImgName(instance, filename):
    try:
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return filename
    except:
        pass

def changePerfilName(instance, filename):
    try:
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return  f'perfil/{filename}'
    except:
        pass

class Plant(models.Model):
    plant = models.CharField(max_length=25,verbose_name=("Plant") , help_text='Insert the current plant' , blank=False, null=False)
    plantAbrv = models.CharField(max_length=10, verbose_name=("Plant Abbreviation") , help_text='Insert the abbreviation of the plant', blank=False, null=False)

    def __str__(self) -> str:
        return self.plant

class Area(models.Model):
    area = models.CharField(max_length=40,verbose_name=("Area") , help_text='Insert the current area' , blank=False, null=False)
    areaAbrv = models.CharField(max_length=10, verbose_name=("Area Abbreviation"), help_text='Insert the abbreviation of the area', blank=False, null=False)
    

    def __str__(self) -> str:
        return self.area

class Team(models.Model):
    name = models.CharField(max_length=50,verbose_name=("Name"), help_text='Insert the Team name', blank=False, null=False)
    qttMates = models.IntegerField(default = 0,verbose_name=("Quantity of Mates"), help_text='Insert the quantity of members', blank=True, null=True)
    fk_area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True, verbose_name=("Area"), help_text='Insert the Area')
    fk_plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name=("Plant"), help_text='Select the plant', blank=True, null=True)
    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    localName = models.CharField(max_length=80, blank=False, null=False, default='')
    businessPoint = models.CharField(max_length=30, blank=False, null=True, default='')

    def __str__(self) -> str:
        return self.localName


class Event(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, default='')
    event_responsible = models.CharField(max_length=100, null=True, blank=True, default='')
    description = models.CharField(max_length=100, null=True, blank=True, default='')
    date = models.DateField(blank=False, null=False, auto_now_add=False, default='')
    startTime = models.TimeField(blank=False, null=False, auto_now_add=False, default='')
    endTime = models.TimeField(blank=False, null=False, auto_now_add=False, default='')
    location = models.ForeignKey(Location, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    # location

class TeamEvent(models.Model):
    fk_team = models.ForeignKey(Team, blank= False, null=False, on_delete=models.CASCADE, default='')
    fk_event = models.ForeignKey(Event, blank=False, null=False, on_delete=models.CASCADE, default='')

    

class ProfileService(models.Model):
    profile = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self) -> str:
        return self.profile
    
class AccessLevel(models.Model):
            
    level = models.IntegerField(blank=False, null=False, default=1,choices=((1,1),(2,2),(3,3)))
    name = models.CharField(max_length=20, )
    profiles = models.ManyToManyField('ProfileService',)
    def __str__(self) -> str:
        return self.name




class SimpleUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=False, null=False, default='', help_text='Insert The User Name', verbose_name='Name:' )
    last_name = models.CharField(max_length=40, blank=False, null=False, default='', help_text='Insert The User Last Name', verbose_name='Last Name:' )
    username = models.CharField(max_length=8,blank=False, null=False, help_text='Insert The Colaborator USERID', verbose_name='Intern User',unique=True)
    email = models.EmailField(max_length=80, help_text='Insert The Colaborator Email', default='', verbose_name='Email', blank=False, null=False)
    currentLevel = models.ForeignKey(AccessLevel, default='', blank=True, null=True, help_text='Insert The Colaborator Access Level', verbose_name='Access Level', on_delete=models.CASCADE)
    edv = models.CharField(max_length=12,default='', help_text='Insert The Colaborator EDV', verbose_name='EDV')
    password = models.CharField(max_length=500, blank=False, null=False, help_text='Insert you password', verbose_name='Password', default="")
    birthDate = models.DateField(blank=True, null=True, auto_now_add=True, help_text='Insert The Colaborator Birth Date', verbose_name='Birth Date' )
    #fk_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, help_text='Insert The Colaborator Team', verbose_name='Team',)
    user_img = models.ImageField(upload_to='users/', blank=True, null=True, default='users/default_user.png')
    fk_team = models.ManyToManyField('Team', null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        else: pass
        #  pbkdf2_sha256
        
        super(SimpleUser, self).save(*args, **kwargs)
        dados = SimpleUser.objects.get(id=self.id)

        # for team in dados.fk_team.all():
        #     counter = SimpleUser.objects.filter(fk_team = team.id)
        #     realTeam = Team.objects.get(id=team.id)
        #     realTeam.qttMates = len(counter)
        #     print(len(counter))
        #     realTeam.save()

        # if self._state.adding:
        #     dados = SimpleUser.objects.get(id=self.id)
        #     for team in dados.fk_team.all():
        #         print(team)
        #         team.qttMates = team.qttMates + 1
        #         team.save()
  


    USERNAME_FIELD = 'username'
    objects = UserManager()
    REQUIRED_FIELDS = ['email']

    

    


# class Colab_Team(models.Model):
#     fk_colab = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, blank=False, null=False, default='')
#     fk_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False)
    
#     def __str__(self) -> str:
#         return str(self.id)
    
class SuperUser:
    pass

class System(models.Model):
    name = models.CharField(max_length=100, default="", blank=True, null=True, help_text="Selected System Name", verbose_name="Selected System Name")
    description = models.CharField(max_length=500, default="", null=True, blank=True)
    router_to = models.CharField(max_length=500, default="", null=True, blank=True)
    icon = models.CharField(max_length=50, default="", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

class SSMType(models.Model):
    type = models.CharField(max_length=100, null=False, blank=False, default="", help_text='Insert SSM Type name', verbose_name="Type")
    def __str__(self) -> str:
        return self.type

class SSM(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default="", help_text='Insert The Title',verbose_name='Title' )
    file = models.FileField(upload_to="ssm/pdfs/")
    miniImg = models.ImageField(upload_to="ssm/imgs/", default="", blank=True, null=True, help_text='Insert Front Image', verbose_name='Front Image')
    fk_type = models.ForeignKey(SSMType, on_delete=models.CASCADE, blank=False, null=False, default="")
    #miniImg = models.TextField(default="", null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.title)
     
        
    def save(self, *args, **kwargs):
        super(SSM, self).save(*args, **kwargs)
        images = convert_from_path(self.file.path, poppler_path=POPPLER_PATH)
        
        for i in range(len(images)):
            # Save pages as images in the pdf
            file_name = str(uuid.uuid4()) +'.jpg'
            images[i].save('media/ssm/imgs/'+ file_name, 'JPEG')
            basewidth = 480
            img = Image.open('media/ssm/imgs/'+ file_name)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save('media/ssm/imgs/'+ file_name)
            self.miniImg = 'ssm/imgs/'+ file_name;
            super(SSM, self).save(*args, **kwargs)




        

class DDS(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default="", help_text='Insert The Title',verbose_name='Title' )
    frontImg = models.ImageField(upload_to=changeImgName, default="", blank=True, null=True, help_text='Insert Front Image', verbose_name='Front Image')
    frontText = models.CharField(max_length=1000,default="", blank=True, null=True, help_text='Insert Front Text', verbose_name='Front Text' )
    backImg = models.ImageField(upload_to=changeImgName, default="", blank=True, null=True, help_text='Insert Front Image', verbose_name='Front Image')
    backText = models.CharField(max_length=1000,default="", blank=True, null=True, help_text='Insert Back Text', verbose_name='Back Text' )
    read = models.BooleanField(default=False, blank=True)
    readDate = models.DateField(default=None, null=True, blank=True)
    #fk_type = models.ForeignKey(SSMType, on_delete=models.CASCADE, blank=True, null=True, default="")
    
    def __str__(self) -> str:
        return str(self.title)
    
    # def save(self, *args, **kwargs):
    #     import base64
    #     with open(self.frontImg, "rb") as pdf_file:
    #         encoded_string = base64.b64encode(pdf_file.read())
    #         self.frontImg = encoded_string
    

# class SSMRandomOrder(models.Model):
#     date = models.DateTimeField(blank=True, null=True, help_text='Date do present the DDS card')
#     fk_ssm = models.ForeignKey(SSM, on_delete=models.CASCADE, blank=True, null=True, default='')
#     readDate = models.DateTimeField(null=True, blank=True, help_text='Last date and time when card was read', verbose_name='Read date2')

class PatrolQuest(models.Model):
    question = models.CharField(max_length=1000,default="", blank=False, null=False, help_text='Insert The Patrol Question', verbose_name='Question' )

    def __str__(self) -> str:
        return str(self.question)

import datetime
class PatrolWeek(models.Model):

    def allQuests():
        return PatrolQuest.objects.all()

    initialDate = models.DateField(blank=False, null=False, auto_now_add=False, help_text='Insert The Initial Patrol Date', verbose_name='Initial Date' )
    fk_patrol = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, blank=False, null=False)
    fk_days = models.ManyToManyField('PatrolDay', null=True, blank=True)
    fk_quests = models.ManyToManyField('PatrolQuest', null=False, blank=False, default=allQuests)
    status = models.BooleanField(default=True)
    answerGenerated = models.BooleanField(default=False)

    

    def __str__(self) -> str:
        return f'{self.id}_{self.initialDate}-{self.fk_patrol}'

    def save(self, *args, **kwargs):
        super(PatrolWeek, self).save(*args, **kwargs)

        # PatrolWeekDATA = PatrolWeek.objects.get(id=self.id)
        # #fk_patrol
        # print(PatrolWeekDATA.fk_patrol.id)


        # if not PatrolWeekDATA.answerGenerated:
        #     for day in range(0,7):
        #         cDay = PatrolDay()
        #         cDay.cDate = PatrolWeekDATA.initialDate + datetime.timedelta(days=day)
        #         cDay.save()
        #         for quests in PatrolWeekDATA.fk_quests.all():
        #             newAnswer = PatrolAnswer()
        #             newAnswer.fk_patrolquest = quests
        #             newAnswer.fk_patrolweek = PatrolWeekDATA
        #             newAnswer.save()
        #             item = PatrolAnswer.objects.get(id=newAnswer.id)
        #             cDay.fk_answers.add(item)

        #         cDay.save()
        #         PatrolWeekDATA.fk_days.add(cDay)
        #         PatrolWeekDATA.answerGenerated = True
        #         PatrolWeekDATA.save()

            
        # incomeData = self.fk_quests.all()
        # print(incomeData)
        # for quest in incomeData:
        #     print(quest)


class PatrolDay(models.Model):
    cDate = models.DateField(blank=False, null=False, auto_now_add=False, help_text='Insert The Initial Patrol Date', verbose_name='Initial Date' )
    fk_answers = models.ManyToManyField('PatrolAnswer', null=True, blank=True)

    def __str__(self) -> str:
        return str(self.cDate)
    
           

class PatrolAnswer(models.Model):
    answerDay = models.DateField(null=True, blank=True, help_text="Insert The Date", auto_now_add=False, verbose_name="Date")
    answerBool = models.BooleanField(null=True)
    answer = models.CharField(max_length=500,null=True, blank=True, help_text="Insert The Possible Answer", verbose_name="Answer")  
    fk_patrolquest =  models.ForeignKey(PatrolQuest, on_delete=models.CASCADE, blank=False, null=False, help_text="Insert The Patrol Quest",  verbose_name="Quest")
    fk_patrolweek = models.ForeignKey(PatrolWeek, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.fk_patrolweek)



# class GeneratedAnswerFields(models.Model):
#     patrol_week_id = models.ForeignKey(PatrolWeek, null=False, blank=False, on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):
#         pass
#         # print(self.patrol_week_id)
        
#         # id = str(self.patrol_week_id).split('_', 1)[0]
#         # print(2)
#         # PatrolWeekDATA = PatrolWeek.objects.get(id=id)
#         # for quests in PatrolWeekDATA.fk_quests.all():
#         #     data = PatrolAnswer()
#         #     data.fk_patrolquest = quests
#         #     data.fk_patrolweek = PatrolWeekDATA
#         #     data.save()



# import requests
# # @receiver(post_save, sender=PatrolWeek)
# def setAnswerFields(sender, **kwargs):    
#     # print(PatrolWeek.objects.get(id=kwargs['instance'].id))
#     # time.sleep(1)
#     print(1)
#     r = requests.get(f"http://localhost:8000/apiv1/patrolweek/{kwargs['instance'].id }")
#     for d in r:
#         print(d)
#     if kwargs['created']:
#         pass
        
        
#         # for d in PatrolWeek.objects.get(id=kwargs['instance'].id).fk_quests.all():
#         #     print(1)


# post_save.connect(setAnswerFields, sender=PatrolWeek)
        



########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
# #change
# class ProjCat(models.Model):
#     type = models.CharField(max_length=60)

#     class Meta:
#         verbose_name_plural = "projects' categories"
#         verbose_name = "project's category"

#     def __str__(self):
#         return self.type

# ########################################################################################################################################################################
# ########################################################################################################################################################################
# ########################################################################################################################################################################
# ########################################################################################################################################################################





# class Project(models.Model):
#     name = models.CharField(max_length=100, help_text="Insert The Project Name", verbose_name="Project Name")
#     description = models.CharField(max_length=300, blank=True, null=True,default="", help_text="Insert The Project Descripition", verbose_name="Description" )
#     percentage = models.FloatField(blank=True, null=True, help_text="Insert The Percentage", verbose_name="Percentage")
#     fk_owner = models.ForeignKey(SimpleUser, on_delete=models.CASCADE, blank=False, null=False, help_text="Insert The Owner", verbose_name="Owner")
#     fk_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True,default="", help_text="Insert The Team", verbose_name="Team")
#     fk_category = models.ForeignKey(ProjCat, on_delete=models.CASCADE, blank=True, null=True, default='')

#     def __str__(self) -> str:
#         return self.name
# class LocationSchedule(models.Model):
#     description = models.CharField(max_length=200,null=False, blank=False, help_text="Insert The Location Description For Schedule Event", verbose_name="Event Location Description")

#     def __str__(self) -> str:
#         return self.description

# class ScheduleEvent(models.Model):
#     title = models.CharField(max_length=100,null=False, blank=False, help_text="Insert The Title", verbose_name="Title")
#     date = models.DateField(null=False, blank=False, help_text="Insert The Date", verbose_name="Date")
#     initTime = models.TimeField(null=False, blank=False, help_text="Initial Time", verbose_name="Initial Time")
#     finalTIme = models.TimeField(null=False, blank=False, help_text="Final Time", verbose_name="Final Time")
#     description = models.CharField(max_length=400, blank=True, null=True, help_text="Insert The Description", verbose_name="Description")
#     fk_location = models.ForeignKey(LocationSchedule, on_delete=models.CASCADE, blank=False, null=False, default="", help_text="Insert The Location", verbose_name="Location")
#     fk_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, null=False, default="", help_text="Insert The Team", verbose_name="Team")
#     fk_system = models.ForeignKey(System, on_delete=models.CASCADE,  blank=False, null=False, default="", help_text="Insert The System", verbose_name="System" )

#     def __str__(self) -> str:
#         return self.title


# # Wiki Models

# class QuickAcess(models.Model):
#     title = models.CharField(max_length=10)
#     link = models.CharField(max_length=300)
#     img = models.ImageField(upload_to='media/qa', blank=True)

#     class Meta:
#         verbose_name_plural = "Quick Access"
#         verbose_name = "Quick Access"

#     def __str__(self):
#         return self.title 

# class Category(models.Model):
#     category = models.CharField(max_length=20)

#     class Meta:
#         verbose_name_plural = "categories"
#         verbose_name = "category"

#     def __str__(self):
#         return self.category

# class Links(models.Model):
#     title = models.CharField(max_length=20)
#     links = models.CharField(max_length=300)
#     fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "links"
#         verbose_name = "link"

#     def __str__(self):
#         return self.title


# class Extensions_Emails(models.Model):
#     title = models.CharField(max_length=20)
#     ramalNum = models.IntegerField()
#     mainEmail = models.EmailField()
#     secondaryEmail = models.EmailField(blank=True)
#     fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "contacts"
#         verbose_name = "contact"

#     def __str__(self):
#         return self.title


# class Bus(models.Model):
#     line = models.CharField(max_length=5)
#     region = models.CharField(max_length=300)
#     upload = models.FileField(upload_to='media/bus', blank=True)

#     # ADICIONAR NA CLASS BUS UM CAMPO PARA UPLOAD DE PDF
#     # CRIAR A CLASS EVENTS PARA O CALENDARIO CONFORME O CALENDARIO NECESSITAR

#     class Meta:
#         verbose_name_plural = "buses"
#         verbose_name = "bus"

#     def __str__(self):
#         return self.line


# class Note(models.Model):
#     setNote = models.CharField(max_length=30)

#     def __str__(self):
#         return self.setNote

#     class Meta:
#         verbose_name_plural = "notes"
#         verbose_name = "note"

# class Feedback(models.Model):
#     fk_note = models.ForeignKey(Note, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=500)
#     data = models.DateField(auto_now_add=True)


#     class Meta:
#         verbose_name_plural = "feedbacks"
#         verbose_name = "feedback"

#     def __str__(self):
#         return self.comment


# Related Auto Call methods 
@receiver(models.signals.post_delete, sender=DDS)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    try:
        if instance.frontImg:
            if os.path.isfile(instance.frontImg.path):
                os.remove(instance.frontImg.path)
    except:
        pass




   