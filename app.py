import sys
sys.path.append("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages")
from config import app
import views
import auth
import ssl

app.add_url_rule('/', view_func=views.home)
app.add_url_rule('/seo', view_func=views.seo)
app.add_url_rule('/event', view_func=views.event)
app.add_url_rule('/event_details', view_func=views.event_details, methods=['GET', 'POST'])
app.add_url_rule('/all_courses', view_func=views.all_courses)
app.add_url_rule('/course_details', view_func=views.course_details, methods=['GET', 'POST'])
app.add_url_rule('/profile', view_func=views.profile, methods=['GET', 'POST'])
app.add_url_rule('/edit_profile', view_func=views.edit_profile, methods=['GET', 'POST'])
app.add_url_rule('/change_password', view_func=views.change_password, methods=['GET', 'POST'])
app.add_url_rule('/my_preference', view_func=views.my_preference, methods=['GET', 'POST'])
app.add_url_rule('/why_timmins', view_func=views.why_timmins)
app.add_url_rule('/blogs_detail_timmins', view_func=views.blogs_detail_timmins)
app.add_url_rule('/blogs_timmins', view_func=views.blogs_timmins)
app.add_url_rule('/contact_us_timmins', view_func=views.contact_us_timmins, methods=['GET', 'POST'])
app.add_url_rule('/book_a_demo', view_func=views.book_a_demo, methods=['GET', 'POST'])
app.add_url_rule('/buy_ticket', view_func=views.buy_ticket, methods=['GET', 'POST'])
app.add_url_rule('/request_for_training', view_func=views.request_for_training, methods=['GET', 'POST'])
app.add_url_rule('/my_calendar', view_func=views.my_calendar, methods=['GET', 'POST'])

