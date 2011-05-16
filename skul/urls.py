from django.conf.urls.defaults import *

urlpatterns = patterns('guider.skul.views',
    url(r'^$', 'root_view', name='main-page'),
    url(r'^student/register$', 'student_register', name='reg-student'),
    url(r'^teacher/addtopic$', 'teacher_addtopic', name='addtopic-teacher'),
    url(r'^student$', 'student_home', name='home-student'),
    url(r'^teacher$', 'teacher_home', name='home-teacher'),
    url(r'^FAQ$', 'FAQ_home', name='home-FAQ'),
    url(r'^contact$', 'contact', name='contact'),
    url(r'^student/login$', 'student_login', name='log-student'),
    url(r'^student/sedev$', 'student_sedev', name='sedev-student'),
    url(r'^student/yzleg/huvaari$', 'student_yzhuv', name='yzhuv-student'),
    url(r'^contact/message$', 'contact_message', name='message_contact'),
)
