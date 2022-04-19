from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from usermgmt.models import Member
#ctrl+클릭 => 링크 이동

from usermgmt.forms import MemberForm


def list_members(request):
    members = Member.objects.all()
    return render(request, 'usermgmt/list_members.html', {'members' : members})
# render => request 받아와 경로에 model의 members 객체 전달


def create_member(request):
    form = MemberForm(request.POST or None)
    # a line to create an object when a "submit" is requested.

    if form.is_valid():
            # function that return boolean (true/false) to confirm
            # that a form is valid or not.
        form.save()
        return redirect('list_members') # function to execute a HTML file according to the name

    return render(request, 'usermgmt/member_form.html', {'form': form})

# update member
def update_member(request, id):
    member = Member.objects.get(id=id) # get the one row matched id
    form = MemberForm(request.POST or None, instance=member)

    if form.is_valid():
        form.save()
        return redirect('list_members')

    return render(request, 'usermgmt/member_form.html', {'form': form, 'member': member})


def delete_member(request, id):
    member = Member.objects.get(id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('list_members')

    return render(request, 'usermgmt/member_delete_confirm.html', {'member': member})