app.add_url_rule('/admin_panel', view_func=views.admin_panel, methods=['GET', 'POST'])
app.add_url_rule('/admin_courses_main', view_func=views.admin_courses_main)
app.add_url_rule('/admin_course_individual', view_func=views.admin_course_individual, methods=['GET', 'POST'])
app.add_url_rule('/admin_course_individual_update', view_func=views.admin_course_individual_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_course_individual_delete', view_func=views.admin_course_individual_delete, methods=['GET', 'POST'])
app.add_url_rule('/admin_new_course_upload', view_func=views.admin_new_course_upload, methods=['GET', 'POST'])
app.add_url_rule('/admin_domain_create', view_func=views.admin_domain_create)
app.add_url_rule('/admin_domain_upload', view_func=views.admin_domain_upload, methods=['GET', 'POST'])
app.add_url_rule('/admin_domain_view', view_func=views.admin_domain_view)
app.add_url_rule('/admin_domain_edit', view_func=views.admin_domain_edit, methods=['GET', 'POST'])
app.add_url_rule('/admin_domain_update', view_func=views.admin_domain_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_domain_edit_delete', view_func=views.admin_domain_edit_delete, methods=['GET', 'POST'])
app.add_url_rule('/admin_certification_create_new', view_func=views.admin_certification_create_new, methods=['GET', 'POST'])
app.add_url_rule('/admin_certification_view', view_func=views.admin_certification_view)
app.add_url_rule('/admin_certification_course_edit', view_func=views.admin_certification_course_edit, methods=['GET', 'POST'])
app.add_url_rule('/admin_certification_course_update', view_func=views.admin_certification_course_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_certification_course_edit_delete', view_func=views.admin_certification_course_edit_delete, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_profile', view_func=views.admin_user_profile)
app.add_url_rule('/admin_user_profile_update', view_func=auth.admin_user_profile_update, methods=['GET', 'POST'])

app.add_url_rule('/admin_training_calendar_new', view_func=views.admin_training_calendar_new, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_batches_list', view_func=views.admin_calendar_batches_list, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_individual_batch', view_func=views.admin_calendar_individual_batch, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_batch_details', view_func=views.admin_calendar_batch_details, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_sessions_list', view_func=views.admin_calendar_sessions_list)
app.add_url_rule('/admin_calendar_sessions_update', view_func=views.admin_calendar_sessions_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_add_new_session', view_func=views.admin_calendar_add_new_session, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_list_view', view_func=views.admin_calendar_list_view)
app.add_url_rule('/admin_calendar_edit_batches_list', view_func=views.admin_calendar_edit_batches_list, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_edit_batch_update', view_func=views.admin_calendar_edit_batch_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_edit_add_batch', view_func=views.admin_calendar_edit_add_batch, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_edit_add_batch_update', view_func=views.admin_calendar_edit_add_batch_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_edit_event_update', view_func=views.admin_calendar_edit_event_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_edit_batch_details_view', view_func=views.admin_calendar_edit_batch_details_view, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_no_batch_details', view_func=views.admin_calendar_no_batch_details, methods=['GET', 'POST'])
app.add_url_rule('/admin_calendar_edit_event_name', view_func=views.admin_calendar_edit_event_name, methods=['GET', 'POST'])

app.add_url_rule('/admin_user_calendar_create', view_func=views.admin_user_calendar_create, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_display_list', view_func=views.admin_user_display_list, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_details_view', view_func=views.admin_user_details_view, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_details_view_update', view_func=views.admin_user_details_view_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_batches_view', view_func=views.admin_user_batches_view, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_batch_delete', view_func=views.admin_user_batch_delete, methods=['GET', 'POST'])
app.add_url_rule('/admin_user_batches_view_update', view_func=views.admin_user_batches_view_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_event_users_mapping', view_func=views.admin_event_users_mapping)
app.add_url_rule('/admin_individual_event_mapped_users', view_func=views.admin_individual_event_mapped_users, methods=['GET', 'POST'])
app.add_url_rule('/admin_individual_event_mapped_users_delete', view_func=views.admin_individual_event_mapped_users_delete, methods=['GET', 'POST'])
app.add_url_rule('/admin_individual_event_user_create', view_func=views.admin_individual_event_user_create, methods=['GET', 'POST'])


app.add_url_rule('/admin_basic_calendar', view_func=views.admin_basic_calendar)
app.add_url_rule('/admin_banner_creation', view_func=views.admin_banner_creation, methods=['GET', 'POST'])

app.add_url_rule('/admin_courses', view_func=views.admin_courses)
app.add_url_rule('/admin_mailbox', view_func=views.admin_mailbox)
app.add_url_rule('/admin_mailbox', view_func=views.admin_mailbox)
app.add_url_rule('/admin_mailbox_compose', view_func=views.admin_mailbox_compose)
app.add_url_rule('/admin_mailbox_read', view_func=views.admin_mailbox_read)
app.add_url_rule('/admin_list_view_calendar', view_func=views.admin_list_view_calendar)
app.add_url_rule('/admin_bookmark', view_func=views.admin_bookmark)
app.add_url_rule('/admin_review', view_func=views.admin_review)
app.add_url_rule('/admin_add_listing', view_func=views.admin_add_listing)
app.add_url_rule('/admin_panel1', view_func=views.admin_panel1)
app.add_url_rule('/admin_teacher_profile', view_func=views.admin_teacher_profile)
app.add_url_rule('/individual_category_page', view_func=views.individual_category_page, methods=['GET', 'POST'])
app.add_url_rule('/certification', view_func=views.certification, methods=['GET', 'POST'])

app.add_url_rule('/login', view_func=auth.login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=auth.register, methods=['GET', 'POST'])
app.add_url_rule('/forgot_password', view_func=auth.forgot_password, methods=['GET', 'POST'])
app.add_url_rule('/otp_verification', view_func=auth.otp_verification, methods=['GET', 'POST'])
app.add_url_rule('/new_password', view_func=auth.new_password, methods=['GET', 'POST'])
app.add_url_rule('/new_user_password', view_func=auth.new_user_password, methods=['GET', 'POST'])
app.add_url_rule('/new_user_password_update', view_func=auth.new_user_password_update, methods=['GET', 'POST'])
app.add_url_rule('/header', view_func=auth.header)
app.add_url_rule('/footer', view_func=auth.footer)
app.add_url_rule('/contact_details_update', view_func=auth.contact_details_update, methods=['GET', 'POST'])
app.add_url_rule('/request_for_training_update', view_func=auth.request_for_training_update, methods=['GET', 'POST'])
app.add_url_rule('/buy_ticket_update', view_func=auth.buy_ticket_update, methods=['GET', 'POST'])
app.add_url_rule('/brochure_update', view_func=auth.brochure_update, methods=['GET', 'POST'])
app.add_url_rule('/book_a_demo_update', view_func=auth.book_a_demo_update, methods=['GET', 'POST'])
app.add_url_rule('/for_scripting', view_func=auth.for_scripting)
app.add_url_rule('/logout', view_func=auth.logout)
app.add_url_rule('/download', view_func=views.download_file, methods=['GET', 'POST'])
app.add_url_rule('/download_cs1', view_func=views.download_cs1, methods=['GET', 'POST'])
app.add_url_rule('/download_cs2', view_func=views.download_cs2, methods=['GET', 'POST'])
app.add_url_rule('/download_cs3', view_func=views.download_cs3, methods=['GET', 'POST'])
app.add_url_rule('/download_cs4', view_func=views.download_cs4, methods=['GET', 'POST'])

app.add_url_rule('/admin_testimonial_creation', view_func=views.admin_testimonial_creation, methods=['GET', 'POST'])
app.add_url_rule('/admin_testimonial_view', view_func=views.admin_testimonial_view)
app.add_url_rule('/admin_testimonial_edit', view_func=views.admin_testimonial_edit, methods=['GET', 'POST'])
app.add_url_rule('/admin_testimonial_update', view_func=views.admin_testimonial_update, methods=['GET', 'POST'])
app.add_url_rule('/admin_testimonial_edit_delete', view_func=views.admin_testimonial_edit_delete, methods=['GET', 'POST'])
app.add_url_rule('/admin_testimonial_for_individual_course_creation', view_func=views.admin_testimonial_for_individual_course_creation)
app.add_url_rule('/admin_testimonial_for_individual_course_creation_page', view_func=views.admin_testimonial_for_individual_course_creation_page, methods=['GET', 'POST'])
app.add_url_rule('/admin_testimonial_for_individual_course_upload', view_func=views.admin_testimonial_for_individual_course_upload, methods=['GET', 'POST'])
app.add_url_rule('/admin_testimonial_for_individual_course_edition', view_func=views.admin_testimonial_for_individual_course_edition)
app.add_url_rule('/admin_testimonial_for_individual_course_edition_page', view_func=views.admin_testimonial_for_individual_course_edition_page, methods=['GET', 'POST'])
app.add_url_rule('/admin_seo', view_func=views.admin_seo)
app.add_url_rule('/admin_seo_update', view_func=views.admin_seo_update,methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, port=4533)
    #ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #ssl_context.load_cert_chain(certfile='consult-timmins_com.crt', keyfile='timminsprod.key')
    #ssl_context.load_verify_locations(cafile='intermediate.crt')



