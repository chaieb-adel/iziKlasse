from django.conf.urls import include, url
from django.urls import path
from yaksh import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^update_email/$', views.update_email, name="update_email"),
    url(r'^activate/(?P<key>.+)$', views.activate_user, name="activate"),
    url(r'^new_activation/$', views.new_activation, name='new_activation'),
    url(r'^toggle_moderator/$', views.toggle_moderator_role,
        name='toggle_moderator'),
    url(r'^quizzes/$', views.quizlist_user, name='quizlist_user'),
    url(r'^results/$', views.results_user),
    url(r'^start/(?P<questionpaper_id>\d+)/(?P<module_id>\d+)/'
        '(?P<course_id>\d+)/$', views.start, name="start_quiz"),
    url(r'^start/(?P<attempt_num>\d+)/(?P<module_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<course_id>\d+)/$', views.start,
        name="start_quiz"),
    url(r'^quit/(?P<attempt_num>\d+)/(?P<module_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<course_id>\d+)/$', views.quit,
        name="quit_quiz"),
    url(r'^complete/$', views.complete, name="complete"),
    url(r'^complete/(?P<attempt_num>\d+)/(?P<module_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<course_id>\d+)/$', views.complete,
        name="complete"),
    url(r'^register/$', views.user_register, name="register"),
    url(r'^(?P<q_id>\d+)/check/$', views.check, name="check"),
    url(r'^get_result/(?P<uid>\d+)/(?P<course_id>\d+)/(?P<module_id>\d+)/$',
        views.get_result),
    url(r'^(?P<q_id>\d+)/check/(?P<attempt_num>\d+)/(?P<module_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<course_id>\d+)/$',
        views.check, name="check"),
    url(r'^(?P<q_id>\d+)/skip/(?P<attempt_num>\d+)/(?P<module_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<course_id>\d+)/$',
        views.skip, name="skip_question"),
    url(r'^(?P<q_id>\d+)/skip/(?P<next_q>\d+)/(?P<attempt_num>\d+)/'
        '(?P<module_id>\d+)/(?P<questionpaper_id>\d+)/(?P<course_id>\d+)/$',
        views.skip, name="skip_question"),
    url(r'^enroll_request/(?P<course_id>\d+)/$', views.enroll_request,
        name='enroll_request'),
    url(r'^self_enroll/(?P<course_id>\d+)/$', views.self_enroll,
        name='self_enroll'),
    url(r'^view_answerpaper/(?P<questionpaper_id>\d+)/(?P<course_id>\d+)$',
        views.view_answerpaper, name='view_answerpaper'),
    url(r'^download/user_assignment/(?P<question_id>\d+)/(?P<user_id>\d+)/'
        '(?P<quiz_id>\d+)/(?P<course_id>\d+)$',
        views.download_assignment_file, name="download_user_assignment"),
    url(r'^show_lesson/(?P<lesson_id>\d+)/(?P<module_id>\d+)/'
        '(?P<course_id>\d+)/$', views.show_lesson, name='show_lesson'),
    url(r'^quizzes/view_module/(?P<module_id>\d+)/(?P<course_id>\d+)/$',
        views.view_module, name='view_module'),
    url(r'^next_unit/(?P<course_id>\d+)/(?P<module_id>\d+)/'
        '(?P<current_unit_id>\d+)/$', views.get_next_unit, name='next_unit'),
    url(r'^next_unit/(?P<course_id>\d+)/(?P<module_id>\d+)/$',
        views.get_next_unit, name='next_unit'),
    url(r'^next_unit/(?P<course_id>\d+)/(?P<module_id>\d+)/'
        '(?P<current_unit_id>\d+)/(?P<first_unit>\d+)/$',
        views.get_next_unit, name='next_unit'),
    url(r'^course_modules/(?P<course_id>\d+)/$',
        views.course_modules, name='course_modules'),
    url(r'^forum/course_forum/(?P<course_id>\d+)/$',
        views.course_forum,
        name='course_forum'),
    url(r'^forum/lessons_forum/(?P<course_id>\d+)/$',
        views.lessons_forum, name='lessons_forum'),
    url(r'^forum/(?P<course_id>\d+)/post/(?P<uuid>[0-9a-f-]+)/$',
        views.post_comments,
        name='post_comments'),
    url(r'^forum/(?P<course_id>\d+)/post/(?P<uuid>[0-9a-f-]+)/delete/',
        views.hide_post,
        name='hide_post'),
    url(r'^forum/(?P<course_id>\d+)/comment/(?P<uuid>[0-9a-f-]+)/delete/',
        views.hide_comment,
        name='hide_comment'),
    url(r'^manage/$', views.prof_manage, name='manage'),
    url(r'^manage/addquestion/$', views.add_question, name="add_question"),
    url(r'^manage/addquestion/(?P<question_id>\d+)/$', views.add_question,
        name="add_question"),
    url(r'^manage/add_exercise/(?P<course_id>\d+)/(?P<module_id>\d+)/$',
        views.add_exercise, name='add_exercise'),
    url(r'^manage/add_exercise/(?P<course_id>\d+)/(?P<module_id>\d+)/(?P<quiz_id>\d+)$',
        views.add_exercise, name='edit_exercise'),
    url(r'^manage/addquiz/(?P<course_id>\d+)/(?P<module_id>\d+)/$',
        views.add_quiz, name='add_quiz'),
    url(r'^manage/addquiz/(?P<course_id>\d+)/(?P<module_id>\d+)/(?P<quiz_id>\d+)$',
        views.add_quiz, name='edit_quiz'),
    url(r'^manage/gradeuser/$', views.grade_user, name="grade_user"),
    url(r'^manage/gradeuser/(?P<quiz_id>\d+)/(?P<course_id>\d+)/$',
        views.grade_user, name="grade_user"),
    url(r'^manage/gradeuser/(?P<quiz_id>\d+)/(?P<user_id>\d+)/'
        '(?P<course_id>\d+)/$',
        views.grade_user, name="grade_user"),
    url(r'^manage/gradeuser/(?P<quiz_id>\d+)/(?P<user_id>\d+)/'
        '(?P<attempt_number>\d+)/(?P<course_id>\d+)/$',
        views.grade_user, name="grade_user"),
    url(r'^manage/questions/$', views.show_all_questions,
        name="show_questions"),
    url(r'^manage/monitor/$', views.monitor, name="monitor"),
    url(r'^manage/monitor/(?P<quiz_id>\d+)/(?P<course_id>\d+)/$',
        views.monitor, name="monitor"),
    url(r'^manage/monitor/(?P<quiz_id>\d+)/(?P<course_id>\d+)/(?P<attempt_number>\d+)/$',
        views.monitor, name="monitor"),
    url(r'^manage/user_data/(?P<user_id>\d+)/(?P<questionpaper_id>\d+)/'
        '(?P<course_id>\d+)/$',
        views.user_data, name="user_data"),
    url(r'^manage/user_data/(?P<user_id>\d+)/$', views.user_data),
    url(r'^manage/designquestionpaper/(?P<course_id>\d+)/(?P<quiz_id>\d+)/'
        '(?P<questionpaper_id>\d+)/$',
        views.design_questionpaper, name='designquestionpaper'),
    url(r'^manage/designquestionpaper/(?P<course_id>\d+)/(?P<quiz_id>\d+)/$',
        views.design_questionpaper, name='designquestionpaper'),
    url(r'^manage/statistics/question/(?P<questionpaper_id>\d+)/'
        '(?P<course_id>\d+)/$',
        views.show_statistics, name="show_statistics"),
    url(r'^manage/statistics/question/(?P<questionpaper_id>\d+)/'
        '(?P<attempt_number>\d+)/(?P<course_id>\d+)/$',
        views.show_statistics, name="show_statistics"),
    url(r'^manage/download_quiz_csv/(?P<course_id>\d+)/(?P<quiz_id>\d+)/$',
        views.download_quiz_csv, name="download_quiz_csv"),
    url(r'^manage/duplicate_course/(?P<course_id>\d+)/$',
        views.duplicate_course, name='duplicate_course'),
    url(r'manage/courses/$', views.courses, name='courses'),
    url(r'manage/add_course/$', views.add_course, name='add_course'),
    url(r'manage/edit_course/(?P<course_id>\d+)$', views.add_course,
        name='edit_course'),
    url(r'manage/course_detail/(?P<course_id>\d+)/$', views.course_detail,
        name='course_detail'),

    url(r'manage/enroll/(?P<course_id>\d+)/$', views.enroll_reject_user,
        name="enroll_reject_user"),
    url(r'manage/enroll/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        views.enroll_user, name="enroll_user"),
    url(r'manage/reject/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        views.reject_user, name="reject_user"),
    url(r'manage/enrolled/reject/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        views.reject_user, {'was_enrolled': True},
        name="reject_enrolled_user"),
    url(r'manage/enrolled/reject/(?P<course_id>\d+)/$',
        views.enroll_reject_user, {'was_enrolled': True},
        name="reject_enrolled_users"),
    url(r'manage/enroll/rejected/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        views.enroll_user, {'was_rejected': True},
        name="enroll_rejected_user"),
    url(r'manage/enroll/rejected/(?P<course_id>\d+)/$',
        views.enroll_reject_user, {'was_rejected': True},
        name="enroll_rejected_users"),

    url(r'manage/upload_users/(?P<course_id>\d+)/$', views.upload_users,
        name="upload_users"),
    url(r'manage/send_mail/(?P<course_id>\d+)/$', views.send_mail,
        name="send_mail"),

    url(r'manage/toggle_status/(?P<course_id>\d+)/$',
        views.toggle_course_status, name="toggle_course_status"),
    url(r'^questions/filter$', views.questions_filter,
        name="questions_filter"),
    url(r'^editprofile/$', views.edit_profile, name='edit_profile'),
    url(r'^viewprofile/$', views.view_profile, name='view_profile'),
    url(r'^generate_qrcode/(?P<answerpaper_id>\d+)/(?P<question_id>\d+)/'
        r'(?P<module_id>\d+)/$',
        views.generate_qrcode, name='generate_qrcode'),
    url(r'^upload_file/(?P<key>.+)/$', views.upload_file, name='upload_file'),
    url(r'^manage/searchteacher/(?P<course_id>\d+)/$', views.search_teacher,
        name="search_teacher"),
    url(r'^manage/addteacher/(?P<course_id>\d+)/$', views.add_teacher,
        name='add_teacher'),
    url(r'^manage/remove_teachers/(?P<course_id>\d+)/$', views.remove_teachers,
        name='remove_teacher'),
    url(r'^manage/download_questions/$', views.show_all_questions,
        name="download_questions"),
    url(r'^manage/upload_questions/$', views.show_all_questions,
        name="upload_questions"),
    url(r'^manage/regrade/paper/question/(?P<course_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<question_id>\d+)/$',
        views.regrade, name='regrade_by_quiz'),
    url(r'^manage/regrade/user/(?P<course_id>\d+)/(?P<questionpaper_id>\d+)/'
        '(?P<answerpaper_id>\d+)/$', views.regrade, name='regrade_by_user'),
    url(r'^manage/regrade/user/question/(?P<course_id>\d+)/'
        '(?P<questionpaper_id>\d+)/(?P<answerpaper_id>\d+)/'
        '(?P<question_id>\d+)/', views.regrade, name='regrade_by_question'),
    url(r'^manage/(?P<mode>godmode|usermode)/(?P<quiz_id>\d+)/'
        '(?P<course_id>\d+)/$', views.test_quiz, name="test_quiz"),
    url(r'^manage/create_demo_course/$', views.create_demo_course,
        name="create_demo_course"),
    url(r'^manage/courses/download_course_csv/(?P<course_id>\d+)/$',
        views.download_course_csv, name="download_course_csv"),
    url(r'^manage/download/user_assignment/(?P<question_id>\d+)/'
        '(?P<user_id>\d+)/(?P<quiz_id>\d+)/(?P<course_id>\d+)$',
        views.download_assignment_file, name="download_user_assignment"),
    url(r'^manage/download/quiz_assignments/(?P<quiz_id>\d+)/'
        '(?P<course_id>\d+)$', views.download_assignment_file,
        name="download_quiz_assignment"),
    url(r'^manage/courses/download_yaml_template/',
        views.download_yaml_template, name="download_yaml_template"),
    url(r'^manage/download_sample_csv/',
        views.download_sample_csv, name="download_sample_csv"),
    url(r'^manage/courses/edit_lesson/(?P<course_id>\d+)/(?P<module_id>\d+)/$',
        views.edit_lesson, name="edit_lesson"),
    url(r'^manage/courses/edit_lesson/(?P<course_id>\d+)/(?P<module_id>\d+)/(?P<lesson_id>\d+)/$',
        views.edit_lesson, name="edit_lesson"),
    url(r'^manage/courses/designmodule/(?P<module_id>\d+)/$',
        views.design_module, name="design_module"),
    url(r'^manage/courses/designmodule/(?P<module_id>\d+)/'
        '(?P<course_id>\d+)/$', views.design_module, name="design_module"),
    url(r'^manage/courses/add_module/(?P<course_id>\d+)/$',
        views.add_module, name="add_module"),
    url(r'^manage/courses/add_module/(?P<course_id>\d+)/(?P<module_id>\d+)/$',
        views.add_module, name="edit_module"),
    url(r'^manage/courses/designcourse/(?P<course_id>\d+)/$',
        views.design_course, name="design_course"),
    url(r'^manage/course_status/(?P<course_id>\d+)/$',
        views.course_status, name="course_status"),
    url(r'^manage/preview_questionpaper/(?P<questionpaper_id>\d+)/$',
        views.preview_questionpaper, name="preview_questionpaper"),
    url(r'^manage/get_user_status/(?P<course_id>\d+)/(?P<student_id>\d+)/$',
        views.get_user_data, name="get_user_data"),
    url(r'^manage/courses/download_course/(?P<course_id>\d+)/$',
        views.download_course, name="download_course"),
    url(r'^download_course/(?P<course_id>\d+)/$',
        views.download_course, name="download_course"),
    url(r'^manage/course/all/modules/(?P<course_id>\d+)',
        views.get_course_modules, name="get_course_modules"),
    url(r'^manage/course/teachers/(?P<course_id>\d+)',
        views.course_teachers, name="course_teachers"),
    url(r'^manage/download/course/progress/(?P<course_id>\d+)',
        views.download_course_progress, name="download_course_progress"),
    url(r'^manage/question/download/(?P<question_id>\d+)',
        views.download_question, name="download_question"),
    url(r'^manage/question/test/(?P<question_id>\d+)',
        views.test_question, name="test_question"),
    url(r'^manage/question/delete/(?P<question_id>\d+)',
        views.delete_question, name="delete_question"),
    url(r'^manage/search/questions', views.search_questions_by_tags,
        name="search_questions_by_tags"),
    path('view/notifications', views.view_notifications,
         name="view_notifications"),
    path('mark/notifications/<uuid:message_uid>',
        views.mark_notification, name="mark_notification"),
    path('mark/notifications', views.mark_notification,
         name="mark_notification"),
    url(r'^manage/micromanager/allow_special_attempt/(?P<user_id>\d+)/'
        '(?P<course_id>\d+)/(?P<quiz_id>\d+)/$',
        views.allow_special_attempt, name='allow_special_attempt'),
    url(r'^micromanager/special_start/(?P<micromanager_id>\d+)/$',
        views.special_start, name='special_start'),
    url(r'^manage/micromanager/special_revoke/(?P<micromanager_id>\d+)/$',
        views.revoke_special_attempt, name='revoke_special_attempt'),
    url(r'^manage/extend_time/(?P<paper_id>\d+)/$',
        views.extend_time, name='extend_time'),
    path('manage/add/marker/<int:course_id>/<int:lesson_id>', views.add_marker,
         name='add_marker'),
    path('manage/add/lesson/topic/<int:content_type>/<int:course_id>/<int:lesson_id>',
         views.add_topic, name='add_topic'),
    path('manage/edit/lesson/topic/<int:content_type>/<int:course_id>/<int:lesson_id>/'
         '<int:toc_id>/<int:topic_id>', views.add_topic, name='edit_topic'),
    path('manage/add/lesson/quiz/<int:content_type>/<int:course_id>/<int:lesson_id>',
         views.add_marker_quiz, name='add_marker_quiz'),
    path('manage/edit/lesson/quiz/<int:content_type>/<int:course_id>/<int:lesson_id>/'
         '<int:toc_id>/<int:question_id>', views.add_marker_quiz,
         name='edit_marker_quiz'),
    path('manage/remove/lesson/toc/<int:course_id>/<int:toc_id>',
         views.delete_toc, name='delete_toc'),
    path('get/marker/quiz/<int:course_id>/<int:toc_id>', views.get_marker_quiz,
         name='get_marker_quiz'),
    path('submit/marker/quiz/<int:course_id>/<int:toc_id>',
         views.submit_marker_quiz, name='submit_marker_quiz'),
    path('manage/lesson/stats/<int:course_id>/<int:lesson_id>',
         views.lesson_statistics, name='lesson_statistics'),
    path('manage/lesson/stats/<int:course_id>/<int:lesson_id>/<int:toc_id>',
         views.lesson_statistics, name='lesson_statistics'),
    path('manage/download/sample/toc',
         views.download_sample_toc, name='download_sample_toc'),
    path('manage/upload_marks/<int:course_id>/<int:questionpaper_id>/',
         views.upload_marks, name='upload_marks'),
    path(r'manage/upload_download_course_md/<int:course_id>',
        views.upload_download_course_md, name="upload_download_course_md"),
]
