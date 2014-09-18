Redmine::Plugin.register :test do
  name 'Test plugin'
  author 'Author name'
  description 'This is a plugin for Redmine'
  version '0.0.1'
  url 'http://example.com/path/to/plugin/hello'
  author_url 'http://example.com/about'
  delete_menu_item :top_menu, :help
end
