require 'active_support/inflector'

file = IO.read 'old/app/assets/scripts/app/views/shared/table_cell_views.js.coffee'

file.each_line do |line|
  if line.start_with? 'UI.'
    line_parts = line.split('=')
    name = line_parts.first.strip().split('.').last
    if name.include? 'View'
      name = name.gsub 'View', ''
      name = name.underscore.gsub('_', '-')
      #p "ember g view #{name}"
      p "ember g view #{name}"
    end
  end
end
