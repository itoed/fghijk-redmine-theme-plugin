Redmine::Plugin.register :fghijk_redmine_theme_plugin do
  name 'FGHIJK Redmine Theme Plugin'
  author 'Eduardo Ito'
  description 'Stylesheets and custom layout for the FGHIJK Redmine installation'
  version '${project.version}'
  url 'https://fghijk.net/projects/fghijk-redmine-theme-plugin'
  author_url 'http://fghijk.net'

  delete_menu_item :top_menu, :home
  delete_menu_item :top_menu, :help
  menu :top_menu, :sources, 'https://gitlab.fghijk.net/public', :html => { 'target' => '_blank' }
  menu :top_menu, :builds, 'http://jenkins.fghijk.net', :html => { 'target' => '_blank' }
  menu :top_menu, :artifacts, 'http://nexus.fghijk.net', :html => { 'target' => '_blank' }
end
