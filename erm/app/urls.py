from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.login_user),
    path('logoutuser',views.logout_user),
    path('index',views.index),
    path('hrprofile',views.hr_profile),
    
    path('empregister',views.emp_register),
    path('empindex',views.employee_index,name='empindex'),
    path('empprofile',views.empprofile),
    path('empprofileedit/<int:id>',views.empprofile_edit,name='empprofileedit'),  
    path('empprofileupdate/<int:id>',views.empprofile_update,name='empprofileupdate'),
    path('eempleaveview/<int:id>',views.eempleave_view,name='eempleaveview'),





    #admin module
    path('adminregister',views.admin_register),
    path('adminindex',views.admin_index),
    path('adepreg',views.adep_reg),
    path('adepview',views.adep_view),
    path('aposreg',views.apos_reg),
    path('aposview',views.apos_view),
    path('adepheadreg',views.adepheadreg),
    path('adepheadview',views.adepheadview),
    path('aempreg',views.aemp_reg),
    path('aempview',views.aemp_view),
    path('aempedit/<int:id>',views.aemp_edit,name='aempedit'),
    path('aempdelete/<int:id>',views.aemp_delete,name='aempdelete'),
    path('aempupdate/<int:id>',views.aemp_update,name='aempupdate'),
    path('aempindview/<int:id>',views.aempindview,name='aempindview'),
    path('aleavetypereg',views.aleavetype_reg),
    path('aleavetypedelete/<int:id>',views.aleavetype_delete,name='aleavetypedelete'),
    path('aclientreg',views.aclient_reg),
    path('aclientview',views.aclient_view),
    path('aclientcomreg',views.aclientcom_reg),
    path('aclientcomview',views.aclientcom_view),
    path('aprojectreg',views.aproject_reg),
    path('aprojectview',views.aproject_view),
    path('aprojectdelete/<int:id>',views.aproject_delete,name='aprojectdelete'),
    path('aprojectindview/<int:id>',views.aprojectindview,name='aprojectindview'),
    path('acoursereg',views.acourse_reg),
    path('acourseview',views.acourse_view),
    path('atrainingreg',views.atraining_reg),
    path('atrainingview',views.atraining_view),
    path('aadmleaveview',views.aadmleave_view),




    # department
    path('depreg',views.dep_reg),
    path('depview',views.dep_view),
    path('depedit/<int:id>',views.dep_edit,name='depedit'),
    path('depdelete/<int:id>',views.dep_delete,name='depdelete'),
    path('depupdate/<int:id>',views.dep_update,name='depupdate'),
    # position
    path('posreg',views.pos_reg),
    path('posview',views.pos_view),
    path('posedit/<int:id>',views.pos_edit,name='posedit'),
    path('posdelete/<int:id>',views.pos_delete,name='posdelete'),
    path('posupdate/<int:id>',views.pos_update,name='posupdate'),
    # employee
    path('empreg',views.emp_reg),
    path('empview',views.emp_view),
    path('empsalaryview',views.empsalary_view),
    path('empedit/<int:id>',views.emp_edit,name='empedit'),
    path('empdelete/<int:id>',views.emp_delete,name='empdelete'),
    path('empupdate/<int:id>',views.emp_update,name='empupdate'),
    path('empindview/<int:id>',views.empindview,name='empindview'),



    # admin
    path('admreg',views.adm_reg),
    path('admview',views.adm_view),
    path('admsalaryview',views.admsalary_view),
    path('admedit/<int:id>',views.adm_edit,name='admedit'),
    path('admdelete/<int:id>',views.adm_delete,name='admdelete'),
    path('admupdate/<int:id>',views.adm_update,name='admupdate'),
    path('admindview/<int:id>',views.admindview,name='admindview'),

    #Department Heads
    path('depheadreg',views.depheadreg),
    path('depheadview',views.depheadview),
    path('depheadedit/<int:id>',views.depheadedit,name='depheadedit'),
    path('depheaddelete/<int:id>',views.depheaddelete,name='depheaddelete'),
    path('depheadupdate/<int:id>',views.depheadupdate,name='depheadupdate'),
    path('depheadindview/<int:id>',views.depheadindview,name='depheadindview'),

    #Leave Type
    path('leavetypereg',views.leavetype_reg),
    path('leavetypedelete/<int:id>',views.leavetype_delete,name='leavetypedelete'),

    path('adempleaveview',views.adempleave_view),


    path('empleavereg',views.empleave_reg),
    path('empleaveview',views.empleave_view),
    path('empleavedelete/<int:id>',views.empleave_delete,name='empleavedelete'),
    path('empleaveedit/<int:id>',views.empleave_edit,name='empleaveedit'),  
    path('empleaveupdate/<int:id>',views.empleave_update,name='empleaveupdate'),

    path('admleavereg',views.admleave_reg),
    path('admleaveview',views.admleave_view),
    path('admleavedelete/<int:id>',views.admleave_delete,name='admleavedelete'),
    path('admleaveedit/<int:id>',views.admleave_edit,name='admleaveedit'),  
    path('admleaveupdate/<int:id>',views.admleave_update,name='admleaveupdate'),

    #Clients
    path('clientreg',views.client_reg),
    path('clientview',views.client_view),
    path('clientdelete/<int:id>',views.client_delete,name='clientdelete'),

    path('clientcomreg',views.clientcom_reg),
    path('clientcomview',views.clientcom_view),
    path('clientcomdelete/<int:id>',views.clientcom_delete,name='clientcomdelete'),

    ##Projects
    path('projectreg',views.project_reg),
    path('projectview',views.project_view),
    path('projectdelete/<int:id>',views.project_delete,name='projectdelete'),
    path('projectindview/<int:id>',views.projectindview,name='projectindview'),

    #CourseType
    path('coursereg',views.course_reg),
    path('courseview',views.course_view),
    path('courseedit/<int:id>',views.course_edit,name='courseedit'),
    path('coursedelete/<int:id>',views.course_delete,name='coursedelete'),
    path('courseupdate/<int:id>',views.course_update,name='courseupdate'),

    #Training
    path('trainingreg',views.training_reg),
    path('trainingview',views.training_view),
    path('trainingedit/<int:id>',views.training_edit,name='trainingedit'),
    path('trainingdelete/<int:id>',views.training_delete,name='trainingdelete'),
    path('trainingupdate/<int:id>',views.training_update,name='trainingupdate'),

    #Notifications
    path('notreg',views.not_reg),
    path('notview',views.not_view),
    path('notdelete/<int:id>',views.not_delete,name='notdelete'),

    path('empnotreg',views.empnot_reg),
    path('empnotview',views.empnot_view),
    path('empnotdelete/<int:id>',views.empnot_delete,name='empnotdelete'),

    path('hrnotreg',views.hrnot_reg),
    path('hrnotview',views.hrnot_view),
    path('hrnotdelete/<int:id>',views.hrnot_delete,name='hrnotdelete'),



]