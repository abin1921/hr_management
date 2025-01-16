from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.models import Department,Position,DepartmentHead,LeaveType,EmployeeLeave,AdminLeave,Clients,ClientCompany,TrainingType,Training,Projects,CustomUser,Notififaction,HrNotififaction,EmpNotififaction
# Create your views here.

def login_user(request):
    if request.method=="POST":
        un=request.POST["username"]
        pa=request.POST["password"]
        u=authenticate(request,password=pa,username=un)
        if u is not None:
            if u.is_superuser==1:
                request.session['sid']=u.id
                login(request,u)
                return redirect(index)
            elif u.is_superuser==0 and u.usertype=="hr":
                request.session['sid']=u.id
                login(request,u)
                return redirect(admin_index)
            elif u.is_superuser==0 and u.usertype=="employee":
                request.session['sid']=u.id
                e=request.session['sid']
                login(request,u)
                return redirect(employee_index)
            else:
                messages.success(request,("There was an error required!"))
                return redirect(login_user)
        else:
            messages.success(request,("Incorrect Username or Password!"))
            return redirect(login_user)
    else:
        return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect(login_user)

#Emp Register
def emp_register(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        us=request.POST['usertype']
        t=CustomUser.objects.create_user(username=u,password=p,usertype=us)
        t.save()
    return render(request,'emp_module/emp_register.html')

@login_required
def employee_index(request):
 
    st=CustomUser.objects.filter(usertype="employee")
    context = {
        'data' : st,
    
    }
    return render(request, 'emp_module/emp_index.html',context)

@login_required
def empprofile(request):
    st=CustomUser.objects.all()
    return render(request,'emp_module/emp_profile.html',{'data':st})

@login_required
def empprofile_edit(request,id):
    st=CustomUser.objects.get(id=id)
    u=Position.objects.all()
    context = {
        'data' :st,
        'positions' : u}
    return render(request,'emp_module/empprofile_edit.html',context)


@login_required
def empprofile_update(request,id):
    st=CustomUser.objects.get(id=id)
    if request.method=="POST":
        st.firstname=request.POST['fname']
        st.lastname=request.POST['lname']
        st.gender=request.POST['gender']
        st.dob=request.POST['dob']
        st.contact=request.POST['contact']
        st.address=request.POST['address']
        st.email=request.POST['email']
        st.save()
        return redirect(empprofile)
    else:
        st=CustomUser.objects.get(id=id)
        u=Position.objects.all()
        context = {
            'data' :st,
            'positions' : u}
    return render(request, 'emp_module/emp_profile.html',context)

@login_required
def eempleave_view(request,id):
    st=EmployeeLeave.objects.get(id=id)
    return render(request,'emp_module/empleave_view.html',{'data':st})


#Admin Register
def admin_register(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        us=request.POST['usertype']
        t=CustomUser.objects.create_user(username=u,password=p,usertype=us)
        t.save()
    return render(request,'admin_module/admin_register.html')


#ADMIN MODULE
@login_required
def admin_index(request):
    st=CustomUser.objects.filter(usertype="hr")
    context = {
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(CustomUser.objects.filter(usertype="employee")),
        'total_clients':len(Clients.objects.all()),
        'total_projects':len(Projects.objects.all()),
        'data':st     
    }
    return render(request, 'admin_module/admin_index.html',context)


@login_required
def adep_reg(request):
    if request.method=="POST":
        n=request.POST['depname']
        d=request.POST['depdescription']
        s=request.POST['depstatus']
        t=Department.objects.create(name=n,description=d,status=s)
        t.save()
        return redirect(adep_view)
    return render(request,'admin_module/department/dep_reg.html')

@login_required
def adep_view(request):
    st=Department.objects.all()
    return render(request,'admin_module/department/dep_view.html',{'data':st})

@login_required
def apos_reg(request):
    if request.method=="POST":
        n=request.POST['posname']
        s=request.POST['posstatus']
        d=request.POST['depname']
        dep= Department.objects.get(id=d)
        t=Position.objects.create(name=n,department_id=dep,status=s)
        t.save()
        return redirect(apos_view)
    else:
        s=Department.objects.all()
        context = {
        'department' : s}
    return render(request,'admin_module/department/pos_reg.html',context)

@login_required
def apos_view(request):
    st=Position.objects.all()
    return render(request,'admin_module/department/pos_view.html',{'data':st})

@login_required
def adepheadreg(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        c=request.POST['code']
        g=request.POST['gender']
        dob=request.POST['dob']
        con=request.POST['contact']
        ad=request.POST['address']
        em=request.POST['email']
        date=request.POST['datehired']
        sa=request.POST['salary']
        st=request.POST['status']
        d=request.POST['depname']
        dep= Department.objects.get(id=d)
        t=DepartmentHead.objects.create(department_id=dep,code=c,firstname=fn,lastname=ln,gender=g,dob=dob,contact=con,address=ad,email=em,
                                date_hired=date,salary=sa,status=st)
        t.save()
        return redirect(adepheadview)
    else:
        s=Department.objects.all()
        context = {
        'department' : s}
    return render(request, 'admin_module/department/dep_head_reg.html',context)


@login_required
def adepheadview(request):
    st=DepartmentHead.objects.all()
    return render(request,'admin_module/department/dep_head_view.html',{'data':st})

@login_required
def aemp_reg(request):
    if request.method=="POST":
        us=request.POST['username']
        pa=request.POST['password']
        user=request.POST['usertype']
        fn=request.POST['fname']
        ln=request.POST['lname']
        c=request.POST['code']
        g=request.POST['gender']
        dob=request.POST['dob']
        con=request.POST['contact']
        ad=request.POST['address']
        em=request.POST['email']
        date=request.POST['datehired']
        sa=request.POST['salary']
        st=request.POST['status']
        p=request.POST['posname']
        pos= Position.objects.get(id=p)
        t=CustomUser.objects.create_user(username=us,password=pa,usertype=user,position_id=pos,code=c,firstname=fn,lastname=ln,gender=g,dob=dob,contact=con,address=ad,email=em,
                                date_hired=date,salary=sa,status=st)
        t.save()
        return redirect(aemp_view)

    else:
        u=Position.objects.all()
        use=CustomUser.objects.filter(usertype="employee").values()
        context = {
            'user':use,
        'positions' : u}
    return render(request, 'admin_module/employee/emp_reg.html',context)

@login_required
def aemp_view(request):
    st=CustomUser.objects.filter(usertype="employee")
    u=Position.objects.all()
    context = {'data':st,
        'positions' : u}
    return render(request,'admin_module/employee/emp_view.html',context)

@login_required
def aemp_delete(request,id):
    st=CustomUser.objects.get(id=id)
    st.delete()
    return redirect(aemp_view)

@login_required
def aemp_edit(request,id):
    st=CustomUser.objects.get(id=id)
    u=Position.objects.all()
    context = {
        'data' :st,
        'positions' : u}
    return render(request,'admin_module/employee/emp_edit.html',context)


@login_required
def aemp_update(request,id):
    st=CustomUser.objects.get(id=id)
    if request.method=="POST":
        st.username=request.POST['username']
        st.password=request.POST['password']
        st.code=request.POST['code']
        st.firstname=request.POST['fname']
        st.lastname=request.POST['lname']
        st.gender=request.POST['gender']
        st.dob=request.POST['dob']
        st.contact=request.POST['contact']
        st.address=request.POST['address']
        st.email=request.POST['email']
        st.date_hired=request.POST['datehired']
        st.salary=request.POST['salary']
        position_id=request.POST['posname']
        dep = Position.objects.get(id=position_id)
        st.position_id = dep
        st.status=request.POST['status']
        st.save()
        return redirect(aemp_view)
    else:
        st=CustomUser.objects.get(id=id)
        u=Position.objects.all()
        context = {
            'data' :st,
            'positions' : u}
    return render(request, 'admin_module/employee/emp_view.html',context)


@login_required
def aempindview(request,id):
    st=CustomUser.objects.get(id=id)
    return render(request,'admin_module/employee/emp_ind_view.html',{'data':st})

@login_required
def aleavetype_reg(request):
    if request.method=="POST":
        n=request.POST['leavetype']
        t=LeaveType.objects.create(leavetype=n)
        t.save()
        return redirect(aleavetype_reg)
    st=LeaveType.objects.all()
    return render(request,'admin_module/leave/leavetype_reg.html',{'data':st})

@login_required
def aleavetype_delete(request,id):
    st=LeaveType.objects.get(id=id)
    st.delete()
    return redirect(aleavetype_reg)

@login_required
def aadmleave_view(request):
    st=AdminLeave.objects.all()
    return render(request,'admin_module/leave/admleave_view.html',{'data':st})

@login_required
def aclient_reg(request):
    if request.method=="POST":
        fn=request.POST['fname']
        co=request.POST['code']
        cn=request.POST['company']
        pn=request.POST['project']
        em=request.POST['email']
        s=request.POST['status']
        t=Clients.objects.create(code=co,fullname=fn,company_name=cn,
                                 projects_no=pn,email=em,status=s)
        t.save()
        return redirect(aclient_view)
    return render(request,'admin_module/client/client_reg.html')

@login_required
def aclient_view(request):
    st=Clients.objects.all()
    return render(request,'admin_module/client/client_view.html',{'data':st})


@login_required
def aclientcom_reg(request):
    if request.method=="POST":
        ow=request.POST['owner']
        ad=request.POST['address']
        cn=request.POST['company']
        pn=request.POST['project']
        em=request.POST['email']
        s=request.POST['status']
        t=ClientCompany.objects.create(owner=ow,address=ad,company_name=cn,
                                 projects_no=pn,email=em,status=s)
        t.save()
        return redirect(aclientcom_view)
    return render(request,'admin_module/client/clientcom_reg.html')

@login_required
def aclientcom_view(request):
    st=ClientCompany.objects.all()
    return render(request,'admin_module/client/clientcom_view.html',{'data':st})

@login_required
def aproject_reg(request):
    if request.method=="POST":
        fd=request.POST['fdate']
        td=request.POST['tdate']
        ti=request.POST['title']
        de=request.POST['description']
        s=request.POST['status']
        c=request.POST['company']
        p=request.POST['position']
        e=request.POST['employee']
        com= ClientCompany.objects.get(id=c)
        pos= Position.objects.get(id=p)
        emp= CustomUser.objects.get(id=e)
        t=Projects.objects.create(title=ti,emp_id=emp,company_id=com,position_id=pos,from_date=fd,to_date=td,
                                  project_description=de,status=s)
        t.save()
        return redirect(aproject_view)
    else:
        empl=CustomUser.objects.filter(usertype="employee")
        comp=ClientCompany.objects.all()
        posi=Position.objects.all()
        context = {'company':comp,'positions':posi,'employees':empl}
    return render(request,'admin_module/project/project_reg.html',context)

@login_required
def aproject_view(request):
    st=Projects.objects.all()
    return render(request,'admin_module/project/project_view.html',{'data':st})

@login_required
def aproject_delete(request,id):
    st=Projects.objects.get(id=id)
    st.delete()
    return redirect(aproject_view)

@login_required
def aprojectindview(request,id):
    st=Projects.objects.get(id=id)
    return render(request,'admin_module/project/projectind_view.html',{'data':st})

@login_required
def acourse_reg(request):
    if request.method=="POST":
        tr=request.POST['trainer']
        co=request.POST['course']
        c=request.POST['cost']
        t=TrainingType.objects.create(trainer=tr,course=co,cost=c)
        t.save()
        return redirect(acourse_view)
    return render(request,'admin_module/training/course_reg.html')

@login_required
def acourse_view(request):
    st=TrainingType.objects.all()
    return render(request,'admin_module/training/course_view.html',{'data':st})

@login_required
def atraining_reg(request):
    if request.method=="POST":
        fd=request.POST['fdate']
        td=request.POST['tdate']
        bt=request.POST['time']
        c=request.POST['course']
        s=request.POST['status']
        cou= TrainingType.objects.get(id=c)
        t=Training.objects.create(training_id=cou,from_date=fd,to_date=td,batch_time=bt,status=s)
        t.save()
        return redirect(atraining_view)
    else:
        s=TrainingType.objects.all()
        context = {
        'course' : s}
    return render(request,'admin_module/training/training_reg.html',context)

@login_required
def atraining_view(request):
    st=Training.objects.all()
    return render(request,'admin_module/training/training_view.html',{'data':st})


@login_required
def aadmleave_view(request):
    st=AdminLeave.objects.all()
    return render(request,'admin_module/leave/admleave_view.html',{'data':st})



#HR MODULE
@login_required
def index(request):
    context = {
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(CustomUser.objects.filter(usertype="employee")),
        'total_clients':len(Clients.objects.all()),
        'total_projects':len(Projects.objects.all()),
    }
    return render(request, 'index.html',context)

@login_required
def hr_profile(request):   
    return render(request, 'hr/hr_profile.html')



##DEPARTMENT

@login_required
def dep_reg(request):
    if request.method=="POST":
        n=request.POST['depname']
        d=request.POST['depdescription']
        s=request.POST['depstatus']
        t=Department.objects.create(name=n,description=d,status=s)
        t.save()
        return redirect(dep_view)
    return render(request,'department/dep_reg.html')

@login_required
def dep_view(request):
    st=Department.objects.all()
    return render(request,'department/dep_view.html',{'data':st})

@login_required
def dep_edit(request,id):
    st=Department.objects.get(id=id)
    return render(request,'department/dep_edit.html',{'data':st})

@login_required
def dep_delete(request,id):
    st=Department.objects.get(id=id)
    st.delete()
    return redirect(dep_view)

@login_required
def dep_update(request,id):
    st=Department.objects.get(id=id)
    if request.method=="POST":
        st.name=request.POST['depname']
        st.description=request.POST['depdescription']
        st.status=request.POST['depstatus']
        st.save()
        return redirect(dep_view)
    return HttpResponse("Successfully Update")



##POSITION

@login_required
def pos_reg(request):
    if request.method=="POST":
        n=request.POST['posname']
        s=request.POST['posstatus']
        d=request.POST['depname']
        dep= Department.objects.get(id=d)
        t=Position.objects.create(name=n,department_id=dep,status=s)
        t.save()
        return redirect(pos_view)
    else:
        s=Department.objects.all()
        context = {
        'department' : s}
    return render(request,'department/pos_reg.html',context)

@login_required
def pos_view(request):
    st=Position.objects.all()
    return render(request,'department/pos_view.html',{'data':st})

@login_required
def pos_edit(request,id):
    st=Position.objects.get(id=id)
    s=Department.objects.all()
    context = {
        'data' :st,
        'department' : s}
    return render(request,'department/pos_edit.html',context)

@login_required
def pos_delete(request,id):
    st=Position.objects.get(id=id)
    st.delete()
    return redirect(pos_view)

@login_required
def pos_update(request,id):
    st=Position.objects.get(id=id)
    if request.method=="POST":
        st.name=request.POST['posname']
        st.status=request.POST['posstatus']
        department_id=request.POST['depname']
        dep = Department.objects.get(id=department_id)
        st.department_id = dep
        st.save()
        return redirect(pos_view)
    s = Department.objects.all()
    context = {
        'data': st,
        'department': s
    }
    return render(request, 'department/pos_view.html', context)




##EMPLOYEE

@login_required
def emp_reg(request):
    if request.method=="POST":
        us=request.POST['username']
        pa=request.POST['password']
        user=request.POST['usertype']
        fn=request.POST['fname']
        ln=request.POST['lname']
        c=request.POST['code']
        g=request.POST['gender']
        dob=request.POST['dob']
        con=request.POST['contact']
        ad=request.POST['address']
        em=request.POST['email']
        date=request.POST['datehired']
        sa=request.POST['salary']
        st=request.POST['status']
        p=request.POST['posname']
        pos= Position.objects.get(id=p)
        t=CustomUser.objects.create_user(username=us,password=pa,usertype=user,position_id=pos,code=c,firstname=fn,lastname=ln,gender=g,dob=dob,contact=con,address=ad,email=em,
                                date_hired=date,salary=sa,status=st)
        t.save()
        return redirect(emp_view)

    else:
        u=Position.objects.all()
        use=CustomUser.objects.filter(usertype="employee").values()
        context = {
            'user':use,
        'positions' : u}
    return render(request, 'employee/emp_reg.html',context)

@login_required
def emp_view(request):
    st=CustomUser.objects.filter(usertype="employee")
    context = {'data':st}
    return render(request,'employee/emp_view.html',context)

@login_required
def empsalary_view(request):
    st=CustomUser.objects.filter(usertype="employee")
    u=Position.objects.all()
    context = {'data':st,
        'positions' : u}
    return render(request,'employee/empsalary.html',context)

@login_required
def emp_edit(request,id):
    st=CustomUser.objects.get(id=id)
    u=Position.objects.all()
    context = {
        'data' :st,
        'positions' : u}
    return render(request,'employee/emp_edit.html',context)

@login_required
def emp_delete(request,id):
    st=CustomUser.objects.get(id=id)
    st.delete()
    return redirect(emp_view)

@login_required
def emp_update(request,id):
    st=CustomUser.objects.get(id=id)
    if request.method=="POST":
        st.username=request.POST['username']
        st.password=request.POST['password']
        st.code=request.POST['code']
        st.firstname=request.POST['fname']
        st.lastname=request.POST['lname']
        st.gender=request.POST['gender']
        st.dob=request.POST['dob']
        st.contact=request.POST['contact']
        st.address=request.POST['address']
        st.email=request.POST['email']
        st.date_hired=request.POST['datehired']
        st.salary=request.POST['salary']
        position_id=request.POST['posname']
        dep = Position.objects.get(id=position_id)
        st.position_id = dep
        st.status=request.POST['status']
        st.save()
        return redirect(emp_view)
    else:
        st=CustomUser.objects.get(id=id)
        u=Position.objects.all()
        context = {
            'data' :st,
            'positions' : u}
    return render(request, 'employee/emp_view.html',context)


@login_required
def empindview(request,id):
    st=CustomUser.objects.get(id=id)
    return render(request,'employee/emp_ind_view.html',{'data':st})


##ADMIN

@login_required
def adm_reg(request):
    if request.method=="POST":
        us=request.POST['username']
        pa=request.POST['password']
        user=request.POST['usertype']
        fn=request.POST['fname']
        ln=request.POST['lname']
        c=request.POST['code']
        g=request.POST['gender']
        dob=request.POST['dob']
        con=request.POST['contact']
        ad=request.POST['address']
        em=request.POST['email']
        date=request.POST['datehired']
        sa=request.POST['salary']
        st=request.POST['status']
        t=CustomUser.objects.create_user(username=us,password=pa,usertype=user,code=c,firstname=fn,lastname=ln,gender=g,dob=dob,contact=con,address=ad,email=em,
                                date_hired=date,salary=sa,status=st)
        t.save()
        return redirect(adm_view)
    return render(request, 'admin/adm_reg.html')


@login_required
def adm_view(request):
    st=CustomUser.objects.filter(usertype="hr").values()
    return render(request,'admin/adm_view.html',{'data':st})

@login_required
def admsalary_view(request):
    st=CustomUser.objects.filter(usertype="hr").values()
    return render(request,'admin/admsalary.html',{'data':st})

@login_required
def adm_edit(request,id):
    st=CustomUser.objects.get(id=id)
    return render(request,'admin/adm_edit.html',{'data':st})

@login_required
def adm_delete(request,id):
    st=CustomUser.objects.get(id=id)
    st.delete()
    return redirect(adm_view)

@login_required
def adm_update(request,id):
    st=CustomUser.objects.get(id=id)
    if request.method=="POST":
        st.username=request.POST['username']
        st.password=request.POST['password']
        st.code=request.POST['code']
        st.firstname=request.POST['fname']
        st.lastname=request.POST['lname']
        st.gender=request.POST['gender']
        st.dob=request.POST['dob']
        st.contact=request.POST['contact']
        st.address=request.POST['address']
        st.email=request.POST['email']
        st.date_hired=request.POST['datehired']
        st.salary=request.POST['salary']
        st.status=request.POST['status']
        st.save()
        return redirect(adm_view)
    return render(request,'admin/adm_view.html',{'data':st})

@login_required
def admindview(request,id):
    st=CustomUser.objects.get(id=id)
    return render(request,'admin/adm_ind_view.html',{'data':st})



##Department Head

@login_required
def depheadreg(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        c=request.POST['code']
        g=request.POST['gender']
        dob=request.POST['dob']
        con=request.POST['contact']
        ad=request.POST['address']
        em=request.POST['email']
        date=request.POST['datehired']
        sa=request.POST['salary']
        st=request.POST['status']
        d=request.POST['depname']
        dep= Department.objects.get(id=d)
        t=DepartmentHead.objects.create(department_id=dep,code=c,firstname=fn,lastname=ln,gender=g,dob=dob,contact=con,address=ad,email=em,
                                date_hired=date,salary=sa,status=st)
        t.save()
        return redirect(depheadview)
    else:
        s=Department.objects.all()
        context = {
        'department' : s}
    return render(request, 'department/dep_head_reg.html',context)


@login_required
def depheadview(request):
    st=DepartmentHead.objects.all()
    return render(request,'department/dep_head_view.html',{'data':st})

@login_required
def depheadedit(request,id):
    st=DepartmentHead.objects.get(id=id)
    s=Department.objects.all()
    context = {
        'data' :st,
        'department' : s}
    return render(request,'department/dep_head_edit.html',context)

@login_required
def depheaddelete(request,id):
    st=DepartmentHead.objects.get(id=id)
    st.delete()
    return redirect(depheadview)

@login_required
def depheadupdate(request,id):
    st=DepartmentHead.objects.get(id=id)
    if request.method=="POST":
        st.code=request.POST['code']
        st.firstname=request.POST['fname']
        st.lastname=request.POST['lname']
        st.gender=request.POST['gender']
        st.dob=request.POST['dob']
        st.contact=request.POST['contact']
        st.address=request.POST['address']
        st.email=request.POST['email']
        st.date_hired=request.POST['datehired']
        st.salary=request.POST['salary']
        st.status=request.POST['status']
        department_id=request.POST['depname']
        dep = Department.objects.get(id=department_id)
        st.department_id = dep
        st.save()
        return redirect(depheadview)
    s = Department.objects.all()
    context = {
        'data': st,
        'department': s
    }
    return render(request,'department/dep_head_view.html',context)

@login_required
def depheadindview(request,id):
    st=DepartmentHead.objects.get(id=id)
    return render(request,'department/dep_head_indview.html',{'data':st})



##Leave

@login_required
def leavetype_reg(request):
    if request.method=="POST":
        n=request.POST['leavetype']
        t=LeaveType.objects.create(leavetype=n)
        t.save()
        return redirect(leavetype_reg)
    st=LeaveType.objects.all()
    return render(request,'leave/leavetype_reg.html',{'data':st})

@login_required
def leavetype_delete(request,id):
    st=LeaveType.objects.get(id=id)
    st.delete()
    return redirect(leavetype_reg)

#Employee Leave

@login_required
def empleave_reg(request):
    if request.method=="POST":
        fd=request.POST['fdate']
        td=request.POST['tdate']
        dn=request.POST['days']
        re=request.POST['reason']
        d=request.POST['employee']
        l=request.POST['leave']
        s=request.POST['status']
        emp= CustomUser.objects.get(id=d)
        lea= LeaveType.objects.get(id=l)
        t=EmployeeLeave.objects.create(from_date=fd,to_date=td,days_no=dn,reason=re,
                                  emp_id=emp,leavetype_id=lea,status=s)
        t.save()
        return redirect(empleave_reg)
    else:
        empl=CustomUser.objects.filter(usertype="employee").values()
        leav=LeaveType.objects.all()
        context = {'employee':empl,'leave' : leav}
    return render(request,'emp_module/empleave_reg.html',context)

@login_required
def adempleave_view(request):
    st=EmployeeLeave.objects.all()
    return render(request,'leave/empleave_view.html',{'data':st})

@login_required
def empleave_view(request):
    st=EmployeeLeave.objects.all()
    return render(request,'admin_module/employee/empleave_view.html',{'data':st})

@login_required
def empleave_edit(request,id):
    st=EmployeeLeave.objects.get(id=id)
    s=CustomUser.objects.all()
    le= LeaveType.objects.all()

    context = {
        'data' :st,
        'user' : s,
        'leave' : le}
    return render(request,'admin_module/employee/empleave_edit.html',context)


@login_required
def empleave_update(request,id):
    st=EmployeeLeave.objects.get(id=id)
    if request.method=="POST":
        st.status=request.POST['status']
        st.save()
        return redirect(empleave_view)
    s = CustomUser.objects.all()
    l= LeaveType.objects.all()
    context = {
        'data': st,
        'user': s,
        'leave': l
    }
    return render(request,'admin_module/employee/empleave_view.html',context)


@login_required
def empleave_delete(request,id):
    st=EmployeeLeave.objects.get(id=id)
    st.delete()
    return redirect(empleave_view)

#Admin Leave

@login_required
def admleave_reg(request):
    if request.method=="POST":
        fd=request.POST['fdate']
        td=request.POST['tdate']
        dn=request.POST['days']
        re=request.POST['reason']
        s=request.POST['status']
        d=request.POST['admin']
        l=request.POST['leave']
        adm= CustomUser.objects.get(id=d)
        lea= LeaveType.objects.get(id=l)
        t=AdminLeave.objects.create(from_date=fd,to_date=td,days_no=dn,reason=re,
                                  adm_id=adm,leavetype_id=lea,status=s)
        t.save()
        return redirect(aadmleave_view)
    else:
        admi=CustomUser.objects.filter(usertype="hr").values()
        leav=LeaveType.objects.all()
        context = {'admin':admi,'leave':leav}
    return render(request,'admin_module/leave/admleave_reg.html',context)

@login_required
def admleave_view(request):
    st=AdminLeave.objects.all()
    return render(request,'leave/admleave_view.html',{'data':st})

@login_required
def admleave_edit(request,id):
    st=AdminLeave.objects.get(id=id)
    s=CustomUser.objects.all()
    le= LeaveType.objects.all()

    context = {
        'data' :st,
        'user' : s,
        'leave' : le}
    return render(request,'leave/admleave_edit.html',context)


@login_required
def admleave_update(request,id):
    st=AdminLeave.objects.get(id=id)
    if request.method=="POST":
        st.status=request.POST['status']
        st.save()
        return redirect(admleave_view)
    s = CustomUser.objects.all()
    l= LeaveType.objects.all()
    context = {
        'data': st,
        'user': s,
        'leave': l
    }
    return render(request,'leave/admleave_view.html',context)


@login_required
def admleave_delete(request,id):
    st=AdminLeave.objects.get(id=id)
    st.delete()
    return redirect(admleave_view)



##Clients

@login_required
def client_reg(request):
    if request.method=="POST":
        fn=request.POST['fname']
        co=request.POST['code']
        cn=request.POST['company']
        pn=request.POST['project']
        em=request.POST['email']
        s=request.POST['status']
        t=Clients.objects.create(code=co,fullname=fn,company_name=cn,
                                 projects_no=pn,email=em,status=s)
        t.save()
        return redirect(client_view)
    return render(request,'client/client_reg.html')

@login_required
def client_view(request):
    st=Clients.objects.all()
    return render(request,'client/client_view.html',{'data':st})


@login_required
def client_delete(request,id):
    st=Clients.objects.get(id=id)
    st.delete()
    return redirect(client_view)



##Client Company

@login_required
def clientcom_reg(request):
    if request.method=="POST":
        ow=request.POST['owner']
        ad=request.POST['address']
        cn=request.POST['company']
        pn=request.POST['project']
        em=request.POST['email']
        s=request.POST['status']
        t=ClientCompany.objects.create(owner=ow,address=ad,company_name=cn,
                                 projects_no=pn,email=em,status=s)
        t.save()
        return redirect(clientcom_view)
    return render(request,'client/clientcom_reg.html')

@login_required
def clientcom_view(request):
    st=ClientCompany.objects.all()
    return render(request,'client/clientcom_view.html',{'data':st})


@login_required
def clientcom_delete(request,id):
    st=ClientCompany.objects.get(id=id)
    st.delete()
    return redirect(clientcom_view)


##Projects

@login_required
def project_reg(request):
    if request.method=="POST":
        fd=request.POST['fdate']
        td=request.POST['tdate']
        ti=request.POST['title']
        de=request.POST['description']
        s=request.POST['status']
        c=request.POST['company']
        p=request.POST['position']
        e=request.POST['employee']
        com= ClientCompany.objects.get(id=c)
        pos= Position.objects.get(id=p)
        emp= CustomUser.objects.get(id=e)
        t=Projects.objects.create(title=ti,emp_id=emp,company_id=com,position_id=pos,from_date=fd,to_date=td,
                                  project_description=de,status=s)
        t.save()
        return redirect(project_view)
    else:
        empl=CustomUser.objects.filter(usertype="employee").values()
        comp=ClientCompany.objects.all()
        posi=Position.objects.all()
        context = {'company':comp,'positions':posi,'employees':empl}
    return render(request,'project/project_reg.html',context)

@login_required
def project_view(request):
    st=Projects.objects.all()
    return render(request,'project/project_view.html',{'data':st})


@login_required
def project_delete(request,id):
    st=Projects.objects.get(id=id)
    st.delete()
    return redirect(project_view)

@login_required
def projectindview(request,id):
    st=Projects.objects.get(id=id)
    return render(request,'project/projectind_view.html',{'data':st})


##Course Type

@login_required
def course_reg(request):
    if request.method=="POST":
        tr=request.POST['trainer']
        co=request.POST['course']
        c=request.POST['cost']
        t=TrainingType.objects.create(trainer=tr,course=co,cost=c)
        t.save()
        return redirect(course_view)
    return render(request,'training/course_reg.html')

@login_required
def course_view(request):
    st=TrainingType.objects.all()
    return render(request,'training/course_view.html',{'data':st})


@login_required
def course_edit(request,id):
    st=TrainingType.objects.get(id=id)
    return render(request,'training/course_edit.html',{'data':st})

@login_required
def course_delete(request,id):
    st=TrainingType.objects.get(id=id)
    st.delete()
    return redirect(course_view)

@login_required
def course_update(request,id):
    st=TrainingType.objects.get(id=id)
    if request.method=="POST":
        st.trainer=request.POST['trainer']
        st.course=request.POST['course']
        st.cost=request.POST['cost']
        st.save()
        return redirect(course_view)
    return HttpResponse("Successfully Update")


##Training

@login_required
def training_reg(request):
    if request.method=="POST":
        fd=request.POST['fdate']
        td=request.POST['tdate']
        bt=request.POST['time']
        c=request.POST['course']
        s=request.POST['status']
        cou= TrainingType.objects.get(id=c)
        t=Training.objects.create(training_id=cou,from_date=fd,to_date=td,batch_time=bt,status=s)
        t.save()
        return redirect(training_view)
    else:
        s=TrainingType.objects.all()
        context = {
        'course' : s}
    return render(request,'training/training_reg.html',context)

@login_required
def training_view(request):
    st=Training.objects.all()
    return render(request,'training/training_view.html',{'data':st})

@login_required
def training_edit(request,id):
    st=Training.objects.get(id=id)
    s=TrainingType.objects.all()
    context = {
        'data' :st,
        'course' : s}
    return render(request,'training/training_edit.html',context)

@login_required
def training_delete(request,id):
    st=Training.objects.get(id=id)
    st.delete()
    return redirect(training_view)

@login_required
def training_update(request,id):
    st=Training.objects.get(id=id)
    if request.method=="POST":
        st.from_date=request.POST['fdate']
        st.to_date=request.POST['tdate']
        st.batch_time=request.POST['time']
        st.status=request.POST['status']
        training_id=request.POST['course']
        cou = TrainingType.objects.get(id=training_id)
        st.training_id = cou
        st.save()
        return redirect(training_view)
    s = TrainingType.objects.all()
    context = {
        'data': st,
        'course': s
    }
    return render(request, 'training/training_view.html', context)


##Notification

@login_required
def not_reg(request):
    if request.method=="POST":
        ti=request.POST['title']
        me=request.POST['message']
        t=Notififaction.objects.create(title=ti,message=me)
        t.save()
        return redirect(not_reg)
    return render(request,'notification/not_reg.html')

@login_required
def not_view(request):
    st=Notififaction.objects.all()
    return render(request,'admin_module/notification/not_view.html',{'data':st})

@login_required
def not_delete(request,id):
    st=Notififaction.objects.get(id=id)
    st.delete()
    return redirect(not_view)



##EmpNotification

@login_required
def empnot_reg(request):
    if request.method=="POST":
        ti=request.POST['title']
        me=request.POST['message']
        t=EmpNotififaction.objects.create(title=ti,message=me)
        t.save()
        return redirect(empnot_reg)
    return render(request,'emp_module/not_reg.html')

@login_required
def empnot_view(request):
    st=EmpNotififaction.objects.all()
    return render(request,'admin_module/notification/empnot_view.html',{'data':st})

@login_required
def empnot_delete(request,id):
    st=EmpNotififaction.objects.get(id=id)
    st.delete()
    return redirect(empnot_view)


##EmpNotification

@login_required
def hrnot_reg(request):
    if request.method=="POST":
        ti=request.POST['title']
        me=request.POST['message']
        t=HrNotififaction.objects.create(title=ti,message=me)
        t.save()
        return redirect(hrnot_reg)
    return render(request,'admin_module/notification/not_reg.html')

@login_required
def hrnot_view(request):
    st=HrNotififaction.objects.all()
    return render(request,'emp_module/not_view.html',{'data':st})

@login_required
def hrnot_delete(request,id):
    st=HrNotififaction.objects.get(id=id)
    st.delete()
    return redirect(hrnot_view)
