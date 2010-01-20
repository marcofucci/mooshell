from django.conf.urls.defaults import *

urlpatterns = patterns('mooshell.views',
    url(r'^mooshellmedia/(?P<path>.*)$', 'serve_static', name='mooshell_media'),
    url(r'^css/(?P<path>.*)$', 'serve_static', {'type': 'css'}, name='mooshell_css'),
    url(r'^js/(?P<path>.*)$', 'serve_static', {'type': 'js'}, name='mooshell_js'),
    url(r'^img/(?P<path>.*)$', 'serve_static', {'type': 'img'}, name='mooshell_img'),
	url(r'^codemirror/(?P<path>.*)$', 'serve_static', {'media': 'codemirror'}, name='codemirror'),
	url(r'^_save/$','pastie_save', name='pastie_save'),
	url(r'^_display/$','pastie_save', {'nosave': True}, name='pastie_display'),
	url(r'^_display/(?P<skin>\w+)/$','pastie_save', {'nosave': True}),
	url(r'^ajax_json_response/$','ajax_json_response', name='ajax_json_response'),
	url(r'^ajax_html_javascript_response/$','ajax_html_javascript_response', name='ajax_html_javascript_response'),
	url(r'^ajax_json_echo/$','ajax_json_echo', name='ajax_json_echo'),
	url(r'^ajax_json_echo/nodelay/$','ajax_json_echo', {'delay': False}, name='ajax_json_echo_nodelay'),
	url(r'^ajax_html_echo/$','ajax_html_echo', name='ajax_html_echo'),
	url(r'^ajax_html_echo/nodelay/$','ajax_html_echo', {'delay': False}, name='ajax_html_echo_nodelay'),
	url(r'^ajax_xml_echo/$','ajax_xml_echo', name='ajax_xml_echo'),
	url(r'^ajax_xml_echo/nodelay/$','ajax_xml_echo', {'delay': False}, name='ajax_xml_echo_nodelay'),
	url(r'^_get_dependencies/(?P<lib_id>.*)/$','get_dependencies', name='_get_dependencies'),
	url(r'^_get_library_versions/(?P<group_id>.*)/$','get_library_versions', name='_get_library_versions'),
	

	# compatibility with old mooshell/* urls DO NOT USE THEM
	url(r'^mooshell/ajax_json_response/$','ajax_json_response', name='old_ajax_json_response'),
	url(r'^mooshell/ajax_html_javascript_response/$','ajax_html_javascript_response', name='old_ajax_html_javascript_response'),
    url(r'^mooshell/(?P<slug>.*)/$','pastie_edit', name='old_pastie'),

	# embedded
	url(r'^(?P<slug>\w+)/embedded/$','embedded', name='embedded'),
	url(r'^(?P<slug>\w+)/embedded/(?P<tabs>.*)/(?P<skin>\w+)/$','embedded', name='embedded_with_tabs_and_skin'),
	url(r'^(?P<slug>\w+)/embedded/(?P<tabs>.*)/$','embedded', name='embedded_with_tabs'),
	url(r'^(?P<slug>\w+)/(?P<version>\d+)/embedded/$','embedded', name='embedded_with_version'),
	url(r'^(?P<slug>\w+)/(?P<version>\d+)/embedded/(?P<tabs>.*)/(?P<skin>\w+)/$','embedded', name='embedded_with_version_tabs_and_skin'),
	url(r'^(?P<slug>\w+)/(?P<version>\d+)/embedded/(?P<tabs>.*)/$','embedded', name='embedded_with_version_and_tabs'),
	url(r'^(?P<author>\w+)/(?P<slug>\w+)/embedded/$','embedded', name='author_embedded'),
	url(r'^(?P<author>\w+)/(?P<slug>\w+)/embedded/(?P<tabs>.*)/(?P<skin>\w+)/$','embedded', name='author_embedded_with_tabs_and_skin'),
	url(r'^(?P<author>\w+)/(?P<slug>\w+)/embedded/(?P<tabs>.*)/$','embedded', name='author_embedded_with_tabs'),
	url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/embedded/$','embedded', name='author_embedded_with_version'),
	url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/embedded/(?P<tabs>.*)/(?P<skin>\w+)/$','embedded', name='author_embedded_with_version_tabs_and_skin'),
	url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/embedded/(?P<tabs>.*)/$','embedded', name='author_embedded_with_version_and_tabs'),
	
	# simple API (parts)
    url(r'^(?P<slug>\w+)/show_html/$','show_part', {'part': 'html'}, name='show_html'),
    url(r'^(?P<slug>\w+)/show_css/$','show_part', {'part': 'css'}, name='show_css'),
    url(r'^(?P<slug>\w+)/show_js/$','show_part', {'part': 'js'}, name='show_js'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/show_html/$','show_part', {'part': 'html'}, name='show_html_with_version'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/show_css/$','show_part', {'part': 'css'}, name='show_css_with_version'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/show_js/$','show_part', {'part': 'js'}, name='show_js_with_version'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/show_html/$','show_part', {'part': 'html'}, name='author_show_html'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/show_css/$','show_part', {'part': 'css'}, name='author_show_css'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/show_js/$','show_part', {'part': 'js'}, name='author_show_js'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/show_html/$','show_part', {'part': 'html'}, name='author_show_html_with_version'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/show_css/$','show_part', {'part': 'css'}, name='author_show_css_with_version'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/show_js/$','show_part', {'part': 'js'}, name='author_show_js_with_version'),

	# API
	url(r'^api/user_shells/(?P<author>\w+)/$','api_get_users_pasties'),


    # show
    url(r'^(?P<slug>\w+)/show/$','pastie_show', name='pastie_show'),
    url(r'^(?P<slug>\w+)/show/(?P<skin>\w+)/$','pastie_show', name='pastie_show_with_skin'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/show/$','pastie_show', name='pastie_show_with_version'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/show/(?P<skin>\w+)/$','pastie_show', name='pastie_show_with_version_and_skin'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/show/$','pastie_show', name='author_pastie_show'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/show/(?P<skin>\w+)/$','pastie_show', name='author_pastie_show_with_skin'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/show/$','pastie_show', name='author_pastie_show_with_version'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/show/(?P<skin>\w+)/$','pastie_show', name='author_pastie_show_with_version_and_skin'),
    
	# main action
	url(r'^_make_favourite/$','make_favourite', name='make_favourite'),
	url(r'^_add_external_resource/$', 'add_external_resource', name='add_external_resource'),
    url(r'^(?P<slug>\w+)/$','pastie_edit', name='pastie'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/$','pastie_edit', name='shell'),
    url(r'^(?P<slug>\w+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/(?P<revision>\d+)/$','pastie_edit', name='revision'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^(?P<slug>\w+)/(?P<version>\d+)/(?P<revision>\d+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/$','pastie_edit', name='author_pastie'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/$','pastie_edit', name='author_shell'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/(?P<revision>\d+)/$','pastie_edit', name='author_revision'),
    url(r'^(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/(?P<revision>\d+)/(?P<skin>\w+)/$','pastie_edit'),
    
    
    url(r'^u/(?P<author>\w+)/(?P<slug>\w+)/$','pastie_edit', name='u_author_pastie'),
    url(r'^u/(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/$','pastie_edit', name='u_author_shell'),
    url(r'^u/(?P<author>\w+)/(?P<slug>\w+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^u/(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/(?P<skin>\w+)/$','pastie_edit'),
    url(r'^u/(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/(?P<revision>\d+)/$','pastie_edit', name='u_author_revision'),
    url(r'^u/(?P<author>\w+)/(?P<slug>\w+)/(?P<version>\d+)/(?P<revision>\d+)/(?P<skin>\w+)/$','pastie_edit'),
    
    url(r'^$','pastie_edit', name='pastie'),
   )
